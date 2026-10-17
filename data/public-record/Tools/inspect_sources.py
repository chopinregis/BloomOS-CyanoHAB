from pathlib import Path
import csv, gzip, json
from PIL import Image
R=Path(__file__).resolve().parents[1]
for p in (R/'Originals/GLERL').glob('*results*.csv'):
    rows=list(csv.DictReader(p.read_text(encoding='cp1252').splitlines()))
    print(p.name, 'rows',len(rows),'fields',list(rows[0]))
    for year in (2014,2019):
        subset=[r for r in rows if r['Date'].endswith(str(year))]
        if subset:
            print(year,len(subset), sorted(set(r['Site'] for r in subset)))
            print('first',subset[0])
for p in (R/'Originals/NDBC').glob('*.gz'):
    lines=gzip.decompress(p.read_bytes()).decode().splitlines()
    print(p.name,len(lines),lines[:3])
for p in (R/'Originals/USGS').glob('*.json'):
    data=json.loads(p.read_text())
    print(p.name,[(t['variable']['variableDescription'],t['variable']['unit'],sum(len(v['value']) for v in t['values'])) for t in data['value']['timeSeries']])
for year in (2014,2019):
    files=list((R/f'Originals/Satellite/{year}/image').glob('*.tif'))
    if files:
        p=files[0]
        im=Image.open(p)
        print(p.name, im.size,im.mode,dict(im.tag_v2))
