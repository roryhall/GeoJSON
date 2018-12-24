# GeoJSON

Note ## "https://gisservices.information.qld.gov.au/arcgis/rest/services/PlanningCadastre 
Note ## "https://gisservices/arcgis/rest/services/Biota
for outside the network

Accessing data from a spatial web server using JSON.
This script can be used to intersect and return features from a spatial web service layer.
For example get all the features from a vegetation layer which intersects a parcel of land.
Step 1:
The script inputs a where claus to return a 'parcel' selection using attributes descriptor. eg where: LOTPLAN = '6BE60'
The where claus is encoded to be included in a REST server request URL
Step 2:
The geometry is returned for this feature by returning JSON and extracting the geometry
The geometry is encoded to be included in a REST server request URL
