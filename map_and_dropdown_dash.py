

import dash
import dash_core_components as dcc
import dash_html_components as html
import sys
import os
import pandas as pd 
import dash_leaflet as dl
from dash.dependencies import Input, Output

#app = dash.Dash(__name__)

app = dash.Dash(external_stylesheets=['https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css'],
                prevent_initial_callbacks=True)


df = pd.read_csv(r'C:\Users\Nelly\Downloads\artsliste.csv')

test = df['0'].unique()

options = [{'label': t, 'value': t} for t in test]

art_dropdown = dcc.Dropdown(
    options=options,
    searchable=False,
    multi=True,
    )

map_component= dl.Map(
    [dl.TileLayer(), dl.LocateControl(options={'locateOptions': {'enableHighAccuracy': True}})],
    id="map", style={'width': '100%', 'height': '50vh', 'margin': "auto", "display": "block"})


@app.callback(Output("text", "children"), [Input("map", "location_lat_lon_acc")])
def update_location(location):
    return "You are within {} meters of (lat,lon) = ({},{})".format(location[2], location[0], location[1])


app.layout = html.Div([art_dropdown,map_component,html.Div(id="text")])


if __name__ == '__main__':
    app.run_server(debug=True)
    
      
    
    