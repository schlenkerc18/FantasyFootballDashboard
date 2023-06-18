from dash import Dash, html, dcc
import dash
import dash_bootstrap_components as dbc

app = Dash(__name__, use_pages=True, external_stylesheets=["./assets/bootsrap.min.css"])

app.layout = html.Div([
    html.Div(
        [

            html.Div(
                dcc.Link(
                    f"{page['name']}", href=page["relative_path"]
                ),

            )
            for page in dash.page_registry.values()
        ],

    ),
	dash.page_container
], style={'margin-left': '2%', 'margin-right': '2%', 'margin-top': '15px'})

server = app.server

if __name__ == '__main__':
	app.run_server(
        host='0.0.0.0',
        port=8080,
        debug=False
    )