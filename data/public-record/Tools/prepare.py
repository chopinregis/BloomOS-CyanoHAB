"""Prepare traceable CSV/JSON data without modifying downloaded originals."""
from pathlib import Path
import csv, json, gzip, io, re, hashlib, math
from datetime import datetime, timedelta
from PIL import Image
R=Path(__file__).resolve().parents[1]
P=R/'Prepared Data'; P.mkdir(exist_ok=True)
summary={'glerl':{},'ndbc':{},'usgs':{},'satellite':{}}
issues=[]
def dump(name,rows):
    if not rows:return
    fields=list(dict.fromkeys(k for r in rows for k in r))
    with (P/name).open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fields);w.writeheader();w.writerows(rows)
def readcsv(path):
    body=path.read_bytes()
    try: text=body.decode('utf-8-sig')
    except UnicodeDecodeError:text=body.decode('cp1252')
    return list(csv.DictReader(io.StringIO(text)))
def number(v):
    try:return float(v)
    except (ValueError,TypeError):return None
def cell(v):
    v=(v or '').strip()
    if not v:return {'raw':v,'value':None,'qualifier':'missing','limit':None}
    if v.startswith(('<','>')):
        return {'raw':v,'value':None,'qualifier':v[0],'limit':number(v[1:])}
    n=number(v)
    return {'raw':v,'value':n,'qualifier':'numeric' if n is not None else 'unparsed','limit':None}
registry={}
for p in (R/'Originals/GLERL').glob('*coordinates*.csv'):
    for row in readcsv(p):
        site=row.get('station','').strip()
        if site:
            registry[site]={'site':site,'latitude':number(row.get('lat')),'longitude':number(row.get('long')),'source_file':str(p.relative_to(R))}
dump('GLERL_station_registry.csv',list(registry.values()))
for year in (2014,2019):
    source=R/('Originals/GLERL/lake_erie_habs_field_sampling_results_2012_2018_v2.csv' if year==2014 else 'Originals/GLERL/lake_erie_habs_field_sampling_results_2019.csv')
    rows=readcsv(source); selected=[]; observations=[]
    for line,row in enumerate(rows,2):
        if not row.get('Date'):continue
        date=datetime.strptime(row['Date'],'%m/%d/%Y').date()
        if date.year!=year:continue
        flags=[];site=row['Site'].strip()
        if site not in registry:flags.append('site_identifier_not_in_master_registry')
        lat=number(row.get('Latitude (decimal deg)'));lon=number(row.get('Longitude (decimal deg)'))
        if lat is None or lon is None:flags.append('sample_coordinates_missing')
        elif not(41.3<=lat<=42.4 and -83.8<=lon<=-82.0):flags.append('sample_coordinates_outside_western_erie_review_box')
        oid=f'glerl-{year}-L{line}'
        prefix={'record_id':oid,'date_iso':str(date),'source_file':str(source.relative_to(R)),'source_csv_line':line,'qa_flags':';'.join(flags)}
        selected.append({**prefix,**row})
        def field(prefix):
            keys=[k for k in row if k.startswith(prefix)]
            return row[keys[0]] if keys else ''
        obs={**prefix,'site':site,'sample_depth_category':row.get('Sample Depth (category)'),
             'sample_depth_m':number(row.get('Sample Depth (m)')),'local_time_eastern_raw':row.get('Local Time (Eastern Time Zone)'),
             'latitude_sample':lat,'longitude_sample':lon,'nominal_station':registry.get(site),
             'particulate_microcystin_ug_L':cell(field('Particulate Microcystin')),
             'dissolved_microcystin_ug_L':cell(field('Dissolved Microcystin')),
             'extracted_phycocyanin_ug_L':cell(field('Extracted Phycocyanin')),
             'extracted_chlorophyll_a_ug_L':cell(field('Extracted Chlorophyll a'))}
        observations.append(obs)
        if flags:issues.append({'record_id':oid,'source_file':str(source.relative_to(R)),'source_csv_line':line,'flags':';'.join(flags),'site_raw':site})
    dump(f'GLERL_{year}_all_fields.csv',selected)
    (P/f'GLERL_{year}_observations.json').write_text(json.dumps(observations,indent=2,ensure_ascii=False),encoding='utf-8')
    summary['glerl'][str(year)]={'rows':len(selected),'dates':len({r['date_iso'] for r in selected}),
        'start':min(r['date_iso'] for r in selected),'end':max(r['date_iso'] for r in selected),
        'registered_sites':sorted({r['site'] for r in observations if r['site'] in registry}),
        'unregistered_site_labels':sorted({r['site'] for r in observations if r['site'] not in registry}),
        'flagged_rows':sum(bool(r['qa_flags']) for r in observations),
        'particulate_microcystin':{q:sum(r['particulate_microcystin_ug_L']['qualifier']==q for r in observations) for q in ['numeric','<','>','missing','unparsed']},
        'dissolved_microcystin':{q:sum(r['dissolved_microcystin_ug_L']['qualifier']==q for r in observations) for q in ['numeric','<','>','missing','unparsed']}}
    src=R/f'Originals/NDBC/45005h{year}.txt.gz'
    lines=gzip.decompress(src.read_bytes()).decode('ascii').splitlines()
    (P/f'45005h{year}_original_uncompressed.txt').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    names=lines[0].lstrip('#').split();units=lines[1].lstrip('#').split();out=[]
    sentinels={'WDIR':999,'WSPD':99,'GST':99,'WVHT':99,'DPD':99,'APD':99,'MWD':999,'PRES':9999,'ATMP':999,'WTMP':999,'DEWP':999,'VIS':99,'TIDE':99}
    missing_counts={k:0 for k in sentinels}
    for line,s in enumerate(lines[2:],3):
        if not s.strip():continue
        values=s.split();assert len(values)==len(names),(line,len(values))
        raw=dict(zip(names,values));d=datetime(*[int(raw[k]) for k in ['YY','MM','DD','hh','mm']])
        record={'timestamp_utc':d.isoformat()+'Z','station':'45005','source_file':str(src.relative_to(R)),'source_text_line':line}
        for k in sentinels:
            val=float(raw[k]); missing=val==sentinels[k];missing_counts[k]+=missing
            record[k]=None if missing else val
            record[k+'_raw']=raw[k]
        out.append(record)
    dump(f'NDBC_45005_{year}.csv',out)
    summary['ndbc'][str(year)]={'rows':len(out),'start':out[0]['timestamp_utc'],'end':out[-1]['timestamp_utc'],'missing_by_variable':missing_counts,'units':dict(zip(names,units))}
    src=R/f'Originals/USGS/04193500_discharge_{year}.json'
    j=json.loads(src.read_text());out=[]
    for series in j['value']['timeSeries']:
        assert series['variable']['variableCode'][0]['value']=='00060'
        for block in series['values']:
            for v in block['value']:
                val=number(v['value']);val=None if val==series['variable']['noDataValue'] else val
                out.append({'site':'04193500','date':v['dateTime'][:10],'source_datetime':v['dateTime'],'discharge_ft3_s':val,
                    'qualifiers':';'.join(v['qualifiers']),'source_file':str(src.relative_to(R))})
    dump(f'USGS_04193500_discharge_{year}.csv',out)
    summary['usgs'][str(year)]={'rows':len(out),'start':out[0]['date'],'end':out[-1]['date'],'unit':'ft3/s','statistic':'daily mean','missing':sum(r['discharge_ft3_s'] is None for r in out)}
