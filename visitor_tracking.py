import psycopg2
from psycopg2.extras import RealDictCursor
import geoip2.database
import os
import pytz
from datetime import datetime
from flask import request, g
from dotenv import load_dotenv

# --- Initialisierung ---
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
GEOIP_DB_PATH = "GeoLite2-City.mmdb"

# GeoIP Setup
try:
    reader = geoip2.database.Reader(GEOIP_DB_PATH)
except Exception as e:
    print(f"[GeoIP] Fehler beim Laden der Datenbank: {e}")
    reader = None


def get_db_connection():
    try:
        return psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
    except Exception as e:
        print(f"[DB Connection Error] {e}")
        return None


def create_visitors_table():
    conn = get_db_connection()
    if conn is None:
        print("[create_visitors_table] DB-Verbindung fehlgeschlagen.")
        return
    try:
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS visitors")
        cur.execute("""
            CREATE TABLE IF NOT EXISTS visitors (
                id SERIAL PRIMARY KEY,
                ip VARCHAR(45),
                city VARCHAR(100),
                country VARCHAR(100),
                visit_time TIMESTAMPTZ,
                leave_time TIMESTAMPTZ,
                duration_seconds INTEGER
            )
        """)
        conn.commit()
        cur.close()
        print("[DB] Tabelle 'visitors' erfolgreich erstellt.")
    except Exception as e:
        print(f"[DB] Fehler beim Erstellen der Tabelle: {e}")
    finally:
        conn.close()


def before_request_logging():
    path = request.path

    # Nur GET auf Hauptseiten (nicht: Dash intern, Assets, Favicons)
    if not request.method == "GET":
        return
    if path.startswith("/_dash") or path.startswith("/assets") or path.endswith((".css", ".js", ".ico")):
        return

    g.start_time = datetime.utcnow()

    # IP extrahieren
    ip_raw = request.headers.get("X-Forwarded-For", request.remote_addr)
    ip_list = [ip.strip() for ip in ip_raw.split(",")]
    g.ip = next((ip for ip in ip_list if not ip.startswith(("10.", "172.", "192.168.", "127."))), ip_list[0])


def after_request_logging(response):
    if not hasattr(g, "start_time"):
        return response

    try:
        leave_time = datetime.utcnow()
        duration = int((leave_time - g.start_time).total_seconds())
        ip = getattr(g, "ip", "Unknown")

        # Geo-Daten ermitteln
        try:
            if reader is None or ip.startswith("127."):
                raise Exception("Lokale IP oder kein GeoIP verfügbar")
            geo = reader.city(ip)
            city = geo.city.name or "Unknown"
            country = geo.country.name or "Unknown"
        except Exception as e:
            print(f"[GeoIP Fehler] {e}")
            city = "Localhost"
            country = "Local"

        # Zeiten in Europe/Berlin umwandeln
        tz = pytz.timezone("Europe/Berlin")
        visit_time = pytz.utc.localize(g.start_time).astimezone(tz)
        leave_time_local = pytz.utc.localize(leave_time).astimezone(tz)

        # In DB schreiben
        conn = get_db_connection()
        if conn is None:
            print("[after_request_logging] DB-Verbindung fehlgeschlagen – Logging übersprungen.")
            return response

        cur = conn.cursor()
        cur.execute("""
            INSERT INTO visitors (ip, city, country, visit_time, leave_time, duration_seconds)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (ip, city, country, visit_time, leave_time_local, duration))
        conn.commit()
        cur.close()
        conn.close()

    except Exception as e:
        print(f"[after_request_logging] Error: {e}")

    return response
