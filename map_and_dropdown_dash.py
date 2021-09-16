import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd 
import dash_leaflet as dl
from dash.dependencies import Input, Output
import requests


app = dash.Dash(external_stylesheets=['https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css'],
                prevent_initial_callbacks=True)


## liste av arter 
df = pd.read_csv(r'C:\Users\Nelly\Downloads\artsliste.csv')

test = df['0'].unique()

options = [{'label': t, 'value': t} for t in test]

art_dropdown = dcc.Dropdown(
    options=options,
    searchable=True,
    multi=True,
    id = 'art_dropdown'
    )


## liste av terreng 
terrengdata = pd.read_csv(r'C:\Users\Nelly\Downloads\terreng.csv')

terreng = terrengdata['0'].unique()

ulike_terreng = [{'label': t, 'value': t} for t in terreng]

terreng_dropdown = dcc.Dropdown(
    options=ulike_terreng,
    searchable=True,
    multi=True,
    id = 'terreng_dropdown')



#Returnerer MOH for koordinater
def get_moh(nord, ost):
    moh = 0
    try:
        url = f'https://ws.geonorge.no/hoydedata/v1/punkt?nord={nord}&ost={ost}&geojson=false&koordsys=4326'
        r = requests.get(url)
        my_json = r.json()
        for dictio in my_json['punkter']:
            moh = dictio['z']
    except Exception as e:
        print(f'En feil har oppstått: {Exception}\nVennligst skriv inn koordinater på formen:')
    return moh



## kart
map_component= dl.Map(
    [dl.TileLayer(), dl.LayerGroup(id="layer"), dl.LocateControl(options={'locateOptions': {'enableHighAccuracy': True}})],
    id="map", style={'width': '100%', 'height': '50vh', 'margin': "auto", "display": "block"})



@app.callback(Output("text", "children"), Input("map", "location_lat_lon_acc"))
def update_location(location):
    return "YOU ARE HERE: You are within {} meters of (lat,lon) = ({},{})".format(location[2], location[0], location[1])


@app.callback(Output("text2", "children"), [Input("map", "location_lat_lon_acc"), Input("map", "click_lat_lng")])
def dash_moh(location, click_lat_lng):
    if click_lat_lng == None:
        nord,ost = location[0:2]
        moh = get_moh(nord,ost)
    else:
        nord,ost = click_lat_lng
        moh = get_moh(nord,ost)
    return f'MARKER:dette er {moh} meter over havet'


@app.callback(Output('text3','children'), [Input("art_dropdown", "value")])
def map_click(arter):
    print(arter)
    return f'valgt art: {arter }'


@app.callback(Output('text4','children'), [Input("map", "click_lat_lng")])
def map_click(plass):
    print(plass)
    return f'valgt lokasjon: {plass }'



@app.callback(Output('text5','children'), [Input("terreng_dropdown", "value")])
def map_click(terreng):
    return f' valgt terreng: {terreng }'



@app.callback(Output("layer", "children"), [Input("map", "click_lat_lng"), Input("map", "location_lat_lon_acc")])
def clickmarker_to_locatecontrol(click_lat_lng, location_lat_lon_acc):
    if click_lat_lng == None:
        mpos = [dl.Marker(position=location_lat_lon_acc, children=dl.Tooltip("({:.3f}, {:.3f})".format(*location_lat_lon_acc)))]
    else:
        mpos = [dl.Marker(position=click_lat_lng, children=dl.Tooltip("({:.3f}, {:.3f})".format(*click_lat_lng)))]
    return mpos


app.layout = html.Div([art_dropdown, terreng_dropdown, map_component, html.Div(id="text"),html.Div(id="text2"),html.Div(id="text3"),html.Div(id="text4"),html.Div(id="text5")])


if __name__ == '__main__':
    app.run_server(debug=True)


