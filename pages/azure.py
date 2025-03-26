from dash import dcc, html
import dash_bootstrap_components as dbc

azure = [
    dbc.Row([
        dbc.Col([
            dcc.Markdown('**Cloud-Datenlösungen**',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    dcc.Markdown('**Azure Blob Storage**')),
                        html.Ul([
                            html.Li(
                                dcc.Markdown('Skalierbarer Objektspeicher für strukturierte & unstrukturierte Daten')),
                            html.Li(
                                dcc.Markdown('Integration mit Azure Data Factory, Databricks & MLflow')),
                            html.Li(
                                dcc.Markdown('Sicherer Zugriff mit Managed Identities & Shared Access Signatures (SAS)')),
                                    ]),               
            ]),

            html.Ul([
                html.Li(
                    dcc.Markdown('**Azure Data Factory (ADF)**')),
                        html.Ul([
                            html.Li(
                                dcc.Markdown('ETL & ELT Pipelines für Big Data-Workloads')),
                            html.Li(
                                dcc.Markdown('Integration mit SQL Server, Blob Storage, Synapse Analytics & Power BI')),
                            
                                    ]),               
            ]),

        ], width=5)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('**Automatisierung & Serverless Computing**',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    dcc.Markdown('**Azure Functions (Python)**')),
                        html.Ul([
                            html.Li(
                                dcc.Markdown('Event-gesteuerte serverlose Funktionen für Datenverarbeitung')),
                            html.Li(
                                dcc.Markdown('Trigger für Blob Storage, Service Bus & HTTP Requests')),
                            
                                    ]),               
            ]),

            html.Ul([
                html.Li(
                    dcc.Markdown('**Azure Logic Apps**')),
                        html.Ul([
                            html.Li(
                                dcc.Markdown('No-Code/Low-Code-Workflows zur Automatisierung von Geschäftsprozessen')),
                            html.Li(
                                dcc.Markdown('Integration mit Outlook, SharePoint, SQL, Dynamics 365, APIs & Webhooks')),
                            
                                    ]),               
            ]),

        ], width=5)
    ], justify='center')
]