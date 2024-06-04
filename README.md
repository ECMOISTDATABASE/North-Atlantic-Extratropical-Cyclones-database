# North Atlantic Extratropical Cyclone Tracks and Lagrangian-Derived Moisture Uptake Dataset
## Environmental Physics Laboratory (EPhysLab)
Centro de Investigación Mariña, Universidade de Vigo, Campus As Lagoas s/n, 32004 Ourense, Spain

Contact: patricia.coll@uvigo.gal

## What is this?
Extratropical cyclones (ECs) play an important role in the generation of precipitation at mid-latitudes. This dataset contains positional and meteorological data, two-dimensional masks and a variable for moisture uptake associated with precipitation from ECs in the North Atlantic during extended winters from 1985 to 2022.

<!-- ![Figure 1:](https://github.com/ECMOISTDATABASE/North-Atlantic-Extratropical-Cyclones-database/blob/main/sat_2002.png)  -->

As of the last update date of the repository, it contains information on the tracks of 11,177 cases. Information about masks and descriptive variables of moisture uptake measurements is available for 237 ECs cases. The most intense ones identified over the Atlantic, which information is documented in the database, are stored in the file <EC_NATL_int_1985_2022.dat>.

### EC_NATL_int_1985_2022.dat description:

**Example:**<br>
**LINE #1:** WNATL0091985, <br>
**LINE #2:** 19850106, 00,45.37,-59.57,958.182,994.151,1002.68,<br>

There are two corresponding lines for each case, as illustrated by the example lines. The first line follows the format:<br>
 **AREAidxyear,**<br>
 where **AREA** represents the subregion in the North Atlantic where the cyclone reached maximum intensity (Possibilities: 'ENATL' for Eastern North Atlantic, 'NATL' for Northern North Atlantic, 'WNATL' for Western North Atlantic), **idx** is a three-position indicator unique to each case per year, corresponding to the sequence of cyclone formation, and **year** is the year of cyclone detection.<br>
The second line contains the following columns of information: <br>
**date** in yyyymmdd format, <br>
**hour** in UTC, <br>
**latitude** in degrees North,  <br>
**longitude** in degrees West-East,  <br>
**minimum sea level pressure** at the cyclone's center in hPa,  <br>
 cyclone **radius** in km, and  <br>
 pressure at the **last closed isobar** in hPa. <br>

All '.dat' separators are defined with commas.

The function **read_track_data** in [script example_case.py](https://github.com/ECMOISTDATABASE/North-Atlantic-Extratropical-Cyclones-database/blob/main/Example_case_029_2002/example_case.py) allows for reading the **EC_NATL_int_1985_2022.dat** file too. Could you correctly adjust the index on line 181 to select the **AREA** name?


## DATASET description:
The data set is organized within the repositories:

1985-2000:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.11454946.svg)](https://doi.org/10.5281/zenodo.11454946)

2001-2016: 

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.11476835.svg)](https://doi.org/10.5281/zenodo.11476835)

2017-2022: 

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.11476925.svg)](https://doi.org/10.5281/zenodo.11476925)


In the repositories, compressed files corresponding to the years between 1985 and 2022 have been distributed (given the database size). Until the publication of these data, access depends on the authorization of the authors.

Within each year folder, subfolders are named according to the following pattern: **mm_seasoninfo** (mm=month). The season information indicates whether the month corresponds to the winter season of the year folder or a previous year, providing a benchmark for code interpretation.<br>
Inside the month folder, you'll find subfolders named according to an index corresponding to each EC case in the year. The order is determined by the chronological formation of the ECs, with each index represented by a three-digit number.<br>


Case folder description:

Within each EC folder, you'll find files containing the following information:

- Track data
- Mask data
- Moisture uptake variables (if listed in EC_NATL_int_1985_2022.dat)

### Track data file <track_idx.dat>
The '.dat' file contains a header in the following format:

**NATL0091985,**

 where "NATL" is standard for all cases, indicating the North Atlantic basin as described in LINE #1 of [EC_NATL_int_1985_2022.dat](https://github.com/ECMOISTDATABASE/North-Atlantic-Extratropical-Cyclones-database?tab=readme-ov-file#ec_natl_int_1985_2022dat-description) 
The number of lines corresponds to the EC lifetime in 6-hour time steps. They are coded as follows:


**19850105, 18, 43.96, -62.53, 967.133, 996.137, 1041.71,**


The rows correspond with the following:
- yyyymmdd: Date in year-month-day format
- hh (in UTC): Hour in Coordinated Universal Time
- latitude (degrees North): Latitude in degrees North
- longitude (degrees West): Longitude in degrees West
- MSLP (hPa): Mean Sea Level Pressure in hectopascals (hPa)
- Radius (km): Cyclone radius in kilometres (km)
- last closed isobar (hPa): Pressure at the last closed isobar in hectopascals (hPa)

### Mask data file <typemask_idx.nc>

The typemask attribute could take the following names: "radius," "spiral," or "wcb," corresponding to the decided shapes for representing the cyclone in the meteorological data.

The figure illustrates two key elements:

In (a), the mask 'radius' is depicted with contoured dashed blue lines. To represent the occurrence probabilities of warm conveyor belts (WCBs), solid red lines indicate inflow, blue lines denote ascent, and green lines signify outflow. These lines are compounded by the lowest probability regions, shaping the 'WCB' target area. The background presents a the Geostationary IR Channel Brightness Temperature (BT)- GridSat-B1 Climate Data Record (CDR). In yellow marker EC centre surface position.

In (b), precipitation from WRF outputs serves as the background, while the 'spiral' shape is delineated with contoured lines.

![Figure 1:](https://github.com/ECMOISTDATABASE/North-Atlantic-Extratropical-Cyclones-database/blob/main/case_0292002_mask_example.png)

File Format: NetCDF (Network Common Data Form).

Data Structure:

Dimensions:

    longitude: 799
    latitude: 479

Variables:
```
  name: yyyymmddhh (e.g "1985010518")
  long_name: yyyymmddhh
  type: float
  shape: (latitude, longitude) 
  Mask values: 0 and 1

  name: XLAT
  long_name: latitude
  type: float
  shape: (lat) 
  units: "degrees"

  name: XLONG
  long_name: longitud
  type: float
  shape: (lon) 
  units: "degrees"

```

Attributes:

    Global attributes:
        history: "EC NATL database/Target region: **typemask**/Case: **idx_yyyy**/EPhysLab/Contact: patricia.coll@uvigo.gal"

### Moisture Uptake Variables <typemask.zip>
The '.zip' archive contains the resultant moisture uptake files for each type of mask. Consequently, you will find three '.zip' files. It's important to note that different particles were considered in the water budget analysis for each mask. So, pay close attention to the correspondence between the desired results and mask selection.

Each NetCDF file within the '.zip' correspond to the output from a mask variable, contained in the ['typemask_idx.nc'](https://github.com/ECMOISTDATABASE/North-Atlantic-Extratropical-Cyclones-database?tab=readme-ov-file#mask-data-file-typemask_idxnc). They are named according the date of the cyclone position analysis format yyyymmddhh plus .nc extension. 

Data Structure:

Dimensions:

```
    lat = 325 ;
    lon = 600 ;
    time = 10 ;
    layers = 10 ;
```

Variables:
```
  name: lat
  long_name: latitude
  type: double
  shape: (lat) 
  units: "degrees"

  name: lon
  long_name: longitud
  type: double
  shape: (lon) 
  units: "degrees"

  name: time
  long_name: time
  type: double
  shape: (time) 
  units: "days since 1900-01-01"

  name: E_P
  long_name: E_P
  type: double
  shape: (time, lat, lon) 
  units: "mm/day"

  name: E_P_integrated
  long_name: E_P integrated for ndays considered
  type: double
  shape: (lat, lon) 
  units: "mm/day"

  name: POR
  long_name: Sources Contribution for each parcel
  type: double
  shape: (time, lat, lo) 
  units: "%"

  name: E_P_layers
  long_name: E_P_layers
  type: double
  shape: (time, layers, lat, lon) 
  units: "mm/day"

  name: E_P_integrated_layers
  long_name: E_P_layers
  type: double
  shape: (layers, lat, lon) 
  units: "mm/day"

  name: vertical_layers
  long_name: vertical layers
  type: string
  shape: (layers) 
```


Attributes:
```
    Global attributes:
        history: "EC NATL database/Target region: **typemask**/Case: **idx_yyyy**/EPhysLab/Contact: patricia.coll@uvigo.gal/FROM TROVA SOFTWARE"
```


## Metadata:
Models used:
- The regional high-resolution model Weather Research and Forecasting ([WRF](https://www2.mmm.ucar.edu/wrf/users/download/get_source.html)) (Skamarock et al., 2008) 
    - WRF was fitted with [ERA5](https://cds.climate.copernicus.eu/cdsapp#!/search?type=dataset) reanalysis from the ECMWF (Hersbach et al., 2020) 
- The Lagrangian FLEXible PARTicle dispersion model ([FLEXPART-WRF](https://www.flexpart.eu/wiki/FpRoadmap)) (Brioude et al., 2013) 

Softwares used:
- EuLerian Identification of ascending AirStreams (Quinting & Grams,2022) [ELIAS 2.0](https://doi.org/10.5281/zenodo.5154980) 
- TRansport Of water VApor (Frenández-Alvarez et al., 2022) [TROVA](https://github.com/tramo-ephyslab/TROVA-master.git)

## Example Records:
In the [Example_case_029_2002](https://github.com/ECMOISTDATABASE/North-Atlantic-Extratropical-Cyclones-database/tree/main/Example_case_029_2002) directory, you'll find instructions for reproducing the next figure. Feel free to refer to the **'readme.md'** file for guidance and customize the script according to your requirements. Please note that the [script example_case.py](https://github.com/ECMOISTDATABASE/North-Atlantic-Extratropical-Cyclones-database/blob/main/Example_case_029_2002/example_case.py) includes functions to read information from the track '.dat' files and mask '.nc' file.

![Figure 2:](https://github.com/ECMOISTDATABASE/North-Atlantic-Extratropical-Cyclones-database/blob/main/Example_case_029_2002/Moisture_Up_Cross_Section_029_2002.png)

The filtered landfalling cases over the Iberian Peninsula are stored in the file **EC_IP_int_1985_2022.dat** on the dataset. You can read this file using the **read_track_data** function in the [script example_case.py](https://github.com/ECMOISTDATABASE/North-Atlantic-Extratropical-Cyclones-database/blob/main/Example_case_029_2002/example_case.py).
