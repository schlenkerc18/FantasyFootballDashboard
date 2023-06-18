import json

import dash
from dash import Dash, dcc, html, Input, Output, callback, dash_table, State
from dash.exceptions import PreventUpdate

import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go

from player_files import files


dash.register_page(__name__, name='Player Search')

layout = html.Div(children=[
    html.Br(),
    html.Div(className="row", children=[
            dbc.Input(id='player-name', placeholder='Search Player'),
            # dbc.Button("Search", id='search-button', )
        ], style={'display': 'flex', 'flex-direction': 'row', 'margin-bottom': '10px'}),

    html.Br(),
    html.Div(id='single-player-stats', ),
    dcc.Graph(id = 'point-graph'),
    dcc.Store(id='player-data')
])



@callback(
    Output(component_id='single-player-stats', component_property='children'),
    Output(component_id='player-data', component_property='data'),
    Input(component_id='player-name', component_property='value'),
)
def show_stats(player_name):
    # prevent update if player name has not been entered
    if (player_name is None):
        raise PreventUpdate

    print(player_name)
    df, isPlayer = files.get_player_stats(player_name)

    # prevent update if player is not found
    if (isPlayer == False):
        raise PreventUpdate

    # save data
    df_json = df.to_json(date_format='iso', orient='split')

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
    return dt, df_json

@callback(
    Output('point-graph', 'figure'),
    Input('player-data', 'data')
)
def graph_fantasy_points(player_data):
    if (player_data is None):
        raise PreventUpdate

    df = pd.read_json(player_data, orient='split')

    fig = go.Figure(go.Scatter(
        x=df.Year, y=df.FPTS
    ))

    fig.update_layout(
        xaxis=dict(
            tickmode='array',
            tickvals=df.Year
        ),
        title_text = 'Fantasy Points Per Year',
        title_x = 0.5
    )


    return fig




