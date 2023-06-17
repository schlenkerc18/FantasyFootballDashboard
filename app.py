from dash import Dash, dcc, html, Input, Output, callback, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np

app = Dash(__name__)

app.layout = html.Div(children=[

    html.Br(),
    html.Div(className="row", children=[
                dbc.Label("Year", style={'margin-right': '10px'}),
                dcc.Dropdown(
                    id='year-dropdown',
                    placeholder='Select a Year',
                    options=[2018, 2019, 2020, 2021, 2022, 2023],
                    style={'margin-right': '80px'}
                ),
                dbc.Label("Position", style={'margin-right': '10px'}),
                dcc.Dropdown(
                    id='position-dropdown',
                    placeholder='Select a Position',
                    options=['QB', 'RB', 'WR', 'TE'],
                    style={'margin-right': '100px'}
                )
        ], style={'display': 'flex', 'flex-direction': 'row', 'margin-bottom': '10px', 'margin-left': '10%', 'margin-right': '10%'}),

    html.Br(),
    html.Div(id='player-stats', style={'margin-left': '10%', 'margin-right': '10%'}),
    dcc.Interval(id = 'interval', interval=1000)
])

def get_files(year, position):


    if (position is None):
        print("no position was passed")
        df = pd.read_csv('./StatFiles/qb_stats.csv')
    if (position == 'QB'):
        df = pd.read_csv('./StatFiles/qb_stats.csv')
    elif (position == 'RB'):
        df = pd.read_csv('./StatFiles/rb_stats.csv')
    elif (position == 'WR'):
        df = pd.read_csv('./StatFiles/wr_stats.csv')
    elif (position == 'TE'):
        print("we are in the else part")
        df = pd.read_csv('./StatFiles/te_stats.csv')

    if (year is None):
        df = df[df.Year == 2023]
    else:
        df = df[df.Year == year]
    return df


@callback(
    Output(component_id='player-stats', component_property='children'),
    Input(component_id='year-dropdown', component_property='value'),
    Input(component_id='position-dropdown', component_property='value')
)
def get_player_stats(year, position):

    print("year:", year)
    print("position", position)
    df = get_files(year, position)
    df.Year = df.Year.astype(np.int64)

    # print(qb_df.info())

    dt = dash_table.DataTable(
        data = df.to_dict('records'),
        columns=[{'name': i, 'id': i} for i in df.columns],
        sort_action='native'
    )
    return dt


if __name__ == '__main__':
    app.run_server(debug=True)