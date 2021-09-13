# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 08:52:49 2021

@author: Carin
"""

import pandas as pd

#%%

groups = pd.read_csv('C:/Users/Carin/OneDrive/Documents/AW academy/graduation/carina.csv')
small_groups = pd.read_csv('C:/Users/Carin/OneDrive/Documents/AW academy/graduation/carina_small.csv')

#%%
groups.columns
groups.terreng_DyrketMark[groups.terreng_DyrketMark > 1] = 1
groups['terreng_Innsjø'][groups['terreng_Innsjø'] >1] = 1
groups['terreng_Isbre'][groups['terreng_Isbre'] >1] = 1
groups['terreng_Kyst'][groups['terreng_Kyst'] >1] = 1
groups['terreng_Myr'][groups['terreng_Myr'] >1] = 1
groups['terreng_Plenliknende'][groups['terreng_Plenliknende'] >1] = 1
groups['terreng_Skog'][groups['terreng_Skog'] >1] = 1
groups['terreng_Sterkt_menneskepåvirket_område'][groups['terreng_Sterkt_menneskepåvirket_område'] >1] = 1
groups['terreng_Vei'][groups['terreng_Vei'] >1] = 1
groups['terreng_Åpent_område'][groups['terreng_Åpent_område'] >1] = 1
groups['terreng_Alpinbakke'][groups['terreng_Alpinbakke'] >1] = 1
groups['terreng_Befolket_område'][groups['terreng_Befolket_område'] >1] = 1

#%%
groups.rename(columns= {'latbin':'latitude', 'lonbin': 'longitude'}, inplace=True)
head=groups.head(30)

#%%
groups = groups.iloc[: , 1:]

groups['sum_per_row'] = groups.sum(axis=1)
groups['sum_per_row'] = groups['sum_per_row']- groups['latitude']
groups['sum_per_row'] = groups['sum_per_row']- groups['longitude']
groups['sum_per_row'] = groups['sum_per_row']- groups['moh']

groups['sum_per_row'] = groups['sum_per_row']- groups['terreng_DyrketMark']
groups['sum_per_row'] = groups['sum_per_row']- groups['terreng_Innsjø']
groups['sum_per_row'] = groups['sum_per_row']- groups['terreng_Isbre']
groups['sum_per_row'] = groups['sum_per_row']- groups['terreng_Kyst']
groups['sum_per_row'] = groups['sum_per_row']- groups['terreng_Myr']
groups['sum_per_row'] = groups['sum_per_row']- groups['terreng_Plenliknende']
groups['sum_per_row'] = groups['sum_per_row']- groups['terreng_Skog']
groups['sum_per_row'] = groups['sum_per_row']- groups['terreng_Sterkt_menneskepåvirket_område']
groups['sum_per_row'] = groups['sum_per_row']- groups['terreng_Vei']
groups['sum_per_row'] = groups['sum_per_row']- groups['terreng_Åpent_område']
groups['sum_per_row'] = groups['sum_per_row']- groups['terreng_Alpinbakke']
groups['sum_per_row'] = groups['sum_per_row']- groups['terreng_Befolket_område']

groups['sum_per_row'].min()
groups['sum_per_row'].max()
groups['sum_per_row']

groups_smol = groups[groups.sum_per_row > 10]
groups_smol.head()

#%%
nump = groups.to_numpy()

from sklearn.preprocessing import StandardScaler
ss=StandardScaler()
cols=groups_smol.columns
cols=list(cols)
tfs= ss.fit_transform(groups_smol[cols])


#%%


