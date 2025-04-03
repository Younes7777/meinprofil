from dash import dcc, html
import dash_bootstrap_components as dbc

berufserfahrung_inhalt = [

    dbc.Row([
        dbc.Col([
            dcc.Markdown('**12/2024 - 03/2025**', style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('**Weiterbildung zum Cloud Data Analyst (remote)**\n'
                         'Brainymation AG, München',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li('Moderne Data Analyse mit SQL-Server'),
                html.Li('Power BI Basics und Advanced'),
                html.Li('PL-300T00: Microsoft Power BI Data Analyst'),
                html.Li('DP-900 Praxis: Microsoft Azure Data Fundamentals'),
            ])
        ], width=5)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('**02/2022 - 09/2024**', style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('**IT Data Analyst**\n'
                         'Deutsche Giganetz GmbH, Hamburg',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li('Zuverlässige Entwicklung von Anwendungen und Tools unter Verwendung von Python (Dash) und R (Shiny)'),
                html.Li('Ad-Hoc SQL-Analysen'),
                html.Li('Machine Learning-Implementierung und Evaluation in Python-scikit-learn'),
            ])
        ], width=5)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('**06/2018 - 12/2021**', style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('**Data Analyst**\n'
                         'BetoCall, Marrakesch (Marokko)',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li('Datenextraktion und-aufbereitung aus verschiedenen Quellen'),
                html.Li('Anwendung von statistischen Methoden zur Identifikation von Trends, Mustern und Zusammenhängen in den Daten'),
            ])
        ], width=5)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('**05/2020 - 08/2020**', style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('**Trainee Data Science (remote)**\n'
                         'neuefische GmbH, Hamburg',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li('Intensive-Coding-Bootcamp in Vollzeit (540 Stunden)'),
                html.Li('Fundierte Programmierpraxis in Python mit Eigenentwicklung eines Projektes als Abschlussarbeit (digitales Gesellenstück) sowie 2 weiteren Machine Learning-Projekten'),
            ])
        ], width=5)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('**07/2013 - 05/2018**', style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('**Wissenschaftlicher Mitarbeiter**\n'
                         'Das Fraunhofer-Institut für System- und Innovationsforschung ISI',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li('Eigenständige Aufbereitung wissenschaftlicher Daten sowie Programmierung in Stata, R und SPSS'),
                html.Li('Statistische und ökonometrische Datenanalyse'),
                html.Li('Verfassen von Projektberichten und Publikationen'),
            ])
        ], width=5)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('**01/2012 - 05/2013**', style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('**Mitarbeiter im Bereich der statistischen Datenanalyse und Prognose**\n'
                         'Analytix GmbH, Kiel',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li('Gewissenhafte Aufbereitung wissenschaftlicher Daten sowie Programmierung in SPSS und VBA'),
                html.Li('Ökonometrische Analyse von Querschnitts- und Paneldatenn mit dem Ziel, Prognosen für die Fachkräfteentwicklung zu erstellen'),
            ])
        ], width=5)
    ], justify='center')
]


