from batch_api import sett_sammen_koordinat_par, api_batch_prosess
import pandas as pd
import grequests
import requests
from read_coord_csv import last_inn_data_koord
from datakilde_info import print_datakilde_info

#Last inn CSV med koordinater
rel_path = 'originalkoordinater_endelig.csv'
ost_koord, nord_koord = last_inn_data_koord(rel_path)

#Info om datakilder
print_datakilde_info()

#Slå sammen koordinater med zip
worklist_url = sett_sammen_koordinat_par(ost_koord, nord_koord)
batchsize = 1000
subbatchsize = 50
api_batch_prosess(worklist_url, batchsize, subbatchsize)



    
