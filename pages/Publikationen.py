import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

publikationen = [
    {"Erscheinungsjahr": 2018, "Titel": "External search strategies: The role of innovation objectives and specialization",
     "Auftragsgeber": "Strategisches Eigenforschungsprojekt", "Link": "https://publica.fraunhofer.de/entities/publication/b8c6675a-e1b4-462e-bd0d-ec6a7c7a7a7d/fullmeta"},
    {"Erscheinungsjahr": 2017, "Titel": "Governing innovation projects in firms",
     "Auftragsgeber": "Strategisches Eigenforschungsprojekt", "Link": "https://publica.fraunhofer.de/entities/publication/c489b681-14a5-46d7-bf41-84468d2973bf/fullmeta"},
    {"Erscheinungsjahr": 2018, "Titel": "Innovationen in der deutschen Wirtschaft. Indikatorenbericht zur Innovationserhebung 2017",
     "Auftragsgeber": "BMBF", "Link": "https://publica.fraunhofer.de/entities/publication/5f844293-23cb-45c6-95bf-db5d6b34e38c"},
    {"Erscheinungsjahr": 2018, "Titel": "Monitoring the Evolution and Benefits of Responsible Research and Innovation.",
     "Auftragsgeber": "EU", "Link": "https://op.europa.eu/en/publication-detail/-/publication/9072be49-c06c-11e8-9893-01aa75ed71a1/language-en"},
    {"Erscheinungsjahr": 2017, "Titel": "Innovationsverhalten der deutschen Wirtschaft. Indikatorenbericht zur Innovationserhebung 2016",
     "Auftragsgeber": "BMBF", "Link": "http://ftp.zew.de/pub/zew-docs/mip/16/mip_2016.pdf"},
    {"Erscheinungsjahr": 2016, "Titel": "Innovationsverhalten der deutschen Wirtschaft. Indikatorenbericht zur Innovationserhebung 2015",
     "Auftragsgeber": "BMBF", "Link": "http://www.zew.de/fileadmin/FTP/mip/15/mip_2015.pdf"},
    {"Erscheinungsjahr": 2016, "Titel": "Dokumentation zur Innovationserhebung 2015",
     "Auftragsgeber": "", "Link": "https://www.econstor.eu/handle/10419/127427"},
    {"Erscheinungsjahr": 2015, "Titel": "Determinanten der innovationsinduzierten Dienstleistungsproduktivität",
     "Auftragsgeber": "BMBF", "Link": "https://doi.org/10.24406/publica-fhg-240529"},
    {"Erscheinungsjahr": 2015, "Titel": "Innovationsverhalten der deutschen Wirtschaft. Indikatorenbericht zur Innovationserhebung 2014",
     "Auftragsgeber": "BMBF", "Link": "http://www.zew.de/fileadmin/FTP/mip/14/mip_2014.pdf"},
]

dash.register_page(__name__, order=1)

def layout():
    return dbc.Row([
        dbc.Col([
            html.Br(),
            dbc.Row(
                [ 
                    # Dynamisch Cards für jede Publikation
                    *[
                        dbc.Col(
                            dbc.Card(
                                dbc.CardBody([
                                    html.H5(pub["Titel"], className="card-title"),
                                    html.P(f"📅 Erscheinungsjahr: {pub['Erscheinungsjahr']}", className="text-muted"),
                                    html.P(f"💼 Auftragsgeber: {pub['Auftragsgeber']}", className="text-muted"),
                                    html.A("Öffnen", href=pub["Link"], target="_blank", className="btn btn-primary")
                                ]),
                                className="h-100"  # Setzt die Höhe jeder Card auf 100%
                            ),
                            md=4,  # Drei Cards nebeneinander
                            className="mb-4"
                        ) for pub in publikationen
                    ]
                ]
            ),
        ], width=12)
    ], justify='start')
