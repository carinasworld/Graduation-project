# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 14:52:36 2021

@author: Carin
"""

import requests
import pandas as pd
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import numpy as np
#%%

r = requests.get("https://data.artsdatabanken.no/Natur_i_Norge/Natursystem/Milj%C3%B8variabler/Kalkinnhold/polygon.32633.geojson")

data = r.json()

coords= pd.read_csv('C:/Users/Carin/OneDrive/Documents/AW academy/graduation/ferdige.csv')
CaO_innhold: int = 0 
list_num: int = 0

def polygon(CaO_innhold: int = 0 , list_num: int = 0):
    polyx = data['features'][CaO_innhold]['geometry']['coordinates'][list_num][0]

    lons_vect = []
    lats_vect= []
    for i in range(0, len(polyx)):
        lons_vect.append(polyx[i][0])
        lats_vect.append(polyx[i][1])
        
    lons_lats_vect = np.column_stack((lons_vect, lats_vect))
    polygon = Polygon(lons_lats_vect)
    
    true_vals=[]
    for num in range(0, len(coords)):
        point = Point(coords['lon'][num], coords['lat'][num])
        bool_point = point.within(polygon) # check if a point is in the polygon 
        if bool_point == True:
            true_vals.append[coords['lon'][num], coords['lat'][num], CaO_innhold]
    return true_vals

pol = polygon()




def polygons(CaO_innhold: int = 0 , list_len:int=0):
    polygons= []
    for i in range(0,list_len):
        pol = polygon(CaO_innhold, i)
        polygons.append(pol)
    return polygons
pols= polygons(0, 15)


#lons_lats_vect = np.column_stack((lons_vect, lats_vect)) # Reshape coordinates
#polygon = Polygon(lons_lats_vect) # create 
#point = Point(coords['lon'][0], coords['lat'][0]) # create point

print(polygon.contains(point)) # check if polygon contains point
print(point.within(polygon)) # check if a point is in the polygon 








