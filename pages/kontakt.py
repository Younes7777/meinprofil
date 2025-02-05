import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, order=3)

green_text = {'color':'green'}

def layout():
    return dbc.Row([
        dbc.Col([
    dcc.Markdown('# Younes Iferd', className='mt-3'),
    dcc.Markdown('### Persönliche Daten', style={'color':'gray'}),
    dcc.Markdown('Address', style=green_text),
    dcc.Markdown('Grenzdamm 6 25421 Pinneberg'),
    dcc.Markdown('Telefonnummer', style=green_text),
    dcc.Markdown('00491799487602'),
    dcc.Markdown('Email', style=green_text),
    dcc.Markdown('yiferd@yahoo.fr'),
    
        ], width={'size':6, 'offset':2})
], justify='center')