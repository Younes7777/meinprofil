import dash
from dash import Dash, html
import dash_bootstrap_components as dbc
import os

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.CERULEAN])

header = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Nav(
                            [
                                dbc.NavLink(page["name"], href=page["path"], style={"color": "white"})
                                for page in dash.page_registry.values()
                                if not page["path"].startswith("/app") 
                                and not page["path"].startswith("/berufsinhalt") 
                                and not page["path"].startswith("/Studium") 
                                and not page["path"].startswith("/Programmiersprachen") 
                                and not page["path"].startswith("/ML") 
                                and not page["path"].startswith("/azure")
                            ],
                            navbar=True,
                            style={"display": "flex", "justify-content": "space-between", "width": "100%"}  # Flexbox für gleichmäßige Verteilung
                        ),
                        width=12,  # Die ganze Zeile nutzen
                    ),
                ],
                justify="start",  # Alle Spalten links ausrichten
                align="center",  # Vertikale Zentrierung
            ),
        ],
        fluid=True,
    ),
    dark=True,
    color='primary'
)




app.layout = dbc.Container([header, dash.page_container], fluid=False)

if __name__ == "__main__":
    app.run_server(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))


