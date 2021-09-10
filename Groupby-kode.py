# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 19:13:45 2021

@author: Carin
"""
import pandas as pd
import numpy as np
#%%

path = (f'C:/Users/Carin/OneDrive/Documents/AW academy/graduation/ExcelExport_5361632_Page_{40}.xlsx')
file= pd.read_excel(path, header=2) 
file = file[['Artsnavn', 'Østkoordinat', 'Nordkoordinat']]
file['Artsnavn'].astype('category')
#%%
step = 250
to_bin = lambda x: np.floor(x / step) * step
file["latbin"] = file.Nordkoordinat.map(to_bin)
file["lonbin"] = file.Østkoordinat.map(to_bin)
file.drop(columns=['Nordkoordinat', 'Østkoordinat'], inplace = True)
groups = file.groupby(["latbin", "lonbin"]).sum()

file