dump('GLERL_quality_flags.csv',issues)
satellite=[]
acquisitions=[json.loads(l) for l in (R/'acquisition.jsonl').read_text().splitlines()]
sources={r['file'].replace('\\','/'):r for r in acquisitions}
for year in (2014,2019):
    files=sorted((R/f'Originals/Satellite/{year}/image').glob('*.tif'))
    dates=[]
    for p in files:
        rel=p.relative_to(R).as_posix();m=re.search(r'\.(20\d{2})(\d{3})\.',p.name)
        date=(datetime(int(m[1]),1,1)+timedelta(days=int(m[2])-1)).date() if m else None
        im=Image.open(p);im.load()
        record={'year':year,'date_from_filename':str(date) if date else None,'platform':p.name.split('.')[0],
                'file':rel,'source_url':sources[rel]['source_url'],'sha256':sources[rel]['sha256'],
                'width':im.width,'height':im.height,'mode':im.mode,'description':im.tag_v2.get(270),
                'pixel_scale':list(im.tag_v2.get(33550,[])), 'tiepoint':list(im.tag_v2.get(33922,[])),
                'geokey_directory':list(im.tag_v2.get(34735,[])), 'geodouble_params':list(im.tag_v2.get(34736,[])),
                'geoascii_params':im.tag_v2.get(34737), 'gdal_nodata':im.tag_v2.get(42113)}
        satellite.append(record)
        if date:dates.append(str(date))
    summary['satellite'][str(year)]={'geotiffs':len(files),'unique_dates':len(set(dates)),'start':min(dates) if dates else None,'end':max(dates) if dates else None,
        'bulletins':len(list((R/f'Originals/Satellite/{year}/bulletin').glob('*.pdf')))}
(P/'satellite_catalog.json').write_text(json.dumps(satellite,indent=2),encoding='utf-8')
(P/'coverage_summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print(json.dumps(summary,indent=2))
