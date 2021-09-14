# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 08:52:49 2021

@author: Carin
"""

import pandas as pd

#%%

#groups = pd.read_csv('C:/Users/Carin/OneDrive/Documents/AW academy/graduation/carina.csv')
groups = pd.read_csv('C:/Users/Carin/OneDrive/Documents/AW academy/graduation/carina_small.csv')

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

groups_smol = groups[groups.sum_per_row > 20]
groups_smol.head()


groups_smol.drop(columns=['sum_per_row'], inplace=True)
#%%

cols=groups_smol.columns
cols=list(cols)

#%%

groups_smol.drop(columns= ['artsnavn_Aconitum lycoctonum',
    'artsnavn_Atriplex prostrata prostrata',
    'artsnavn_Cerastium regelii',
    'artsnavn_Cicerbita macrophylla uralensis',
    'artsnavn_Geum ×intermedium',
    'artsnavn_Lysimachia europaea arctica',
    'artsnavn_Lysimachia europaea europaea',
    'artsnavn_Oxybasis glauca',
    'artsnavn_Parnassia palustris palustris',
    'artsnavn_Picea abies abies',
    'artsnavn_Taraxacum croceum'], inplace=True)


cols.remove('artsnavn_Aconitum lycoctonum')
cols.remove('artsnavn_Atriplex prostrata prostrata')
cols.remove('artsnavn_Cerastium regelii')
cols.remove('artsnavn_Cicerbita macrophylla uralensis')
cols.remove('artsnavn_Geum ×intermedium')
cols.remove('artsnavn_Lysimachia europaea arctica')
cols.remove('artsnavn_Lysimachia europaea europaea')
cols.remove('artsnavn_Oxybasis glauca')
cols.remove('artsnavn_Parnassia palustris palustris')
cols.remove('artsnavn_Picea abies abies')
cols.remove('artsnavn_Taraxacum croceum')

#%%

cols=pd.Series(cols)

cols=cols.str.replace('[','')
cols=cols.str.replace(']','')
cols=cols.str.replace('artsnavn_','')
cols=cols.str.replace('_',': ')
cols=cols.str.replace('terreng','Terreng')
cols=cols.str.capitalize()

groups_smol.columns=cols

groups_smol.head()

#%%

groups_smol.to_csv('C:/Users/Carin/OneDrive/Documents/AW academy/graduation/beautiful_csv.csv', index=False)



