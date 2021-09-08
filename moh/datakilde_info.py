import requests

def print_datakilde_info():    
    r = requests.get('https://ws.geonorge.no/hoydedata/v1/datakilder')
    kildeinfo = r.json()
    keys = []
    for key in kildeinfo[0]:
        keys.append(key)
    print('Informasjon om datakilder:')
    kilde = keys[0]
    beskrivelse = keys[1]
    for dictio in kildeinfo:
        print(f'{dictio[kilde].title()}: {dictio[beskrivelse]}')

