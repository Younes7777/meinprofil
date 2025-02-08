import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
from .berufsinhalt import berufserfahrung_inhalt
from .Studium import Studium
from .Programmiersprachen import Programmiersprachen
from .ML import ML
from .azure import azure
from .sprachen import sprachen
dash.register_page(__name__, path='/', order=0)


# Layout mit Buttons und versteckten Abschnitten
layout = html.Div([
    html.Div([
        html.Img(src="/assets/my.jpg", className="hero-image", style={"width": "100%", "height": "800px", "object-fit": "cover", "position": "relative"}),
            html.Div("Younes Iferd", style={
                "position": "absolute", 
                "bottom": "20px",  
                "right": "20px",  
                "color": "white", 
                "fontSize": "64px",  # Größere Schrift
                "backgroundColor": "#007bff",  # Primary Blau, Standard Bootstrap Wert
                "padding": "5px 20px",  # Mehr Platz um den Text
                "borderRadius": "5px",
                "fontWeight": "normal"  # Schrift ist nicht mehr fett
            })
    ], style={"position": "relative"}),


    html.Div(style={"height": "20px"}),
    
    dcc.Markdown('Geboren am 09. Februar 1977 in Rabat (Marokko)', style={'textAlign': 'center'}),
    dcc.Markdown('Verheiratet und Vater eines achtjährigen Sohnes', style={'textAlign': 'center'}),
    
    
    html.Hr(),
    dcc.Markdown('Leidenschaftlicher Data Analyst mit Erfahrung in der statistischen und ökonometrischen Datenanalyse. \n'
                 'Versiert in diversen Programmiersprachen und analytischen Methoden. Ein hilfsbereiter Teamplayer \n'
                 'mit einem lösungsorientierten Ansatz zur Dateninterpretation und Entscheidungsfindung.',
                 style={'textAlign': 'left'}),

    # Buttons zur Steuerung
    html.Div([
        dbc.Button("Berufserfahrung", id="btn-beruf", color="primary", className="flex-grow-1"),
        dbc.Button("Studium", id="btn-studium", color="primary", className="flex-grow-1"),
        dbc.Button("Programmiersprachen", id="btn-it", color="primary", className="flex-grow-1"),
        dbc.Button("Machine Learning", id="btn-ml", color="primary", className="flex-grow-1"),
        dbc.Button("Microsoft Azure", id="btn-azure", color="primary", className="flex-grow-1"),
        dbc.Button("Sprachen", id="btn-sprachen", color="primary", className="flex-grow-1"),
    ], style={"display": "flex", "width": "100%", "gap": "10px", "marginBottom": "20px"}),

    # Speicher für die Sichtbarkeit
    dcc.Store(id='visible-section', data={}),

    # Inhalte der Abschnitte
    html.Div(id='content-section'),

    # Script zum Scrollen zum spezifischen Abschnitt
    html.Script('''
        function scrollToSection() {
            let contentSection = document.querySelector('#content-section');
            if (contentSection) {
                contentSection.scrollIntoView({ behavior: 'smooth' });
            }
        }
    ''')
])

@callback(
    Output('content-section', 'children'),
    [Input('btn-beruf', 'n_clicks'),
     Input('btn-studium', 'n_clicks'),
     Input('btn-it', 'n_clicks'),
     Input('btn-ml', 'n_clicks'),
     Input('btn-azure', 'n_clicks'),
     Input('btn-sprachen', 'n_clicks')]
)
def update_content(n_beruf, n_studium, n_it, n_ml, n_azure, n_sprachen):
    ctx = dash.callback_context
    if not ctx.triggered:
        return ""  # Keine Sektion initial sichtbar
    
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    sections = {
        "btn-beruf": html.Div(berufserfahrung_inhalt, id="content-beruf", className="content-section"),
        "btn-studium": html.Div(Studium, id="content-studium", className="content-section"),
        "btn-it": html.Div(Programmiersprachen, id="content-it", className="content-section"),
        "btn-ml": html.Div(ML, id="content-ml", className="content-section"),
        "btn-azure": html.Div(azure, id="content-azure", className="content-section"),
        "btn-sprachen": html.Div(sprachen, id="content-sprachen", className="content-section")
    }
    
    # Scrollen auslösen
    html.Script('scrollToSection();')

    return sections.get(button_id, "")
