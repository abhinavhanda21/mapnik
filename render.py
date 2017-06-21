#!/usr/bin/env python2

from mapnik import *

mapfile = 'mapnik_style.xml'
map_output = 'mymap7.png'

m = Map(2*1024,2*1024)
load_map(m, mapfile)
bbox=(Envelope( 75.76,30.83,75.96,30.95))

m.zoom_to_box(bbox)
print "Scale = " , m.scale()
render_to_file(m, map_output)
