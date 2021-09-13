# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 19:13:45 2021

@author: Carin
"""
import pandas as pd
import numpy as np

#%%

path = (f'C:/Users/Carin/OneDrive/Documents/AW academy/graduation/plant_moh.csv')
file= pd.read_csv(path) 
file.head()
file = file[['artsnavn', 'Østkoordinat', 'nordkoordinat', 'z', 'terreng']]

file['artsnavn'].astype('category')
file['terreng'].astype('category')

#%%
# get names of indexes for which
# column Age has value 21
vc = file.artsnavn.value_counts()
vc= vc[vc < 20].index
  
file = file[~file['artsnavn'].isin(vc)]


#%%

file=pd.get_dummies(file, columns=['artsnavn'])
file.head()
file['artsnavn'] = file['artsnavn'].apply(lambda x: str(x)+',')
file.head()

file[pd.to_numeric(file['nordkoordinat'], errors='coerce').notnull()]
file[pd.to_numeric(file['Østkoordinat'], errors='coerce').notnull()]

#%%

step_lon = 0.05
step_lat = 0.01
to_bin = lambda x: np.floor(x / step_lon) * step_lon
to_bin_lat = lambda x: np.floor(x / step_lat) * step_lat
moh_step = 25
to_bin_moh = lambda x: np.floor(x / moh_step) * moh_step
file["latbin"] = file.nordkoordinat.map(to_bin_lat)
file['latbin']
file["lonbin"] = file.Østkoordinat.map(to_bin_lon)
file['lonbin']
file['moh'] = file.z.map(to_bin_moh)
file['moh']
file.drop(columns=['nordkoordinat', 'Østkoordinat', 'z'], inplace = True)
head=file.head()
#%%

file['terreng'].unique()
file["terreng"].replace({"Kommunal veg": "Vei", "Fylkesveg": "Vei", 'Privat veg': 'Vei', 'Europaveg': 'Vei', 'Riksveg': 'Vei'}, inplace=True)
file["terreng"].replace({"Tettbebyggelse": 'Befolket_område', "Lufthavn": "Befolket_område", 'Rullebane': 'Befolket_område', 'SportIdrettPlass': 'Befolket_område'}, inplace=True)
file["terreng"].replace({"BymessigBebyggelse": 'Sterkt_menneskepåvirket_område', "IndustriomrÃ¥de": "Sterkt_menneskepåvirket_område", "Steintipp": 'Sterkt_menneskepåvirket_område', "Steinbrudd": "Sterkt_menneskepåvirket_område"}, inplace=True)
file["terreng"].replace({"Golfbane": 'Plenliknende', "Park": "Plenliknende", "Gravplass": "Plenliknende"}, inplace=True)
file["terreng"].replace({"Ã…pentOmrÃ¥de": 'Åpent_område', "InnsjÃ¸Regulert": "Innsjø", "InnsjÃ¸": "Innsjø", 'SnÃ¸Isbre': 'Isbre'}, inplace=True)
file["terreng"].replace({"Havflate": 'Kyst'}, inplace=True)
file['terreng'].unique()

#%%

file=pd.get_dummies(file, columns=['terreng'])
#%%
groups = file.groupby(["latbin", "lonbin", 'moh']).sum()

