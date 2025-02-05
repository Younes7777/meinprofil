import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_table

publikationen = [
    {"Erscheinungsjahr": 2018, "Titel": "The role of innovation objectives and specialization","Auftragsgeber":"Strategisches Eigenforschungsprojekt", "Link": "[Öffnen](https://publica.fraunhofer.de/entities/publication/b8c6675a-e1b4-462e-bd0d-ec6a7c7a7a7d/fullmeta)"},
    {"Erscheinungsjahr": 2017, "Titel": "Governing innovation projects in firms","Auftragsgeber":"Strategisches Eigenforschungsprojekt", "Link": "[Öffnen](https://publica.fraunhofer.de/entities/publication/c489b681-14a5-46d7-bf41-84468d2973bf/fullmeta)"},
    {"Erscheinungsjahr": 2018, "Titel": "Innovationen in der deutschen Wirtschaft. Indikatorenbericht zur Innovationserhebung 2017","Auftragsgeber":"Bundesministerium für Bildung und Forschung - BMBF", "Link": "[Öffnen](https://ftp.zew.de/pub/zew-docs/mip/17/mip_2017.pdf)"},
    {"Erscheinungsjahr":2018, "Titel": "Monitoring the Evolution and Benefits of Responsible Research and Innovation.\nReport on the researchers' survey. Annex 2: Statistical analysis","Auftragsgeber":"EU", "Link": "[Öffnen](https://op.europa.eu/en/publication-detail/-/publication/9072be49-c06c-11e8-9893-01aa75ed71a1/language-en)"},
    {"Erscheinungsjahr":2017, "Titel": "Innovationsverhalten der deutschen Wirtschaft. Indikatorenbericht zur Innovationserhebung 2016","Auftragsgeber":"Bundesministerium für Bildung und Forschung - BMBF", "Link": "[Öffnen](http://ftp.zew.de/pub/zew-docs/mip/16/mip_2016.pdf)"},
    {"Erscheinungsjahr":2016, "Titel": "Innovationsverhalten der deutschen Wirtschaft. Indikatorenbericht zur Innovationserhebung 2015","Auftragsgeber":"Bundesministerium für Bildung und Forschung - BMBF", "Link": "[Öffnen](http://www.zew.de/fileadmin/FTP/mip/15/mip_2015.pdf)"},
    {"Erscheinungsjahr":2016, "Titel": "Dokumentation zur Innovationserhebung 2015","Auftragsgeber":"", "Link": "[Öffnen](https://www.econstor.eu/handle/10419/127427)"},
    {"Erscheinungsjahr":2015, "Titel": "Determinanten der innovationsinduzierten Dienstleistungsproduktivität","Auftragsgeber":"Bundesministerium für Bildung und Forschung - BMBF", "Link": "[Öffnen](https://doi.org/10.24406/publica-fhg-240529)"},
    {"Erscheinungsjahr":2015, "Titel": "Innovationsverhalten der deutschen Wirtschaft. Indikatorenbericht zur Innovationserhebung 2014","Auftragsgeber":"Bundesministerium für Bildung und Forschung - BMB", "Link": "[Öffnen](http://www.zew.de/fileadmin/FTP/mip/14/mip_2014.pdf)"},
    
   
]

dash.register_page(__name__, order=2)
green_text = {'color':'green'}
def layout():
    
    return dbc.Row([
        dbc.Col([
         html.Br(),   
        dash_table.DataTable(
            columns=[
                {"name": "Erscheinungsjahr", "id": "Erscheinungsjahr"},
                {"name": "Titel", "id": "Titel"},
                {"name": "Auftragsgeber", "id": "Auftragsgeber"},
                {"name": "Link", "id": "Link", "presentation": "markdown"},
            ],
            data=publikationen,
            style_table={'width': '100%'},
            style_header={'backgroundColor': 'lightgrey', 'fontWeight': 'bold'},
            style_cell={'textAlign': 'left', 'padding': '3px', 'fontSize': '12px', 'whiteSpace': 'normal','height': 'auto'},
            style_cell_conditional=[
                    {'if': {'column_id': 'Titel'}, 'width': '200px'},  # Engere Spalte für den Titel
            ]
        )
    
        ], width={'size':12, 'offset':0})
], justify='start')