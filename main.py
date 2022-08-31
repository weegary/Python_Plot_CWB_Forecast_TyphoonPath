# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 11:52:45 2022

@author: Gary
@function: plot CWB typhoon's path data (W-C0034-005)

"""

def GetTyphoons(file_name):
    import json
    with open(file_name,"r",encoding="utf-8") as f: 
        data = json.load(f)
    data = data['cwbopendata']
    typhoons = data['dataset']['tropicalCyclones']['tropicalCyclone']
    return typhoons

#%%
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
plt.figure(dpi=600, figsize = (4,4))
m = Basemap(projection='mill',
            resolution='i',
            llcrnrlat = 18,
            llcrnrlon = 115,
            urcrnrlat = 32,
            urcrnrlon = 140)
m.drawcoastlines(linewidth=0.5)
m.fillcontinents(color='white',lake_color='white')

#%%
file_name = r'W-C0034-005.json' 
typhoons = GetTyphoons(file_name)

for t in typhoons:

    lon = []
    lat = []

    for i in t['forecast_data']['fix']:
        temp = i['coordinate'].split(',')
        lon.append(float(temp[0]))
        lat.append(float(temp[1]))

    for i in range(len(lon)):
        x, y = m(lon, lat)
        m.plot(x, y, marker = '.', color='k',markerfacecolor='r',markeredgecolor='r', markersize=1, linewidth=1,zorder=1)
