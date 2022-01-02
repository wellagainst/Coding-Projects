from osgeo import gdal
from osgeo import osr
import numpy


def array2raster(newRasterFileName,rasterOrigin,pixelWidth,pixelHeight,array):
     #Step 1-- choose a driver
     outformat = 'GTiff'
     outDriver = gdal.GetDriverByName(outformat) 

     #Step 2 -- Create output dataset using that driver
     rows  = array.shape[0] 
     cols    = array.shape[1]
     print ('rows: ', rows, ' cols: ', cols)
     nBands   = 1
     dataType = gdal.GDT_Float32
     dsOut=outDriver.Create(newRasterFileName,cols,rows,nBands,dataType)

     #Step 3 -- Set Geotransform
     xCorner=rasterOrigin[0]
     yCorner=rasterOrigin[1]
     xOffset=0
     yOffset=0 
     geoT = [ xCorner, pixelWidth, xOffset, yCorner, yOffset, -pixelHeight]
     dsOut.SetGeoTransform( geoT )

     #Step 4 -- Set Projection
     mySrs = osr.SpatialReference()
     #mySrs.SetWellKnownGeogCS("WGS84")
     mySrs.ImportFromEPSG(4326) #WGS84 http://spatialreference.org/ref/epsg/
     myWKT = mySrs.ExportToWkt()
     #print myWKT
     dsOut.SetProjection(myWKT)

     #Step 5 -- Process Each Band 
     outband = dsOut.GetRasterBand(1)
     outband.SetColorInterpretation(gdal.GCI_Undefined)
     outband.WriteArray(array)
     outband.FlushCache()

     #Step 6 -- Close the output data 
     dsOut=None

## the main function
if __name__ == "__main__":
     #try to read the red and near infrared bands
     try:
          Red =gdal.Open('landsat\L71026029_02920000609_B30_CLIP.TIF',gdal.GA_ReadOnly)
          NIR =gdal.Open('landsat\L71026029_02920000609_B40_CLIP.TIF',gdal.GA_ReadOnly)

          #read Raster data as two-dimensional array; make sure the denominator is not zero
          Red_array=Red.ReadAsArray().astype(float)
          NIR_array=NIR.ReadAsArray().astype(float)
          print ('cols: ',Red.RasterXSize, 'rows: ',Red.RasterYSize)
          #create an empty array to store the final calculated NDVI for each cell
          ndvi_array=numpy.empty([Red.RasterYSize, Red.RasterXSize])
          #loop through every row and every column and perform NDVI calculation
          for row in range(Red.RasterYSize): 
               for col in range(Red.RasterXSize): 
                    ndvi_array[row, col] = (NIR_array[row, col]-Red_array[row, col])/(NIR_array[row, col]+Red_array[row, col])
          print(ndvi_array)
          #raster origin is the upper left x and y coordinates of the raster image
          rasterOrigin = (-92.9273762,45.1809979)
          #pixel width/height is the cell size (resolution of the raster image)
          pixelWidth = 28.5
          pixelHeight = 28.5
          newRasterFileName = 'ndvi.tif'
          array=ndvi_array
          #plug in variables and convert numeric array to raster image
          array2raster(newRasterFileName,rasterOrigin,pixelWidth,pixelHeight,array)
          print("NDVI image produced.")
    except:
         print("the files do not exist or cannot be opened.")


