# North Atlantic Extratropical Cyclone Tracks and Lagrangian-Derived Moisture Uptake Dataset
## Environmental Physics Laboratory (EPhysLab)
Centro de Investigación Mariña, Universidade de Vigo, Campus As Lagoas s/n, 32004 Ourense, Spain

Contact: patricia.coll@uvigo.gal

## What is this?
Extratropical cyclones (ECs) play an important role in the generation of precipitation at mid-latitudes. This dataset contains positional and meteorological data, as well as two-dimensional masks and a variable for moisture uptake associated with precipitation from ECs in the North Atlantic during extended winters from 1985 to 2022.

## Data and models
Models used:
- The regional high-resolution model Weather Research and Forecasting ([WRF](https://www2.mmm.ucar.edu/wrf/users/download/get_source.html)) (Skamarock et al., 2008) 
    - WRF was fitted with [ERA5](https://cds.climate.copernicus.eu/cdsapp#!/search?type=dataset) reanalysis from the ECMWF (Hersbach et al., 2020) 
- The Lagrangian FLEXible PARTicle dispersion model ([FLEXPART-WRF](https://www.flexpart.eu/wiki/FpRoadmap)) (Brioude et al., 2013) 

Softwares used:
- EuLerian Identification of ascending AirStreams (Quinting & Grams,2022) [ELIAS 2.0](https://doi.org/10.5281/zenodo.5154980) 
- TRansport Of water VApor (Frenández-Alvarez et al., 2022) [TROVA](https://github.com/tramo-ephyslab/TROVA-master.git)

## Dataset elements:
- Track info:
    - file extension .dat
    - file content:
- Target Regions info:
    - file extension: .nc
    - file content:
- Moisture Uptake:
    - file extension: .nc
    - file content:
For selecting the target regions where precipitation associated with ECs occur, we consider three different spatial patterns. Thus, we select (1) a symmetric geometry around the centre of the EC (bounded by the outer radius of the system), (2) the footprints of the associated WCB inflow, ascent, and outflow stages, and (3) a square root spiral system's centred and adjusted for MSLP drop. 