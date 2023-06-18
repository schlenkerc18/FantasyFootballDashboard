import dash
from dash import Dash, dcc, html, Input, Output, callback, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np

from player_files import  files

dash.register_page(__name__, path='/')

layout = html.Div(children=[
    html.Br(),
    html.Div(className="row", children=[
        dbc.Label("Year", style={'margin-right': '10px'}),
        dcc.Dropdown(
            className="column",
            id='year-dropdown',
            placeholder='Select a Year',
            options=[2022, 2021, 2020, 2019, 2018],
            style={'margin-right': '80px'}
        ),
        dbc.Label("Position", style={'margin-right': '10px'}),
        dcc.Dropdown(
            className="column",
            id='position-dropdown',
            placeholder='Select a Position',
            options=['QB', 'RB', 'WR', 'TE'],
            style={'margin-right': '100px'}
        )
        ], style={'display': 'flex', 'flex-direction': 'row', 'margin-bottom': '10px'}),

    html.Br(),
    html.Div(id='player-stats', ),
])




@callback(
    Output(component_id='player-stats', component_property='children'),
    Input(component_id='year-dropdown', component_property='value'),
    Input(component_id='position-dropdown', component_property='value')
)
def show_player_stats(year, position):
    df = files.get_files(year, position)
    df = files.clean_data(df)

    dt = dash_table.DataTable(
        data = df.to_dict('records'),
        columns=[{'name': i, 'id': i} for i in df.columns],
        sort_action='native',
        style_data={
            'backgroundColor': '#FAF9F6',
            'color': 'black'
        },
        # row_deletable=True
    )
    return dt