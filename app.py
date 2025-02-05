import dash
from dash import Dash, html
import dash_bootstrap_components as dbc
import os

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.CERULEAN])

header = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row([
                dbc.NavbarToggler(id="navbar-toggler"),
                    dbc.Nav([
                        dbc.NavLink(page["name"], href=page["path"], style={"color": "white"})
                        for page in dash.page_registry.values()
                        if not page["path"].startswith("/app")
                    ])
            ])
        ],
        fluid=True,
    ),
    dark=True,
    color='primary'
)

app.layout = dbc.Container([header, dash.page_container], fluid=False)

if __name__ == "__main__":
    app.run_server(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
