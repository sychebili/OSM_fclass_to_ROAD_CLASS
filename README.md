# OSM_fclass_to_ROAD_CLASS
This Python code can be used to convert OpenStreetMap's fclass road categories to Esri's ROAD_CLASS values in ArcGIS.

INSTRUCTIONS:

1. In ArcGIS, add a ROAD_CLASS field (Short) to the OSM roads layer's attribute table
2. Open the calculate field tool for the ROAD_CLASS column
3. Select Expression Type "Python"
4. In the box labeled "ROAD_CLASS =" enter this text: classify_road(!fclass!)
5. Copy and paste the code below into the box labeled Code Block:
6. Run the tool
