# Author: Patricia Coll-Hidalgo
# Contact: patricia.coll@uvigo.gal

# Importing necessary libraries
import numpy as np  # NumPy for numerical operations
from numpy import dtype #for data manipulation purposes

import matplotlib  # Matplotlib for plotting
import matplotlib.pylab as plt #provide a MATLAB-like interface for plotting
from matplotlib.colors import ListedColormap, BoundaryNorm # Matplotlib for custom color maps and norms
import cartopy.crs as ccrs  # Cartopy for cartographic projections
import cartopy.feature as cfeature # Cartopy for adding geographic features
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter # Cartopy for formatting tick labels

import sys  # System-specific parameters and functions
import os # Operating system dependent functionality

from netCDF4 import Dataset # NetCDF4 for handling NetCDF files
import xarray as xr # Xarray for multi-dimensional arrays

import datetime  # Date and time functionality
import time # Time access and conversions

import zipfile # Import the 'zipfile' module to work with zip files

import metpy # Import the MetPy library for meteorological calculations and plotting
import metpy.calc as mpcalc # Import the module for performing meteorological calculations
from metpy.units import units # Import the units module from MetPy for handling unit conversions
from metpy.interpolate import cross_section

# Set the desired fontsize
fontsize = 35

# Update the rcParams dictionary
matplotlib.rcParams.update({'font.size': fontsize,
                     'axes.labelsize': fontsize,
                     'axes.titlesize': fontsize,
                     'xtick.labelsize': fontsize,
                     'ytick.labelsize': fontsize,
                     'legend.fontsize': fontsize})

#Define functions 

def create_map(ax=None, projection=ccrs.PlateCarree(), figsize=(18, 12), extent=[-100, 10, 10,45], gridlines=True, lon_fontsize=35, lat_fontsize=35, resolution='50m'):
	"""
	Create a map with specified parameters.

	Args:
	- ax (cartopy.mpl.geoaxes.GeoAxesSubplot, optional): Axis to plot the map on. If None, a new figure and axis are created.
	- projection (cartopy.crs.Projection, optional): Map projection.
	- figsize (tuple, optional): Figure size.
	- extent (list, optional): Extent of the map in the form [lon_min, lon_max, lat_min, lat_max].
	- gridlines (bool, optional): Whether to draw gridlines on the map.
	- lon_fontsize (int, optional): Font size for longitude labels.
	- lat_fontsize (int, optional): Font size for latitude labels.
	- resolution (str, optional): Resolution of coastline and border data (e.g., '50m', '110m', '10m').

	Returns:
	- cartopy.mpl.geoaxes.GeoAxesSubplot: Axis with the created map.
	"""
	# Create a figure and axis if not provided
	if ax is None:
		fig, ax = plt.subplots(figsize=figsize, subplot_kw={'projection': projection})
   
	# Add background features
	ax.add_feature(cfeature.LAND, color='lightgray')
	ax.add_feature(cfeature.COASTLINE)
	ax.add_feature(cfeature.BORDERS, linestyle=':')
	ax.add_feature(cfeature.RIVERS)
    
	# Add gridlines if specified
	if gridlines:
		gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=1, color='gray', alpha=0.5, linestyle='--')
		gl.xlabels_top = False
		gl.ylabels_right = False
		gl.xformatter = LongitudeFormatter()
		gl.yformatter = LatitudeFormatter()
        
		# Set fontsize for labels
		gl.xlabel_style = {'size': lon_fontsize}
		gl.ylabel_style = {'size': lat_fontsize}
    
	# Set the extent of the map
	ax.set_extent(extent)
 
	# Return the axis       
	if ax is None:
		return fig, ax
	else:
		return ax

