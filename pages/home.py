import dash
from dash import Dash, dcc, html, Input, Output, callback, dash_table
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import pandas as pd
import numpy as np

from player_files import  files

dash.register_page(__name__, path='/')

# get dataframes
df = files.get_files(2022, 'QB')
df = files.clean_data(df)

layout = html.Div(children=[
    html.Br(),
    html.Div(className="row", children=[
        dbc.Label("Year", style={'margin-right': '10px'}),
        dcc.RadioItems(
            className="column",
            id='year-radioItem',
            options=[2022, 2021, 2020, 2019, 2018],
            style={'margin-right': '80px', 'margin-bottom': '15px'},
            inline=True,
            inputStyle={"margin-right": "4px", 'margin-left': '10px'}
        ),
        dbc.Label("Position", style={'margin-right': '10px'}),
        dcc.RadioItems(
            className="column",
            id='position-radioItem',
            options=['QB', 'RB', 'WR', 'TE'],
            style={'margin-right': '100px'},
            inline=True,
            inputStyle={"margin-right": "4px", 'margin-left': '10px'}
        )
        ], style={'display': 'flex', 'flex-direction': 'row', 'margin-bottom': '10px'}),

    html.Br(),
    html.Div(id='player-stats')
])


@callback(
    Output(component_id='player-stats', component_property='children'),
    Input(component_id='year-radioItem', component_property='value'),
    Input(component_id='position-radioItem', component_property='value')
)
def show_player_stats(year, position):
    df = files.get_files(year, position)
    df = files.clean_data(df)

    dt = dash_table.DataTable(
        data = df.to_dict('records'),
        columns = [{'name': i, 'id': i} for i in df.columns],
        sort_action='native'
    )

    return dt

@callback(
    Output("player-stats", "style_data_conditional"),
    Input("player-stats", "selected_row_ids"),
)
def style_selected_rows(sel_rows):
    if sel_rows is None:
        raise PreventUpdate

    val = [
        {"if": {"filter_query": "{{id}} ={}".format(i)}, "backgroundColor": "#FFCCCB",}
        for i in sel_rows
    ]

    return val