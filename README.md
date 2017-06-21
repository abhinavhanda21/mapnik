# mapnik
render osm files using mapnik

download a .osm file by exporting it from osm.org

create a mapnik_style.xml file

add your file name instead of map(2).osm in <Parameter name="file">map(2).osm</Parameter>

create render.py

add your .osm files longitudes and latitudes in bbox=(Envelope( 75.76,30.83,75.96,30.95)) 

the format should be bbox=(Envelope( min longitude, min latitude, max longitude, min latitude))

open terminal and when you are in file directory run: python render.py