def create_custom_colormap():
	"""
	Create a custom colormap from specified levels and colors.

	Args:
	- levels (array_like): Array of levels.
	- colors (list): List of colors in hexadecimal format.

	Returns:
	- matplotlib.colors.ListedColormap: Custom colormap.
	- matplotlib.colors.Normalize: Normalization for the colormap.
	"""
	
	# Define the number of colors in the palette
	levels = np.arange(0, 30, 0.5)
	
	# Create a range of colors from white to a fully saturated color
	colors = ["#ffffff", "#e1f3e1", "#cde9cd", '#b5deb4', '#87c686', '#72b671', '#60a95f', '#519b50', '#318230', '#237222', '#1a6419', '#267325', "#347c33", '#498949', '#649663', '#739872', '#839c83', '#8fa08f', '#8fa08f', '#8fa09f', '#6e8b91', '#6e8b91', '#6e8b91', '#658b91', '#5d8b91', '#548b91', '#488b91', '#488ba5', '#488ba8', '#488bb1', '#488bbc', "#4885bc", "#4882bc", "#4880bc", '#4876bc', '#486bbc', '#485fbc', '#485cbc', '#4857bc', '#484fbc', '#3b42b3', '#3138ac', '#242ca5', '#161e9b', '#0b1393', '#040c88', '#040c90', "#030a7f", "#040c88", "#040c83", "#040c79", "#040c74", "#040c7e", "#040c7b", "#040c76", "#040c76", "#040c71", "#040c71", "#040c6c", '#040c69']
    
	# Create colormap from levels and colors
	cmap, norm = matplotlib.colors.from_levels_and_colors(levels, colors, extend="max")
	return cmap, norm

def array_for_transversal(input_file, output_file, variable_name):

	# Open the input NetCDF file
	data = xr.open_dataset(input_file)

	# Select "E_P_integrated_layers" 
	variable_data = data[variable_name]

	# Create a new dataset with only the selected variable
	new_data = xr.Dataset({variable_name: variable_data})

	# Copy coordinates and attributes from the original dataset
	for coord in data.coords:
	    new_data[coord] = data[coord]

	# Save the new dataset to a new NetCDF file
	new_data.to_netcdf(output_file)

	# Close the input dataset
	data.close()

	print("Variable '{}' saved to '{}' along with coordinates and attributes.".format(variable_name, output_file))


	return
	
def list_files(root_ad):
	"""
	List files in a directory and return them sorted.

	Args:
	- root_ad (str): Root directory path.

	Returns:
	- list: List of files in the directory sorted alphabetically.

	"""
	# List files in the specified directory
	examples=os.listdir(root_ad)
	# Sort the list of files alphabetically	
	examples=sorted(examples)
	# Return the sorted list of files	
	return examples
	
def unzip(zip_file, extract_to="."):
	"""
	Unzip a zip file to a specified directory.

	Args:
	- zip_file (str): Path to the zip file to unzip.
	- extract_to (str, optional): Directory to extract the zip file to. Default is the current directory.

	Returns:
	- None
	"""
	with zipfile.ZipFile(zip_file, 'r') as zip_ref:
		zip_ref.extractall(extract_to)
def read_track_data():
	# Define the track file name
	track_file_name="./track_029.dat"
	
	# Open the track file for reading		
	input_files=open(track_file_name)
	tracks=input_files.readlines()
	
	# Extract AREA, EC_id, and YEAR from the first line of the track file
	AREA=tracks[0][0:4]
	EC_id=tracks[0][4:7]
	YEAR=tracks[0][7:11]
	
	# Initialize an empty array to store case data
	case_data=np.empty((len(tracks)-1,6))
	
	# Initialize empty lists for storing individual data fields
	date=[]
	latitudes=[]
	longitudes=[]
	MSLP=[]
	Radius=[]
	LCI=[] #last closed isobar
	
	
	# Iterate over each line in the track file
	index=1
	while index < len(tracks):
		array=tracks[index].split(",")

		date=np.append(date,array[0]+array[1].split(" ")[-1])
		latitudes=np.append(latitudes,array[2])
		longitudes=np.append(longitudes,array[3])
		MSLP=np.append(MSLP,array[4])
		LCI=np.append(LCI,array[5])
		Radius=np.append(Radius,array[6])
		

		index=index+1
	
	# Store the data from lists into the case_data array
	case_data[:,0]=date[:]
	case_data[:,1]=latitudes[:]
	case_data[:,2]=longitudes[:]
	case_data[:,3]=MSLP[:]
	case_data[:,4]=Radius[:]
	case_data[:,5]=LCI[:]	
		
	return case_data
	
def read_mask_shape():
	# Open the NETCDF file 
	mask_file_name="./radius_029.nc"
	
	Sfile=Dataset(mask_file_name,'r')
	
	# Extract latitude, longitude, and mask data
	latitud=Sfile.variables["XLAT"][:]	
	longitud=Sfile.variables["XLONG"][:]	
	mask=Sfile.variables["2002020812"][:] # 1 for points of mask
	
	# Close the NETCDF file	
	Sfile.close()	
	return mask


