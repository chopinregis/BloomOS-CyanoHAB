# Public record: western Lake Erie, 2014 and 2019

Downloaded public observations and archived NOAA products for a future retrospective replay
(scenario B of the BloomOS interface demonstrator). Start with **[Start Here.md](Start%20Here.md)**,
then read **[Integration Notes.md](Integration%20Notes.md)** before using any of it.

| Folder / file | Contents |
| --- | --- |
| `Originals/` | Downloaded source bytes, unmodified and checksum-verified: GLERL sample and station CSVs, compressed NDBC 45005 annual files, USGS daily-discharge responses, 2014 satellite GeoTIFFs and bulletins |
| `Prepared Data/` | Year-specific GLERL/CIGLR sample tables (CSV and structured JSON), station registry, quality flags, NDBC buoy 45005 records, USGS Maumee River daily discharge, satellite catalog, coverage summary |
| `Satellite Previews/` | PNG previews of 193 archived NOAA Cyanobacteria Index GeoTIFFs (display only; no georeferencing, colours are not toxin values) |
| `Documentation/` | Archive metadata, directory snapshots, the GLERL sampling-location map, the open-access methods paper, and `Verification.json` |
| `Tools/` | The acquisition, preparation and packaging scripts used to build this package |
| `Source Manifest.csv`, `acquisition.jsonl` | Source URL, retrieval time, byte count and SHA-256 for every downloaded file |
| `Data Overview.html` | Readable inventory with a date slider through the satellite previews (open locally in a browser) |

**Not included yet:** `Originals/Satellite/2019/` (144 source GeoTIFFs, 31 bulletin PDFs and 2
product notes). The 2019 satellite links in the manifest and the overview will not resolve until it
is added. The 2014 satellite originals and everything else, including all previews, are complete.

## Sources and terms

- GLERL/CIGLR western Lake Erie monitoring, DOI [10.25921/11da-3x54](https://doi.org/10.25921/11da-3x54)
  (NCEI accessions [0187718](https://www.ncei.noaa.gov/archive/accession/0187718) and
  [0209116](https://www.ncei.noaa.gov/archive/accession/0209116))
- NOAA NDBC station 45005; USGS station 04193500, Maumee River at Waterville
- NOAA Lake Erie HAB satellite and bulletin archives, NCEI
  [0242494](https://www.ncei.noaa.gov/archive/accession/0242494) (2014) and
  [0209038](https://www.ncei.noaa.gov/archive/accession/0209038) (2019)
- Boegehold et al. (2023), *Routine monitoring of western Lake Erie to track water quality changes
  associated with cyanobacterial harmful algal blooms*, Earth System Science Data 15, 3853,
  [CC BY 4.0](https://essd.copernicus.org/articles/15/3853/2023/)

These files keep their original sources' terms; the use and attribution statements are retained in
the archive metadata under `Documentation/`. The repository's CC BY-NC-SA 4.0 licence covers the
BloomOS specification, not these third-party data. Nothing here is endorsed by NOAA, GLERL, CIGLR,
NDBC or USGS, and lake samples are not finished drinking-water measurements.
