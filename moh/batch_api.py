from pandas.core.frame import DataFrame
from read_coord_csv import last_inn_data_koord
import pandas as pd
import grequests
import requests

rel_path = 'originalkoordinater.csv'

def sett_sammen_koordinat_par(ost, nord):
    coordinates_list = []
    for coord in zip(ost, nord):
        coordinates_list.append(list(coord))
    return coordinates_list

def api_batch_prosess(liste_koordinater, batch, subbatch):
    worklist_url = liste_koordinater
    batchsize = batch
    subbatchsize = subbatch
    df = pd.DataFrame(columns=['datakilde', 'terreng', 'x', 'y', 'z'])
    df.to_csv('moh.csv', index=False)

    def exception_handler(request, exception):
        print(f"Request failed:", exception)

    for batch_no,i in enumerate(range(0, len(worklist_url), batchsize)):
        print(f"Processing batch {batch_no} out of {len(range(0, len(worklist_url), batchsize))}...")
        batch = worklist_url[i:i+batchsize]
        urls = []
        for url in range(0, len(batch), subbatchsize):
            liste_pkt = batch[url:url+subbatchsize]
            r = f'https://ws.geonorge.no/hoydedata/v1/punkt?geojson=false&punkter={liste_pkt}&koordsys=4326'
            urls.append(r)
        rs = [grequests.get(u) for u in urls]
        responses = grequests.map(rs, exception_handler=exception_handler)
        for r in responses:
            resp = r.json()
            for data in resp['punkter']:
                df = df.append(data, ignore_index=True)
        df.to_csv('moh.csv', index=False, mode='a+', header=False)


#skriv
# test_df = pd.DataFrame(columns=['datakilde', 'terreng', 'x', 'y', 'z'])
# test = responses[1].json()
# for i in test['punkter']:
#     test_df = test_df.append(i, ignore_index=True)


