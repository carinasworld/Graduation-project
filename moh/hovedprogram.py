from batch_api import sett_sammen_koordinat_par, api_batch_prosess
import pandas as pd
import grequests
import requests
from read_coord_csv import last_inn_data_koord
from datakilde_info import print_datakilde_info

#Last inn CSV med koordinater
rel_path = 'originalkoordinater.csv'
ost_koord, nord_koord = last_inn_data_koord('originalkoordinater.csv')

#Info om datakilder
print_datakilde_info()

#Slå sammen koordinater med zip
worklist_url = sett_sammen_koordinat_par(ost_koord, nord_koord)
batchsize = 1000
subbatchsize = 50
api_batch_prosess(worklist_url, batchsize, subbatchsize)


#Noter de med missing moh?
# idx_missing = []
# for idx, json in enumerate(liste_koord_med_moh):
#     for punkt in json['punkter']:
#         if punkt['z'] == 2.39:
#             idx_missing.append(idx)
    
