import pandas as pd

def last_inn_data_koord(path:str):
    koordinat_data = pd.read_csv(path)
    ost_koord = list(koordinat_data['Østkoordinat'])
    nord_koord = list(koordinat_data['nordkoordinat'])
    return ost_koord, nord_koord

ost_koord, nord_koord = last_inn_data_koord('originalkoordinater.csv')

