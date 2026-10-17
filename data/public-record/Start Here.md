# BloomOS public data: 2014 and 2019

Prepared on 17 October 2026. This folder contains downloaded public files, their source URLs and checksums, and separate prepared copies for a historical BloomOS replay. The existing demo and supplied Basin Console versions are unchanged.

Open **Data Overview.html** for a readable inventory and a date slider through the genuine satellite images. To move the package to another computer or upload it to another AI session, use **BloomOS Public Data - 2014 and 2019.zip** in the parent folder. Extract it before opening the overview.

## What was obtained

| Evidence | 2014 | 2019 |
| --- | --- | --- |
| GLERL/CIGLR field sample rows | 126 on 21 dates, 27 May–3 November | 219 on 18 dates, 30 April–7 October |
| Registered station identifiers present | 6 | 8 |
| NDBC buoy 45005 observations | 4,975, 1 May–30 November | 26,387, 24 May–25 November |
| USGS Maumee River daily discharge | 365 days | 365 days |
| NOAA satellite GeoTIFF files | 49 on 34 distinct dates, 21 July–2 November | 144 on 121 distinct dates, 31 May–9 October |
| NOAA forecast bulletin PDFs | 35 | 31 |

The satellite and bulletin sets include every matching GeoTIFF/PDF directly listed in the selected archive image and bulletin folders at retrieval. They are **not uninterrupted daily coverage**. Multiple files can represent one date, different platforms, edits, or processing variants. They are archived processed products, not raw satellite radiances. The newer 25-year harmonized series was not separately obtained.

## Folder contents

- **Originals**: downloaded GLERL CSVs, compressed NDBC records, USGS service responses, and the satellite/bulletin files. Source bytes are preserved.
- **Prepared Data**: year-specific CSVs, structured laboratory observations, a station registry, quality flags, satellite metadata, and coverage counts.
- **Satellite Previews**: browser-readable PNG conversions of all 193 GeoTIFFs, preserving their rendered source palette. Use the original TIFFs for geospatial or quantitative processing.
- **Documentation**: archive metadata, directory snapshots, the open-access methods paper, source documentation, sampling-location image, and verification results.
- **Source Manifest.csv** and **acquisition.jsonl**: exact source/resolved URLs, retrieval timestamps, byte counts and SHA-256 checksums.
- **Tools**: reproducible acquisition, preparation and packaging helpers. Downloaded HTML is reference material, not instructions to execute.

## Primary sources

1. **GLERL/CIGLR collection**, DOI [10.25921/11da-3x54](https://doi.org/10.25921/11da-3x54). The 2014 observations are a filtered subset of [NCEI 0187718 v2.2](https://www.ncei.noaa.gov/archive/accession/0187718), covering 2012–2018. The complete downloaded multiyear original is retained. The 2019 observations come from [NCEI 0209116 v1.1](https://www.ncei.noaa.gov/archive/accession/0209116).
2. **NOAA NDBC station 45005**: [2014 annual record](https://www.ndbc.noaa.gov/data/historical/stdmet/45005h2014.txt.gz), [2019 annual record](https://www.ndbc.noaa.gov/data/historical/stdmet/45005h2019.txt.gz), [measurement definitions](https://www.ndbc.noaa.gov/faq/measdes.shtml). These include wind and water-temperature fields with missing-value sentinels. The downloaded present-day station page is contextual metadata, not proof of every historical deployment position or sensor configuration.
3. **USGS station 04193500**, Maumee River at Waterville: daily service responses for parameter 00060, daily mean discharge, in cubic feet per second. Exact query URLs are in the manifest.
4. **2014 NOAA satellite/bulletin archive**: [NCEI 0242494 v1.1](https://www.ncei.noaa.gov/archive/accession/0242494), within the [2008–2016 experimental collection](https://doi.org/10.25921/q053-h813). This corrects the quoted advice that the satellite archive only reaches back to 2017.
5. **2019 NOAA satellite/bulletin archive**: [NCEI 0209038 v1.1](https://www.ncei.noaa.gov/archive/accession/0209038).
6. **Methods paper**: Boegehold et al. (2023), [Routine monitoring of western Lake Erie to track water quality changes associated with cyanobacterial harmful algal blooms](https://essd.copernicus.org/articles/15/3853/2023/). A local PDF is included. Preserve attribution when sharing; the paper identifies its CC BY 4.0 terms. Dataset use/attribution statements are retained in the archive metadata.

## What this enables

There is enough source material to build a substantial **retrospective public-record replay for 2014**, with 2019 as a second season. The next implementation can show real sample locations and concentrations, genuine satellite frames, weather, river flow, source links and visible evidence gaps.

This package has **not** connected those files to the Basin Console, decoded satellite pixels into validated concentration values, reconstructed treatment-plant measurements, or validated advisory thresholds. Those are separate implementation and scientific-review steps. See **Integration Notes.md** before enabling Scenario B.

## Checks performed

The package builder verifies every downloaded file against its recorded SHA-256, checks the expected satellite-download list, decodes every GeoTIFF, checks every generated PNG against the TIFF’s rendered RGB pixels, checks satellite PDF signatures, and reconciles prepared laboratory record counts and identifiers. It also checks the ZIP for corruption. These are acquisition and preparation checks, not scientific certification. Results are in **Documentation/Verification.json**.
