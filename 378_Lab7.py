import arcpy
arcpy.env.workspace = "lab7_data"
# Allow overwrite
# Once the Spatial Analyst extension license has been retrieved by the script, tools using that extension can be used. 
arcpy.env.overwriteOutput = True
arcpy.CheckOutExtension("Spatial")

# Calculate slope from elevation
elevation = arcpy.Raster("elevation.tif")
slope = arcpy.sa.Slope(elevation, "DEGREE", 1)

# Get the minimum and maximum slope values and convert them into float values
minimum = arcpy.GetRasterProperties_management(slope, "MINIMUM")
zMin = float(minimum.getOutput(0))
maximum = arcpy.GetRasterProperties_management(slope, "MAXIMUM")
zMax = float(maximum.getOutput(0))
print (zMin)
print (zMax)

##outName=arcpy.env.workspace+'\Elevation_Colored.tif'
##if os.path.exists(outName):
##    os.remove(outName)

# create raster of scaled elevations between 0 and 1
f = ((slope-zMin)/(zMax-zMin))
# Create red, green and blue rasters
R = 255*(elevation/elevation)
G = f*255
B = f*255

# Compose the three rasters to a TIFF format raster file
arcpy.CompositeBands_management(str(R)+";"+str(G)+";"+str(B), "slope_colored.tif")
print ("New RGB composite color-shaded image generated.")

