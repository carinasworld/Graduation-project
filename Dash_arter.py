# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 09:24:50 2021

@author: Nelly
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import sys
import os
import pandas as pd 


app = dash.Dash(__name__)

df = pd.read_csv(r'C:\Users\Nelly\Downloads\artsliste.csv')

test = df['0'].unique()

options = [{'label': t, 'value': t} for t in test]

art_dropdown = dcc.Dropdown(
    options=options,
    searchable=False,
    multi=True,
    )


app.layout = html.Div(art_dropdown)

if __name__ == '__main__':
    app.run_server(debug=True)