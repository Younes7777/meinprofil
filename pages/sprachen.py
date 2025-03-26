from dash import dcc, html
import dash_bootstrap_components as dbc

Power_BI= [
    dbc.Row([
            dbc.Col([
                dcc.Markdown('**Datenvisualisierung & Dashboards**',
                            style={'textAlign': 'center'})
            ], width=2),
            dbc.Col([
                
                html.Ul([
                    
                            html.Ul([
                                html.Li(
                                    dcc.Markdown('Entwicklung interaktiver Power BI-Dashboards für datengetriebene Entscheidungsfindung')),
                                html.Li(
                                    dcc.Markdown('Erstellung von ansprechenden Berichten mit Visualisierungen wie Karten, Diagrammen und KPI-Widgets')),
                                html.Li(
                                    dcc.Markdown('Nutzung von Bookmarks, Drillthrough & Tooltips für intuitive Benutzerführung')),
                                        ]),               
                ]),

                

                

            ], width=5)
        ], justify='center'),

    dbc.Row([
            dbc.Col([
                dcc.Markdown('**Datenmodellierung & DAX**',
                            style={'textAlign': 'center'})
            ], width=2),
            dbc.Col([
                
                html.Ul([
                    
                            html.Ul([
                                html.Li(
                                    dcc.Markdown('Erstellung komplexer Datenmodelle mit Relationen, Hierarchien und aggregierten Kennzahlen')),
                                html.Li(
                                    dcc.Markdown('Beherrschung von DAX (Data Analysis Expressions) zur Berechnung dynamischer Metriken und KPIs')),
                                html.Li(
                                    dcc.Markdown('Optimierung der Performance durch effiziente DAX-Funktionen und Star-Schema-Design')),
                                        ]),               
                ]),   

            ], width=5)
        ], justify='center'),

    dbc.Row([
            dbc.Col([
                dcc.Markdown('**Datenverarbeitung & Power Query (M)**',
                            style={'textAlign': 'center'})
            ], width=2),
            dbc.Col([
                
                html.Ul([
                    
                            html.Ul([
                                html.Li(
                                    dcc.Markdown('Datenbereinigung, Transformation und ETL mit Power Query (M)')),
                                html.Li(
                                    dcc.Markdown('Verbindung mit verschiedenen Datenquellen (SQL, Excel, APIs, Cloud-Datenbanken)')),
                                html.Li(
                                    dcc.Markdown('Erstellung automatisierter Datenpipelines zur Aktualisierung und Integration großer Datensätze')),
                                        ]),               
                ]),   

            ], width=5)
        ], justify='center'),

    dbc.Row([
            dbc.Col([
                dcc.Markdown('**Datenintegration & Konnektivität**',
                            style={'textAlign': 'center'})
            ], width=2),
            dbc.Col([
                
                html.Ul([
                    
                            html.Ul([
                                html.Li(
                                    dcc.Markdown('Anbindung von Power BI an SQL-Datenbanken, SharePoint, Azure, APIs und externe Datenquellen')),
                                html.Li(
                                    dcc.Markdown('Verwendung von DirectQuery, Import-Modus und Composite Models für optimierte Leistung')),
                                html.Li(
                                    dcc.Markdown('Implementierung von Row-Level Security (RLS) zur Steuerung des Datenzugriffs')),
                                        ]),               
                ]),   

            ], width=5)
        ], justify='center'),

        dbc.Row([
            dbc.Col([
                dcc.Markdown('**Berichtspublikation & Automatisierung**',
                            style={'textAlign': 'center'})
            ], width=2),
            dbc.Col([
                
                html.Ul([
                    
                            html.Ul([
                                html.Li(
                                    dcc.Markdown('Veröffentlichung von Berichten im Power BI Service mit regelmäßigen Datenaktualisierungen')),
                                html.Li(
                                    dcc.Markdown('Nutzung von Power Automate zur Automatisierung von Workflows (z. B. E-Mail-Benachrichtigungen)')),
                                html.Li(
                                    dcc.Markdown('Zusammenarbeit mit Power Apps zur Erstellung interaktiver, dynamischer Anwendungen')),
                                        ]),               
                ]),   

            ], width=5)
        ], justify='center'),

            
]