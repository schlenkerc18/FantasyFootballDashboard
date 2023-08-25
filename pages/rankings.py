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

dash.register_page(__name__, name='Player Rankings')

df = pd.read_csv("./StatFiles/player_rankings.csv")

layout = html.Div(children=[
    html.Br(),
    dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns], row_deletable=True)
])
