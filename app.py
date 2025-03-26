import dash
from dash import Dash, html
import dash_bootstrap_components as dbc
import os

# Initialisiere die Dash-App
app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.CERULEAN])

# Importiere Seiten (z.B. Projekte-Seite)
from pages import projekte

# Layout für die App definieren
header = dbc.Navbar(
    dbc.Container(
        [
            dbc.Nav(
                [
                    dbc.NavLink(
                        page["name"], 
                        href=page["path"], 
                        style={
                            "color": "white", 
                            "padding": "10px 15px",  # Abstand innerhalb der Links
                            "text-decoration": "none",  
                            "font-weight": "bold"
                        }
                    )
                    for page in dash.page_registry.values()
                    if not page["path"].startswith("/app")
                ],
                navbar=True,
                style={
                    "display": "flex",
                    "justify-content": "center",  # Zentrierung der Links
                    "align-items": "center",
                    "gap": "20px",  # Abstand zwischen Links
                    "padding": "10px 0",
                    "list-style": "none"
                }
            ),
        ],
        fluid=True,
    ),
    color="#0b5ed7",  # Hintergrundfarbe
    dark=True,
    style={"marginBottom": "10px"}
)

# Layout der gesamten App
app.layout = dbc.Container([header, dash.page_container], fluid=True)

# Starte den Server
if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
