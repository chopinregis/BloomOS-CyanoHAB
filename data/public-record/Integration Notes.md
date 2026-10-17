# Integration notes for the public-record replay

## Recommended first implementation

Use 2014 as the primary historical season. Start with a late-July through August window, while keeping the full downloaded season available. Let the displayed timestamp govern which actual observations and images appear. Give every evidence item its own collection date, source file, and record reference. Keep a separate optional 2019 comparison.

The replay should be labelled **retrospective archive replay**. Sample collection timestamps do not establish when laboratory results became available to a decision-maker. Publication/receipt times are not supplied for each result. Do not imply that the reconstructed interface shows exactly what an operator knew in real time.

## Laboratory records

The prepared year-specific CSVs retain all source columns and add a stable ID, ISO date, original filename, original CSV line, and preparation flags. Original labels and values remain available. Structured observation JSON provides the principal pigment/toxin fields without forcing a common numeric interpretation.

- Units for particulate microcystin, dissolved microcystin, extracted phycocyanin and extracted chlorophyll a are micrograms per litre, as described by the source. Original field labels may contain legacy character encoding; they are retained in the complete field tables.
- A value such as `<0.1` has `value: null`, `qualifier: "<"`, and `limit: 0.1` in structured JSON. It is not zero, 0.1, or a measured value of 0.05. Any statistical substitution needs an explicit separate method.
- Empty values stay missing. Particulate and dissolved microcystin stay separate. There is no automatically calculated total or treatment-plant advisory classification.
- Different sample depths are different records. Surface and bottom results must not silently be counted as independent surface stations or collapsed into one reading.
- The 2014 subset contains unregistered site strings `1-Aug` and `2-Aug`. The 2019 table contains `2019.1` and `2019.2`. These are preserved and flagged. Their identity has not been established; do not automatically rename or place them at a known station.
- A number of sample rows, especially bottom samples in 2019, omit coordinates. A recognized station can be displayed at its **nominal master-coordinate location**, explicitly labelled as such. Keep the sample coordinate field empty. This is not a measured coordinate or a corrected original record.
- The master registry combines the two downloaded coordinate files; shared entries agree numerically. Each registry entry identifies its source file. Use the year-specific original if strict historical station membership is required.
- Preparation flags identify missing sample coordinates, unknown station identifiers, and coordinates outside a broad western-Erie review box. These checks are not a complete quality-control assessment. A flag does not automatically invalidate a measured concentration.

2014: 89 numeric particulate-microcystin entries and 37 below-limit entries. Dissolved microcystin has 49 numeric, 9 below-limit and 68 missing entries.

2019: particulate microcystin has 104 numeric, 108 below-limit and 7 missing entries. Dissolved microcystin has 68 numeric, 144 below-limit and 7 missing entries.

These lake samples do not establish finished drinking-water concentrations at Toledo, intake conditions at every location, human exposure, official advisory issuance, or the identity of an authorizing official. The demo's fictional intake and beach sites must not be passed off as these monitoring stations.

## Buoy weather

NDBC preparation preserves each source row and its original text values. The added timestamp is UTC. `WSPD` and `GST` are metres per second; `WDIR` is degrees true; `WTMP` and `ATMP` are degrees Celsius. Source definitions and other units are retained in the documentation and coverage summary.

Known field-specific sentinels become blank/null in prepared numeric columns, with the raw value beside them. Original compressed and uncompressed text is included. No interpolation, resampling, or forward fill has been performed.

The two annual files have different reporting cadences. Many 2019 rows lack water temperature or wave variables even when wind is present. Missing counts alone do not establish sensor failure: some variables may report at a different frequency. Choose the nearest appropriate observation within an explicitly displayed tolerance, or report unavailable. One offshore buoy is not a validated basin-wide or intake-specific wind field.

## River flow

The USGS CSVs retain the service's timestamp, daily date, discharge in ft³/s, and qualifiers. They contain one daily-mean record per day for each selected calendar year. Keep daily means separate from instantaneous flow. Do not turn discharge into nutrient loading without corresponding concentration data and a documented calculation.

## Satellite products

All 193 downloaded TIFFs decode successfully. The catalogue records date inferred from the filename, platform, original URL, dimensions, pixel scale, tiepoint, GeoKey directory, projection parameters where present, description, and checksum.

The original GeoTIFFs retain projection information and source pixel codes. The PNGs are **display previews only**, preserving the embedded palette without adding a legend or changing rendered colours. They do not retain georeferencing.

Before overlaying a TIFF on a geographic map, interpret its CRS and transform it correctly. The archives include different grid definitions and sensor/product versions. Do not stretch the full raster over the demo's procedural lake geometry or assume all products share one extent. Do not interpret an 8-bit palette code as CI or cells/mL without the applicable decoding rules. The included filename README is not a complete quantitative encoding specification.

Archive filenames can encode several overflight times in GMT and edited/merged products. The catalogue's primary date is a browsing key, not proof of a single instantaneous acquisition. Multiple sensor/processing variants on a date must stay identifiable. A complete archive folder is not complete cloud-free lake coverage. Retain cloud, land and unavailable pixels separately once their codes are established.

The 2014 archive begins its actual downloaded imagery on 21 July, although the bulletin season begins earlier. The 2019 imagery begins 31 May. Do not manufacture earlier frames. The newly described harmonized 25-year series is a different acquisition target and is not included as that series here.

Satellite CI/pigment products and laboratory microcystin are different evidence types. Never derive a “satellite image” or toxin concentration from the other. If a spatial interpolation is later built from station data, label the measured variable, inference method, spatial support, uncertainty and time window. Do not treat interpolation as validated toxin coverage.

## Governance and presentation

Source data can replace synthetic chart values without validating the current decision index, confidence scores, reopening rules or advisory logic. Policy profiles need their own authoritative, dated source and applicability review. A retrospective policy simulation should be shown separately from archived NOAA forecasts and actual historical public-health actions.

Keep source observations, archived analyst forecasts, newly computed estimates and human actions distinct. A downloaded NOAA bulletin is a historical NOAA product; the BloomOS interface and its conclusions are not NOAA-endorsed. No messages have been sent to NOAA or Richard Stumpf as part of this work.

Before a public presentation, complete the raster decoding/reprojection, resolve or exclude unknown site identities from site-specific gates, establish sample result availability assumptions, and enforce evidence/authority prerequisites in the state transition logic. This package supplies real evidence; those remaining steps make its use defensible.
