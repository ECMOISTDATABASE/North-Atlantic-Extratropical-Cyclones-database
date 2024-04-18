# North Atlantic Extratropical Cyclone Tracks and Lagrangian-Derived Moisture Uptake Dataset
## Environmental Physics Laboratory (EPhysLab)
Centro de Investigación Mariña, Universidade de Vigo, Campus As Lagoas s/n, 32004 Ourense, Spain

Contact: patricia.coll@uvigo.gal

## What is this?
Extratropical cyclones (ECs) play an important role in the generation of precipitation at mid-latitudes. This dataset contains positional and meteorological data, two-dimensional masks and a variable for moisture uptake associated with precipitation from ECs in the North Atlantic during extended winters from 1985 to 2022.

![Figure 1:](https://github.com/ECMOISTDATABASE/North-Atlantic-Extratropical-Cyclones-database/blob/main/sat_2002.png) 

As of the last update date of the repository, it contains information on the tracks of 11,177 cases. Information about masks and descriptive variables of moisture uptake measurements is available for 237 ECs cases. The most intense ones identified over the Atlantic, which information is documented in the database, are stored in the file <EC_NATL_int_1985_2022.dat>.

## EC_NATL_int_1985_2022.dat description:

**Example:**<br>
**LINE #1:** WNATL0091985, <br>
**LINE #2:** 19850106, 00,45.37,-59.57,958.182,994.151,1002.68,<br>

For each case, there are two corresponding lines, as illustrated by the example lines. The first line follows the format:<br>
 **AREAidxyear,**<br>
 where **AREA** represents the subregion in the North Atlantic where the cyclone reached maximum intensity (Possibilities: 'ENATL' for Eastern North Atlantic, 'NATL' for Northern North Atlantic, 'WANTED' for Western North Atlantic), **idx** is a three-position indicator unique to each case per year, corresponding to the sequence of cyclone formation, and **year** is the year of cyclone detection.<br>
The second line contains the following columns of information: <br>
**date** in yyyymmdd format, <br>
 **hour** in UTC, <br>
  **latitude** in degrees North,  <br>
 **longitude** in degrees West-East,  <br>
 **minimum sea level pressure** at the cyclone's center in hPa,  <br>
 cyclone **radius** in km, and  <br>
 pressure at the **last closed isobar** in hPa. <br>

## DATASET description:
The dataset is organized within the parent folder **'EC'**, which contains subfolders for each year from 1985 to 2022. Within each year folder, there are subfolders named according to the following pattern: **mm_seasoninfo** (mm=month). The season information indicates whether the month corresponds to the winter season of the year folder or a previous year, providing a benchmark for code interpretation.<br>
Inside the month folder, you'll find subfolders named according to an index corresponding to each EC case in the year. The order is determined by the chronological formation of the ECs, with each index represented by a three-digit number.<br>


Case folder description:

Within each EC folder, you'll find files containing the following information:

- Track data
- Mask data
- Moisture uptake variables (if listed in EC_NATL_int_1985_2022.dat)

### Track data file <track_idx.dat>
This .dat file contains a header in type:
**NATL0091985,**
as described in LINE #1 of [EC_NATL_int_1985_2022.dat](https://github.com/ECMOISTDATABASE/North-Atlantic-Extratropical-Cyclones-database?tab=readme-ov-file#ec_natl_int_1985_2022dat-description)  
the number of line correspond to the EC lifetime in 6hours time steps. Are coding as follows:<br>
19850105, 18,43.96,-62.53,967.133,996.137,1041.71,

## Metadata:
Models used:
- The regional high-resolution model Weather Research and Forecasting ([WRF](https://www2.mmm.ucar.edu/wrf/users/download/get_source.html)) (Skamarock et al., 2008) 
    - WRF was fitted with [ERA5](https://cds.climate.copernicus.eu/cdsapp#!/search?type=dataset) reanalysis from the ECMWF (Hersbach et al., 2020) 
- The Lagrangian FLEXible PARTicle dispersion model ([FLEXPART-WRF](https://www.flexpart.eu/wiki/FpRoadmap)) (Brioude et al., 2013) 

Softwares used:
- EuLerian Identification of ascending AirStreams (Quinting & Grams,2022) [ELIAS 2.0](https://doi.org/10.5281/zenodo.5154980) 
- TRansport Of water VApor (Frenández-Alvarez et al., 2022) [TROVA](https://github.com/tramo-ephyslab/TROVA-master.git)

## Dataset description:
- Track info:
    - Dimensions
    - file extension .dat
    - The number of rows (observations) and columns (variables/features).
    - Variables/Features: List and describe each variable or feature present in the dataset. Include information such as the variable name, data type, description, and any units of measurement. For categorical variables, specify the categories or levels.
    - Data Types: Specify the data types of each variable (e.g., numerical, categorical, ordinal, datetime).
- Target Regions info:
    - file extension: .nc
    - file content:
        -(1) a symmetric geometry around the centre of the EC (bounded by the outer radius of the system)  
        -(2) the footprints of the associated WCB inflow, ascent, and outflow stages
        -(3) a square root spiral system's centred and adjusted for MSLP drop
- Moisture Uptake:
    - file extension: .nc
    - file content:

## Example Records:
