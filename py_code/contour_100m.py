layer = iface.activeLayer()
elev_field = "ELEV"


elev_values = list(range(0, 2101, 100))

output_layer = QgsVectorLayer("LineString?crs=" + layer.crs().authid(), "Isolinee", "memory")
provider = output_layer.dataProvider()
fields = layer.fields()


provider.addAttributes(fields.toList())
output_layer.updateFields()

for elev in elev_values:

    expression = f'"{elev_field}" = {elev}'

    layer.selectByExpression(expression)
    selected_features = layer.selectedFeatures()

    provider.addFeatures(selected_features)

    layer.removeSelection()


QgsProject.instance().addMapLayer(output_layer)

iface.layerTreeView().refreshLayerSymbology(output_layer.id())
