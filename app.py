import dash
from dash import Dash, html
import dash_bootstrap_components as dbc
import os
from flask import request
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor
import geoip2.database
from datetime import datetime
import pytz

# .env laden (für DATABASE_URL)
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
print(f"DEBUG: DATABASE_URL = {DATABASE_URL}")

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.CERULEAN])
server = app.server

# --- Datenbank-Funktionen ---

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
    return conn

def create_table():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS visitors (
            id SERIAL PRIMARY KEY,
            ip VARCHAR(45),
            city VARCHAR(100),
            country VARCHAR(100),
            visit_time TIMESTAMP
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

create_table()

# GeoIP2 Reader initialisieren (Datei im Repo)
GEOIP_DB_PATH = 'GeoLite2-City.mmdb'
reader = geoip2.database.Reader(GEOIP_DB_PATH)

def log_visitor(ip):
    try:
        response = reader.city(ip)
        city = response.city.name or "Unknown"
        country = response.country.name or "Unknown"
    except Exception as e:
        print(f"GeoIP Lookup Fehler: {e}")
        city = "Unknown"
        country = "Unknown"

    def get_berlin_time():
        tz = pytz.timezone('Europe/Berlin')
        utc_now = datetime.utcnow()
        utc_now = pytz.utc.localize(utc_now)
        berlin_time = utc_now.astimezone(tz)
        return berlin_time

    visit_time = get_berlin_time()

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO visitors (ip, city, country, visit_time)
        VALUES (%s, %s, %s, %s)
    """, (ip, city, country, visit_time))
    conn.commit()
    cur.close()
    conn.close()

# Flask before_request Hook für Besucher-Logging
@server.before_request
def before_request_logging():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    if ip:
        log_visitor(ip)

# --- Dein Original-Code ---

from pages import projekte

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
        ],
        fluid=True,
    ),
    color="#0b5ed7",
    dark=True,
    style={"marginBottom": "10px"}
)

app.layout = dbc.Container([header, dash.page_container], fluid=True)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
