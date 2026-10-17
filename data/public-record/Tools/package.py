"""Validate acquisitions, make browser previews and package the public-data handoff."""
from pathlib import Path
import json, csv, hashlib, zipfile, html
from PIL import Image
R=Path(__file__).resolve().parents[1]
manifest=[json.loads(l) for l in (R/'acquisition.jsonl').read_text().splitlines()]
latest={r['file']:r for r in manifest}
fail=[]
for rec in latest.values():
    p=R/rec['file']
    if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest()!=rec['sha256']:fail.append(rec['file'])
assert not fail,fail
jobs=json.loads((R/'Tools/satellite_downloads.json').read_text())
assert all((R/path).exists() for _,path in jobs),'Satellite download incomplete'
catalog=json.loads((R/'Prepared Data/satellite_catalog.json').read_text())
out=R/'Satellite Previews';out.mkdir(exist_ok=True)
for i,r in enumerate(catalog):
    preview=out/f"{r['year']}_{i:03d}.png"
    im=Image.open(R/r['file']);im.convert('RGB').save(preview,optimize=True)
    r['preview']=preview.relative_to(R).as_posix()
    # Assert palette conversion preserves the rendered pixels; quantitative values remain in original TIFF.
    assert Image.open(preview).tobytes()==im.convert('RGB').tobytes()
(R/'Prepared Data/satellite_catalog.json').write_text(json.dumps(catalog,indent=2),encoding='utf-8')
summary=json.loads((R/'Prepared Data/coverage_summary.json').read_text())
with (R/'Source Manifest.csv').open('w',encoding='utf-8-sig',newline='') as f:
    fields=['file','source_url','resolved_url','retrieved_utc','bytes','content_type','sha256']
    w=csv.DictWriter(f,fields);w.writeheader();w.writerows(latest.values())
checks={'downloaded_files':len(latest),'sha256_checks_passed':len(latest),'satellite_files_expected':len(jobs),
        'satellite_files_present':len(jobs),'geotiffs_decoded':len(catalog),'png_previews_pixel_matched':len(catalog),
        'pdf_signature_checks':0,'row_count_checks':{}}
for p in (R/'Originals/Satellite').rglob('*.pdf'):
    assert p.read_bytes().startswith(b'%PDF-'),p
    checks['pdf_signature_checks']+=1
for year,expected in [(2014,126),(2019,219)]:
    path=R/f'Prepared Data/GLERL_{year}_all_fields.csv'
    rows=list(csv.DictReader(path.open(encoding='utf-8-sig')))
    assert len(rows)==expected
    assert len({r['record_id'] for r in rows})==expected
    checks['row_count_checks'][str(year)]=len(rows)