# Main code
if __name__ == "__main__":
	# Unzip from the Dataset:
	zip_file = "/mnt/lustre/hsm/nlsas/notape/home/uvi/fi/tramo/patricia/PAPER_II/REPO/EC/2002/02_prev_winter/029/radius.zip" 
	extract_to = "./case_0292002/"

	unzip(zip_file, extract_to)
	
	#List files in extracted folder
	case_steps=list_files(extract_to)
		
	# Read NETCDF of genesis 
	# Open the NETCDF file for the first step in the case
	Sfile=Dataset(extract_to+case_steps[0],'r')
	
	# Extract latitude, longitude, and integrated moisture uptake data
	latitud=Sfile.variables["lat"][:]	
	longitud=Sfile.variables["lon"][:]	
	E_P=Sfile.variables["E_P_integrated"][:]
	E_P_l=Sfile.variables["E_P_integrated_layers"][:]
	
	# Close the NETCDF file	
	Sfile.close()	
	
	# Create a file with the variable for cross section
	array_for_transversal(extract_to+case_steps[0], "./cross_file.nc", "E_P_integrated_layers")

	# Open the NetCDF file containing the cross-sectional data	
	data_cut = xr.open_dataset("./cross_file.nc")
	
	# Parse the coordinates and units using MetPy
	data_cut = data_cut.metpy.parse_cf().squeeze()

	# Create 2D meshgrid of longitude and latitude		
	lon2d,lat2d=np.meshgrid(longitud, latitud)		
	
	#Define line for transversal section
	lat_right, lon_right = 30., -66. # Latitude and longitude for the right end of the line
	lat_left, lon_left = 39.5, -75.3 # Latitude and longitude for the left end of the line
	
	start = (lat_right, lon_right)
	end = (lat_left, lon_left)

	# Generate a cross-sectional slice from the data	
	cross = cross_section(data_cut, start, end).set_coords(('lat', 'lon'))
	
	# Extract the integrated moisture uptake data along the cross section
	rh_cross = cross["E_P_integrated_layers"][:]
	
	# Define levels for contour plot
	levels=np.arange(0,30,0.5)
	
	# Create custom colormap and normalization
	cmap,norm=create_custom_colormap()
	
	# Create a figure
	fig=plt.figure(figsize=(18,12))
	
	# Create a map
	mapa=create_map()	
	
	# Plot filled contour
	cn=mapa.contourf(lon2d, lat2d, E_P, levels, cmap=cmap)
	
	# Plot transversal line
	plt.plot([lon_right, lon_left], [lat_right, lat_left], marker='o', color='r', linewidth=2.5)
	
	# Add colorbar
	cb=plt.colorbar(cn,orientation="horizontal", aspect=25,pad=0.05,shrink=0.9, extend="both")
	cb.ax.tick_params(labelsize=35) 
	cb.set_label(label="Moisture Uptake  (" + 'mm/day'+")", size=35,labelpad=15)
	
	# Adjust layout and save the figure
	plt.tight_layout(pad=2)
	plt.savefig("Integrated_Moisture_Up_Genesis",bbox_inches="tight",dpi=600)
	plt.close()
	
	# Define the minimum and maximum values for the contour levels
	min_rh_cross = 0
	max_rh_cross = np.max(rh_cross)
	
	# Define the interval between contour levels
	iterator_rh_cross = 0.15
	
	# Generate an array of contour levels
	levels_rh_cross = np.arange(min_rh_cross,max_rh_cross,iterator_rh_cross)
	
	#Define y axis labels
	zaxis_plot=[1000, 900, 850, 750, 700,  600, 500, 300, 200, 100]

	#Plot cross-section
	fig = plt.figure(figsize=[18,12])
	ax = fig.add_subplot(1, 1, 1)

	ax.set_xlabel('Longitude', fontsize=35)
	ax.set_ylabel('Pressure (hPa)', fontsize=35)

	# Plot rh field   
	# make a color map of fixed colors

	cs = plt.contourf(cross['lon'], cross['layers'],rh_cross, levels = levels_rh_cross, cmap=cmap)

	cb=plt.colorbar(cs,orientation="vertical", aspect=25,pad=0.05,shrink=0.9, extend="both")
	cb.ax.tick_params(labelsize=35) 
	cb.set_label(label="Moisture Uptake  (" + 'mm/day'+")", size=35,labelpad=15)


	ax.set_yticklabels(zaxis_plot)

	plt.savefig("cross_Genesis",bbox_inches="tight",dpi=600)
	plt.close()
	
