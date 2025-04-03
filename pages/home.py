import dash
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
from .berufsinhalt import berufserfahrung_inhalt
from .Studium import Studium
from .Programmiersprachen import Programmiersprachen
from .ML import ML
from .azure import azure
from .sprachen import Power_BI
import os
dash.register_page(__name__, path='/', order=0)


# Layout mit Buttons und versteckten Abschnitten
layout = html.Div([
    html.Div([
        dbc.Row([
        # Linke Spalte - Neue Profil Card
        dbc.Col([
            dbc.Card(
                dbc.Row([
                    # Linke Spalte - Profilbild
                    dbc.Col(
                        dbc.CardImg(
                            src="/assets/my.jpg",
                            className="img-fluid rounded-start",
                            style={"object-fit": "cover", "height": "100%", "width": "100%"}
                        ),
                        className="col-md-4 d-flex align-items-stretch",
                    ),



                    # Rechte Spalte - Name & Profiltext
                    dbc.Col(
                        dbc.CardBody([
                            html.H4("Younes Iferd", className="card-title text-primary fw-bold"),
                            html.P(
                                "Leidenschaftlicher Data Analyst mit umfassender Erfahrung in der statistischen und ökonometrischen "
                                "Datenanalyse. Versiert in Python, R, SQL und Machine Learning. Spezialisiert auf die Entwicklung interaktiver "
                                "Dashboards (Dash, Shiny) und datengetriebene Entscheidungsfindung. Die Weiterbildung zum Cloud Data Analyst habe ich neulich "
                                "erfolgreich abgeschlossen, wobei Power BI einen zentralen Bestandteil ausmacht. Aktuell in der Vorbereitung auf die PL-300-Zertifizierungsprüfung "
                                "von Microsoft. Teamorientiert mit Erfahrung in IT- und Telekommunikationsbranchen.",
                                className="card-text"
                            )
                        ]),
                        className="col-md-8",
                    ),
                ], className="g-0 d-flex align-items-stretch"),  # Gleicht Höhen an
                className="shadow border-0 p-3 mb-3 h-100 d-flex flex-column",
                style={"maxWidth": "100%"},
            )
        ], md=7, className="d-flex"),  # Spalte bleibt gleich hoch

        # Rechte Spalte - Persönliche Infos Card
        dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    html.H4("Über mich", className="card-title text-primary fw-bold"),
                    html.Ul([
                        html.Li(children=[html.Strong("📅 Geboren am: "), "09. Febraur 1977 in Rabat (Marokko)"]),
                        html.Li(children=[html.Strong("📞 Telefon: "), "+49 1799487602"]),
                        html.Li(children=[html.Strong("✉️ E-Mail: "), "yiferd@yahoo.fr"]),
                        html.Li(children=[html.Strong("💼 GitHub: "), html.A("github.com/Younes7777", href="https://github.com/Younes7777", target="_blank")]),
                        
                    ], className="list-unstyled fs-6")
                ]),
                className="shadow border-0 p-3 d-flex flex-column h-100"
            )
        ], md=5, className="d-flex")  # Stellt sicher, dass die Spalte sich dehnt

    ], className="mt-5 justify-content-center align-items-stretch")  # Sorgt für gleiche Höhe der Cards  # Sorgt für gleiche Höhe der Cards
    ], style={"position": "relative"}),

    html.Hr(),

     html.Div([
        dbc.Button(
            "Lebenslauf herunterladen",
            id="btn-download-pdf",
            color="primary",
            #style={"marginBottom": "20px"},
        ),
        dcc.Download(id="download-pdf")
    ], className="d-flex justify-content-center"),
    
    html.Hr(),

    html.Div([
        dbc.Button("Berufserfahrung", id="btn-beruf", color="primary", className="flex-grow-1"),
        dbc.Button("Studium", id="btn-studium", color="primary", className="flex-grow-1"),
        dbc.Button("Programmiersprachen", id="btn-it", color="primary", className="flex-grow-1"),
        dbc.Button("Machine Learning", id="btn-ml", color="primary", className="flex-grow-1"),
        dbc.Button("Microsoft Azure", id="btn-azure", color="primary", className="flex-grow-1"),
        dbc.Button("Power BI", id="btn-sprachen", color="primary", className="flex-grow-1"),
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

@dash.callback(
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
        return html.Div(berufserfahrung_inhalt, id="content-beruf", className="content-section")  # Standard: Berufserfahrung
    
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    sections = {
        "btn-beruf": html.Div(berufserfahrung_inhalt, id="content-beruf", className="content-section"),
        "btn-studium": html.Div(Studium, id="content-studium", className="content-section"),
        "btn-it": html.Div(Programmiersprachen, id="content-it", className="content-section"),
        "btn-ml": html.Div(ML, id="content-ml", className="content-section"),
        "btn-azure": html.Div(azure, id="content-azure", className="content-section"),
        "btn-sprachen": html.Div(Power_BI, id="content-sprachen", className="content-section")
    }
    
    return sections.get(button_id, "")

@dash.callback(
    Output("download-pdf", "data"),
    Input("btn-download-pdf", "n_clicks"),
    prevent_initial_call=True
)
def download_pdf(n_clicks):
    pdf_path = os.path.join(os.getcwd(), "assets", "Lebenslauf.pdf")  # Absoluter Pfad
    return dcc.send_file(pdf_path)