(R/'Documentation/Verification.json').write_text(json.dumps(checks,indent=2),encoding='utf-8')
page='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>BloomOS Public Data</title>
<style>*{box-sizing:border-box}body{margin:0;background:#eef2ef;color:#152b29;font:16px/1.6 system-ui}main{max-width:1200px;margin:auto;padding:45px 30px}h1{font-size:42px;line-height:1.1;margin:12px 0}h2{font-size:24px}.eyebrow{letter-spacing:.14em;font-size:12px;font-weight:700}section{background:white;border:1px solid #cad6ce;border-radius:14px;padding:25px;margin-top:25px}table{border-collapse:collapse;width:100%}td,th{padding:12px;text-align:left;border-bottom:1px solid #ddd}a{color:#086352}button,select{font:inherit;padding:7px 12px;border:1px solid #abbeb3;border-radius:6px;background:#fff}#frame{display:block;max-height:620px;max-width:100%;margin:15px auto;background:#111}#scrub{width:100%}.muted{color:#51635b;font-size:14px}code{overflow-wrap:anywhere}nav{display:flex;gap:20px;flex-wrap:wrap}</style>
<main><div class="eyebrow">BLOOMOS · PUBLIC RECORD PACKAGE · 17 OCTOBER 2026</div><h1>Lake Erie, from the source.</h1><p>Downloaded public observations and archived NOAA satellite products for 2014 and 2019. The current BloomOS interface has not been modified.</p>
<nav><a href="Start%20Here.md">Read the guide</a><a href="Source%20Manifest.csv">Source manifest</a><a href="Prepared%20Data/coverage_summary.json">Coverage details</a><a href="Documentation/Verification.json">File verification</a></nav>
<section><h2>What is here</h2><table><tr><th>Evidence</th><th>2014</th><th>2019</th></tr><tr><td>GLERL/CIGLR sample rows</td><td>126 · 21 sampling dates</td><td>219 · 18 sampling dates</td></tr><tr><td>NDBC 45005 weather rows</td><td>4,975</td><td>26,387</td></tr><tr><td>USGS daily river discharge</td><td>365 days</td><td>365 days</td></tr><tr><td>NOAA satellite GeoTIFFs</td><td>49 · 34 distinct dates</td><td>144 · 121 distinct dates</td></tr><tr><td>Archived NOAA bulletins</td><td>35</td><td>31</td></tr></table><p class="muted">Sample rows include different depths and occasional nonstandard site identifiers. Satellite file counts include different sensors or processing variants on the same day. These are the complete files listed in the selected archive image/bulletin folders, not a claim of complete daily observation coverage.</p></section>
<section><h2>Browse the genuine satellite products</h2><select id="year" aria-label="Year"><option>2014</option><option>2019</option></select> <button id="prev">Previous</button> <button id="next">Next</button><p id="label"></p><input id="scrub" type="range" min="0" value="0" aria-label="Satellite image"><img id="frame" alt="NOAA archived satellite product rendered with its embedded source palette"><p class="muted">Preview preserves the GeoTIFF’s embedded colour palette. It has no added geographic labels or quantitative legend. Inspect the original GeoTIFF and product documentation before interpreting pixel values; colours do not measure toxin concentration. Dates come from source filenames. Files can be edited or composited products.</p><p><a id="original">Original GeoTIFF</a> · <a id="source">NOAA file</a></p><code id="filename"></code></section>
<section><h2>Use in the replay</h2><p>Use real sample points and their dates, actual weather records, and the corresponding satellite product. Display missing evidence, uncertain station identifiers, sample depth, and source age. Keep inferred transport and policy outcomes explicitly separate from measurements.</p><p>Particulate and dissolved microcystin are separate laboratory results. They cannot automatically be treated as a validated drinking-water total. Satellite CI is also a different measurement. This package does not validate the demo’s advisory gates, decision index, authority log, or reconstructed Toledo treatment-plant history.</p><p><a href="Integration%20Notes.md">Integration notes and data limitations</a> · <a href="Prepared%20Data/GLERL_quality_flags.csv">Sample quality flags</a></p></section></main>
<script>const catalog=CATALOG;let rows=[];const y=document.querySelector('#year'),s=document.querySelector('#scrub');function draw(){const i=Number(s.value),r=rows[i];document.querySelector('#label').textContent=r.date_from_filename+' · '+r.platform+' · file '+(i+1)+' of '+rows.length;document.querySelector('#frame').src=r.preview;document.querySelector('#original').href=r.file;document.querySelector('#source').href=r.source_url;document.querySelector('#filename').textContent=r.file.split('/').pop()}function reset(){rows=catalog.filter(r=>String(r.year)===y.value).sort((a,b)=>a.date_from_filename.localeCompare(b.date_from_filename)||a.file.localeCompare(b.file));s.max=rows.length-1;s.value=0;draw()}y.onchange=reset;s.oninput=draw;document.querySelector('#prev').onclick=()=>{s.value=Math.max(0,Number(s.value)-1);draw()};document.querySelector('#next').onclick=()=>{s.value=Math.min(rows.length-1,Number(s.value)+1);draw()};reset();</script></html>'''
(R/'Data Overview.html').write_text(page.replace('CATALOG',json.dumps(catalog)),encoding='utf-8')
archive=R.parent/'BloomOS Public Data - 2014 and 2019.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
    for p in R.rglob('*'):
        if p.is_file() and '__pycache__' not in p.parts:
            z.write(p,Path('BloomOS Public Data')/p.relative_to(R))
with zipfile.ZipFile(archive) as z:assert z.testzip() is None
print(json.dumps({'verification':checks,'zip':str(archive),'zip_bytes':archive.stat().st_size},indent=2))
