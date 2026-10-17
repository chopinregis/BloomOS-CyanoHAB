from pathlib import Path
import re, json, html
from urllib.parse import urljoin
R=Path(__file__).resolve().parents[1]
jobs=[]
for year, base in [(2014,'https://www.ncei.noaa.gov/data/oceans/archive/arc0189/0242494/1.1/data/0-data/2014/'),(2019,'https://www.ncei.noaa.gov/data/oceans/archive/arc0152/0209038/1.1/data/0-data/')]:
    for label, folder in [('images','image'),('bulletins','bulletin'),('docs','doc')]:
        text=(R/f'Documentation/Satellite_{year}_{label}.html').read_text()
        names=[html.unescape(x) for x in re.findall(r'href="([^"]+)"',text) if x.lower().endswith(('.tif','.tiff','.pdf','.txt')) and '/' not in x]
        print(year,label,len(names),names[:2])
        for name in names:
            jobs.append([urljoin(base+folder+'/',name), f'Originals/Satellite/{year}/{folder}/{name}'])
(R/'Tools/satellite_downloads.json').write_text(json.dumps(jobs,indent=2),encoding='utf-8')
