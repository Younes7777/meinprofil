import dash
from dash import Dash
import dash_bootstrap_components as dbc
from dotenv import load_dotenv
import os
import psycopg2
from psycopg2.extras import RealDictCursor

# --- Eigene Module ---
from visitor_tracking import (
    before_request_logging,
    after_request_logging,
    create_visitors_table
)

# --- Initialisierung & Konfiguration ---
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
print(f"DEBUG: DATABASE_URL = {DATABASE_URL}")

# Dash Setup
app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.CERULEAN])
server = app.server

# Flask Hooks für Besucher-Tracking
server.before_request(before_request_logging)
server.after_request(after_request_logging)


# --- Navigation Header ---
header = dbc.Navbar(
    dbc.Container(
        dbc.Nav(
            [
                dbc.NavLink(
                    page["name"],
                    href=page["path"],
                    style={
                        "color": "white",
                        "padding": "10px 15px",
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
                "justify-content": "center",
                "align-items": "center",
                "gap": "20px",
                "padding": "10px 0",
                "list-style": "none"
            }
        ),
        fluid=True,
    ),
    color="#0b5ed7",
    dark=True,
    style={"marginBottom": "10px"}
)

# --- App Layout ---
app.layout = dbc.Container([header, dash.page_container], fluid=True)

# --- App-Start ---
if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
