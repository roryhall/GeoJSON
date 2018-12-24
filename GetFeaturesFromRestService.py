# Test a REST point ARCGIS Server (Web Services)
# Query GET return a JSON object and create a feature class

## "https://gisservices.information.qld.gov.au/arcgis/rest/services for outside the network

import arcpy
import urllib
import json


class LoadJSON(object):
    def __init__(self, data):
	    self.__dict__ = json.loads(data)


	    
outputJSON = r'C:\Temp\data4.json'

## return the geometry of and area of interest (LOTPLN/s)
## returns a dictionary of 'rings'
def getGeometryString(aoi):
    
        request = urllib.urlopen(aoi)        
        myJSON = request.read()
        loaded_json = json.loads(myJSON)
        
        areaInterest = LoadJSON(myJSON)
        #print areaInterest # Returns the JSON file to the interpreter window. Can copy out into txt editor and save as blah.json
        sr = areaInterest.spatialReference['latestWkid']
        
        spatialReference = ',"spatialReference": {}"wkid":{}{}'.format ('{',sr, '}')
        #print spatialReference
        
        x = len(areaInterest.features) # How many features?

        for y in range (x):   # for each feature            
            cleanGeometryList = str(eval(json.dumps(areaInterest.features[y]['geometry'])))
            inputGeometry = '{}{}{}'.format (cleanGeometryList[0:-1],spatialReference, '}')
            #print inputGeometry

        ##### Could copy this to a feature for clipping later

        return inputGeometry


            
# Area of Interest query
query3 = {'where':"LOTPLAN = '6BE60'"} #Syntax WORKS !!!!
encodedQry3 = urllib.urlencode(query3)
#print encodedQry3 
#encodedQry3 = "where=LOTPLAN+%3D+%276BE60%27"

## To return geometry leave out returnCountOnly = true 
field = "LOTPLAN"
querySettings = "http://gisservices/arcgis/rest/services/PlanningCadastre/LandParcelPropertyFramework/MapServer/4/query?{}&outFields={}&returnCountOnly={}&f=json"
queryRVMGeometry = "https://gisservices/arcgis/rest/services/Biota/VegetationManagement/MapServer/109/query?{}&geometryType=esriGeometryPolygon&spatialRel=esriSpatialRelIntersects&outFields={}&returnGeometry=true&f=geojson"

## Area of interest string ( where LOTPLAN = something)
aoi = querySettings.format(encodedQry3, field, '')
#aoiCount = querySettings.format(encodedQry3, field, 'true')

print getGeometryString(aoi)
print "\n"

## Geometry of aoi string
## Pass the where claus to getGeometryString function
## Which returns a formated string for use to intersect another layer
geometryString = {'geometry': getGeometryString(aoi)}
aoiGeometryEncodedString = urllib.urlencode(geometryString)

print aoiGeometryEncodedString
print "\n"

## Pass the aoi geometry to an input geometry parameter of the URL to intersect a layer (RVM)
## The formatted string (URL) which will return the features from the layer (RVM) intersected with an area of interest
RVM_GeoJson = queryRVMGeometry.format(aoiGeometryEncodedString,'*')
print RVM_GeoJson

finalRequest = urllib.urlopen(RVM_GeoJson)        
GEOJSON = finalRequest.read()
loaded_Geojson = json.loads(GEOJSON)

## Write the request (URL) to a json file
with open(outputJSON, 'w') as outfile:
    json.dump(loaded_Geojson, outfile)

###############################WORKS creates a json file can open it in QGIS######################################



print "done"


















