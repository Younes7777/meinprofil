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
    
])

