from osgeo import gdal, ogr
import sys
import math

PowerLine = 'lab6_data/PowerLine.shp'
Parcels = 'lab6_data/Parcels.shp'

#get driver appropriate for input file
driver = ogr.GetDriverByName('ESRI Shapefile')

#open the file using the driver
openedPowerLine = driver.Open(PowerLine, gdal.GA_ReadOnly)
openedParcels = driver.Open(Parcels, gdal.GA_ReadOnly)


# -------------------- TASK 1 -------------------- #

#verify the file was opened, exit if not opened
if openedPowerLine is None:
    print('Failed to open file')
    sys.exit(1)
else:
    #get the first (and only) data layer
    PowerLineLayer = openedPowerLine.GetLayer(0)
    #get a feature from the layer
    PowerLinefeature  = PowerLineLayer.GetFeature(0)
    #Get the geometry of that feature and count its consecutive points
    PowerLinegeometry = PowerLinefeature.GetGeometryRef()
    nPts=PowerLinegeometry.GetPointCount()
    print("There are ",nPts,"points in this power line.")
    #Set the initial distance to be zero, loop through the consecutive points and keep adding the distance
    distance=0
    for i in range(nPts-1):
        #Get the coordinates of each point and the next point
        point1=PowerLinegeometry.GetPoint(i) 
        point2=PowerLinegeometry.GetPoint(i+1)
        x1 = point1[0]
        x2 = point2[0]
        y1 = point1[1]
        y2 = point2[1]
        #Calculate the euclidean distance between two points and sum them up
        distance=distance+math.sqrt(((x1-x2)**2+(y1-y2)**2))
    #transform from feet to mile
    finalDistance=distance/5280
    print("The length of the power line is ",finalDistance,"miles.")

    
    
# -------------------- TASK 2 PART 1-------------------- #    



#verify the file was opened, exit if not opened
if openedParcels is None:
    print('Failed to open file')
    sys.exit(1)
else:
    #get the layer and its definition; count the fields and loop them through
    ParcelLayer = openedParcels.GetLayer(0)
    ParcelFeatureDefn = ParcelLayer.GetLayerDefn()
    fieldCount = ParcelFeatureDefn.GetFieldCount()
    for i in range(0,fieldCount):
        #get the attribute names and their data types
        fieldDef = ParcelFeatureDefn.GetFieldDefn(i)
        fname = fieldDef.GetNameRef()
        ftype = fieldDef.GetType()
        #convert integer ftype to text equivalent
        ftypeString = fieldDef.GetFieldTypeName(ftype)
    print("The attribute names are "+fname+"and the attribute data types are "+ftypeString+".")


# -------------------- TASK 2 PART 2-------------------- #

#count parcel features and loop them through
ParcelFeatureCount=ParcelLayer.GetFeatureCount()
for i in range(0, ParcelFeatureCount):
    #get geometry of each parcel feature
    ParcelFeature  = ParcelLayer.GetFeature(i)
    ParcelGeometry=ParcelFeature.GetGeometryRef()
    #check whether the power line cross the parcel features
    if ParcelGeometry.Crosses(PowerLinegeometry):
        #if yes, get the address and area of that parcel
        address=ParcelFeature.GetField('SITUSADDR')
        area=ParcelGeometry.GetArea()
        print("Address is", address, "and the area is ", area, "sqft.")
            
  
