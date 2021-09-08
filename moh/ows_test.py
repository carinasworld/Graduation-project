from owslib.wms import WebMapService
wms = WebMapService('https://geo.ngu.no/mapserver/BerggrunnOkologiWMS?request=GetCapabilities&service=WMS&version=1.3.0')

print("Title: ", wms.identification.title)
print("Type: ", wms.identification.type)
print("Operations: ", [op.name for op in wms.operations])
print("GetMap options: ", wms.getOperationByName('GetMap').formatOptions)
wms.contents.keys()

for key in ['BerggrunnOkologiWMS', 'Kalkinnhold_N250', 'Ultramafisk_N250', 'Ultramafisk_N250_oversikt']:
    print(wms.contents[key].title)

name = 'Kalkinnhold_N250'
layer = wms.contents[name]
print("Abstract: ", layer.abstract)
print("BBox: ", layer.boundingBoxWGS84)
print("CRS: ", layer.crsOptions)
print("Styles: ", layer.styles)
print("Timestamps: ", layer.timepositions)