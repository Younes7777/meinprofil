import dash
from dash import Dash, html
import dash_bootstrap_components as dbc
import os
from flask import request, send_file
from datetime import datetime
import csv
import requests

# Importiere das Passwort aus der externen Datei
from password import LOG_DOWNLOAD_SECRET

# Initialisiere die Dash-App
app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.CERULEAN])
server = app.server  # für Flask-Zugriff

# ---------------------
# Besuchstracking-Teil
# ---------------------

def get_ip():
    """Ermittelt die IP-Adresse des Besuchers"""
    if request.headers.get('X-Forwarded-For'):
        return request.headers.get('X-Forwarded-For').split(',')[0]
    return request.remote_addr

def get_city_from_ip(ip):
    """Ermittelt die Stadt des Besuchers basierend auf der IP-Adresse"""
    try:
        res = requests.get(f"http://ip-api.com/json/{ip}").json()
        return res.get("city", "Unbekannt")
    except:
        return "Unbekannt"

def log_visit(ip, city):
    """Loggt den Besuch in einer CSV-Datei mit Zeitstempel"""
    timestamp = datetime.now().isoformat()  # Holt den aktuellen Zeitstempel
    with open("visits.csv", "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, ip, city])  # Zeitstempel, IP und Stadt

@server.before_request
def track_visits():
    """Verfolgt jeden Besuch und loggt die IP und Stadt"""
    if request.path.startswith("/_") or "download-log" in request.path:
        return
    ip = get_ip()
    city = get_city_from_ip(ip)
    log_visit(ip, city)

# Route zum Herunterladen der Logdatei
@server.route("/download-log")
def download_log():
    """Lädt die Logdatei herunter, wenn das Secret korrekt ist"""
    secret = request.args.get("secret")
    if secret != LOG_DOWNLOAD_SECRET:
        return "Zugriff verweigert", 403

    if not os.path.exists("visits.csv"):
        return "Noch keine Daten vorhanden", 404

    return send_file("visits.csv", mimetype="text/csv", as_attachment=True)

# ---------------------
# Layout der Anwendung
# ---------------------

# Importiere Seiten (z.B. Projekte-Seite)
from pages import projekte

# Header-Menü
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

# Hauptlayout
app.layout = dbc.Container([header, dash.page_container], fluid=True)

# Starte den Server
if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
