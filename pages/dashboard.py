import dash
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from .side_bar import sidebar

dash.register_page(__name__, title='App1', order=3)

from dash import html

layout = html.Div([
    html.H3("Diese Seite wird derzeit bearbeitet"),
    html.H4("Power BI Bericht: Chinook Musikverkauf"),
    html.A("Download Bericht (PBIX)", 
           href="https://github.com/Younes7777/Chinook_Verkaufs-bersicht/blob/main/Chinook%20%E2%80%93%20Verkaufs%C3%BCbersicht.pbix",
           target="_blank")

    
])

