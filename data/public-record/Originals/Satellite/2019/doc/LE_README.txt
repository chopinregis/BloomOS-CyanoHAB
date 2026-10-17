NOAA Lake Erie Harmful Algal Bloom Data Naming Conventions
------------------------------------------
The file naming conventions are herein described. For information about the Lake Erie Harmful Algal Bloom (HAB) Operational Forecast System, visit https://tidesandcurrents.noaa.gov/hab/lakeerie.

After one year, data is archived at https://data.nodc.noaa.gov/cgi-bin/iso?id=gov.noaa.nodc:NOS-HABOFS-LakeErie.
------------------------------------------
bulletin_current.jpg
------------------------------------------
An image of the most recent Lake Erie HAB bulletin. The bulletin pdf is also posted to the following urls: https://tidesandcurrents.noaa.gov/hab/lakeerie_bulletins/bulletin_current.pdf and https://tidesandcurrents.noaa.gov/hab/lakeerie.
------------------------------------------
MODIS Aqua Files
------------------------------------------
aqua.YYYYDDD.MMDD.HHMM_HHMMC.L3.GL1.v8103_1_1.CI_merge_Kdcorr-E-B.tif
e.g. aqua.2017201.0720.1749_1750_1928_1930C.L3.GL1.v8103_1_1.CI_merge_Kdcorr-E-B.tif

aqua=Name of the satellite carrying the Moderate-resolution Imaging Spectroradiometer (MODIS) instrument
YYYYDDD = Year and julian day of image
MMDD = calendar month and day of image
HHMM = sensor overflight time of image (in GMT, may be multiple times for composite images)
HHMMC = final overflight time for composite image (in GMT)
L3 = processing level of image
GL1 = region of image (Great Lakes)
v8103_1_1 = processing algorithm applied to image
product type = chlorophyll index imagery product (CI_merge_Kdcorr)
E = manually edited by NOAA Lake Erie HAB analysts to remove artifacts from land or clouds
B = included in the NOAA Lake Erie HAB bulletin; files that do not end in "B" were not used on the bulletin
------------------------------------------
MODIS Terra Files
------------------------------------------
terra.YYYYDDD.MMDD.HHMM_HHMMC.L3.GL1.v8103_1_1.CI_merge_Kdcorr-E-B.tif
e.g. terra.2017201.0720.1749_1750_1928_1930C.L3.GL1.v8103_1_1.CI_merge_Kdcorr-E-B.tif

terra=Name of the satellite carrying the MODIS instrument
YYYYDDD = Year and julian day of image
MMDD = calendar month and day of image
HHMM = sensor overflight time of image (in GMT, may be multiple times for composite images)
HHMMC = final overflight time for composite image (in GMT)
L3 = processing level of image
GL1 = region of image (Great Lakes)
v8103_1_1 = processing algorithm applied to image
product type = chlorophyll index imagery product (CI_merge_Kdcorr)
E = manually edited by NOAA Lake Erie HAB analysts to remove artifacts from land or clouds
B = included in the NOAA Lake Erie HAB bulletin; files that do not end in "B" were not used on the bulletin
------------------------------------------
Merged MODIS Terra and Aqua Files
------------------------------------------
When imagery from the MODIS instrument aboard either the Terra or Aqua satellite is partially obscured by clouds, analysts may merge parts of cloud-free imagery from one satellite to fill in the gaps of missing imagery in the other. In this event, the files have an extended naming convention to indicate which satellite’s image was used as the base layer and which satellite was used as the supplemental imagery.

aqua.YYYYDDD.MMDD.HHMM_HHMMC.L3.GL1.v8103_1_1.merge.terra.YYYYDDD.MMDD.HHMM_HHMMC.L3.GL1.v8103_1_1.CI_merge_Kdcorr-E-B.tif
e.g. aqua.2017200.0719.1707_1844_1845C.L3.GL1.v8103_1_1.merge.terra.2017200.0719.1524_1525_1702_1705C.CI_merge_Kdcorr-E-B.tif

aqua/terra = The name of the satellite used for the primary image appears first in the file name. The satellite used to fill in gaps in the primary imagery is displayed second.
YYYYDDD = Year and julian day of image
MMDD = calendar month and day of image
HHMM = sensor overflight time of image (in GMT, may be multiple times for composite images)
HHMMC = final overflight time for composite image (in GMT)
L3 = processing level of image
GL1 = region of image (Great Lakes)
v8103_1_1 = processing algorithm applied to image
product type = chlorophyll index imagery product (CI_merge_Kdcorr)
E = manually edited by NOAA Lake Erie HAB analysts to remove artifacts from land or clouds
B = included in the NOAA Lake Erie HAB bulletin; files that do not end in "B" were not used on the bulletin
------------------------------------------
Sentinel-3 Files
------------------------------------------
sentinel-3a.YYYYDDD.MMDD.HHMMC.L3.LE3.v8103_1_1.CI_PIsrCorr-E-B.tif
e.g. sentinel-3a.2017197.0716.1522C.L3.LE3.v8103_1_1.CI_PIsrCorr-E-B.tif

sentinel-3a=Name of the satellite carrying the Ocean Land Colour Instrument (OLCI) 
YYYYDDD = Year and julian day of image
MMDD = calendar month and day of image
HHMM = sensor overflight time of image (in GMT, may be multiple times)
HHMMC = final overflight time for composite image (in GMT)
L3 = processing level of image
LE3 = region of image (Lake Erie)
v8103_1_1 = processing algorithm applied to image
CI_PIsrCorr-E = chlorophyll index imagery product
E = manually edited by NOAA Lake Erie HAB analysts to remove artifacts from land or clouds
B = included in the NOAA Lake Erie HAB bulletin; files that do not end in "B" were not used on the bulletin
------------------------------------------
LE_IntakesBulletinImagery.zip
------------------------------------------
A compressed file containing the most recent edited image with an interactive layer displaying the location of Lake Erie water intakes. When relevant, the transport nowcast and forecast images are also included for each 24-hour period from the date of the edited image to 72 hours into the future from the date of the model run. The "-Sentinel" suffix indicates this is the most recent image from the Sentinel 3a satellite. If no suffix exists, the most recent image is from the MODIS instrument aboard either the Terra or Aqua satellite.

To measure the coordinates and distances between features in the imagery and geographic locations marked on the map follow the instructions for viewing Geospatial PDFs: https://tidesandcurrents.noaa.gov/hab/hab_publication/HAB-OFS-GeoPDFInstructions.pdf.

The filenames of the images within the zipfile use the following naming convention:
GL1.CI.YYYYMMDDHH.h####.pdf
e.g. GL1.CI.2017072116.h0048.pdf

GL1=Region of PDF (Lake Erie) 
CI = The imagery product featured in the PDF (chlorophyll index)
YYYMMDDHH = calendar year, month, day and hour of the original image used for the transport 
h#### = The number of hours transport was modeled from the initial image (24 hour increments, 0-144 hours)
------------------------------------------
LE_BulletinImagery.zip
------------------------------------------
A compressed file containing the most recent edited image. When relevant, the transport nowcast and forecast images are also included for each 24-hour period from the date of the edited image to 72 hours into the future from the date of the model run. The "-Sentinel" suffix indicates this is the most recent image from the Sentinel 3a satellite. If no suffix exists, the most recent image is from the MODIS instrument aboard either the Terra or Aqua satellite.

The filenames of the images within the zipfile use the following naming convention:
GL1.CI.YYYYMMDD16.h####.png
e.g. GL1.CI.2017072116.h0048.png

GL1=Region of png (Lake Erie) 
CI = The imagery product featured in the png (chlorophyll index)
YYYMMDDHH = calendar year, month, day and hour of the original image used for the transport 
h#### = The number of hours transport was modeled from the initial image (24 hour increments, 0-144 hours)
------------------------------------------


Date last modified: 25-Jun-2018