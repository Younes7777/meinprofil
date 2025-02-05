import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/', order=0)

# resume sample template from https://zety.com/
layout = html.Div([
    html.Img(src="/assets/my.jpg", className="hero-image", style={"width": "100%", "height": "auto"}),
    html.Br(),
    dcc.Markdown('# Younes Iferd', style={'textAlign':'center'}),
    dcc.Markdown('Geboren am 09. Febraur 1977 in Rabat (Marokko)', style={'textAlign':'center'}),
    dcc.Markdown('Verheiratet und Vater eines achtjährigen Sohnes', style={'textAlign': 'center'}),
    

    dcc.Markdown('### Kurzprofil', style={'textAlign': 'center'}),
    html.Hr(),
    dcc.Markdown('Leidenschaftlicher Data Analyst mit Erfahrung in der statistischen und ökonometrischen Datenanalyse. \n'
                 'Versiert in diversen Programmiersprachen und analytischen Methoden. Ein hilfsbereiter Teamplayer \n'
                 'mit einem lösungsorientierten Ansatz zur Dateninterpretation und Entscheidungsfindung.',
                 style={'textAlign': 'center', 'white-space': 'pre'}),

    dcc.Markdown('### Berufserfahrung', style={'textAlign': 'center'}),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('02/2022 - 09/2024', style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('IT Data Analyst \n'
                         'Deutsche Giganetz GmbH, Hamburg',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li('Zuverlässige Entwicklung von Anwendungen und Tools unter Verwendung vonPython (Dash) und R (Shiny)'),
                html.Li('Ad-Hoc SQL-Analysen'),
                html.Li('Machine Learning-Implimentierung und Evaluation in Python-scikit-learn'),
                
            ])
        ], width=5)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('06/2018 to 12/2021',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Data Analyst \n'
                         'BetoCall, Marrakesch (Marokko)',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    'Datenextraktion und-aufbereitung aus verschiedenen Quellen'),
                html.Li(
                    'Anwendung von statistischen Methoden zur Identifikation von Trends, Mustern und Zusammenhängen in den Daten'),
            ])
        ], width=5)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('05/2020 to 08/2020',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Traine Data Science (remote) \n'
                         'neuefische GmbH, Hamburg',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    'Intensive-Coding-Bootcamp in Vollzeit (540 Stunden)'),
                html.Li(
                    'Fundierte Programmierpraxis in Python mit Eigenentwicklung eines Projektes als Abschlussarbeit (digitales Gesellenstück) sowie 2 weiteren Machine Learning-Projekten'),
               
            ])
        ], width=5)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('07/2013 - 05/2018', style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Wissenschaftlicher Mitarbeiter \n'
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
            dcc.Markdown('01/2012 to 05/2013',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Mitarbeiter im Bereich der statistischen Datenanalyse und Prognose \n'
                         'Analytix GmbH, Kiel',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    'Gewissenhafte Aufbereitung wissenschaftlicher Daten sowie Programmierung in SPSS und VBA'),
                html.Li(
                    'Ökonometrische Analyse von Querschnitts- und Paneldatenn mit dem Ziel, Prognosen für die Fachkräfteentwicklung zu erstellen'),
               
            ])
        ], width=5)
    ], justify='center'),

    dcc.Markdown('### Studium', style={'textAlign': 'center'}),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('10/2003 – 12/2011',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Studium der Volkswirtschaftslehre mit Schwerpunkt Quantitative Wirtschaftsforschung und Nebenfach Wirtschaftsinformatik\n'
                         'Christian-Albrechts-Universität zu Kiel, Kiel',
                         style={'white-space': 'pre'},
                         className='ms-3'),
        ], width=5)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('01/1997 – 06/2001',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Studium der Wirtschaftswissenschaften mit Schwerpunkt Betriebswirtschaft\n'
                         'Christian-Albrechts-Universität zu Kiel, Kiel',
                         style={'white-space': 'pre'},
                         className='ms-3'),
        ], width=5)
    ], justify='center'),


    dcc.Markdown('### IT-Kenntnisse', style={'textAlign': 'center'}),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('Python', style={'textAlign': 'center'})
        ], width=2),
    
        dbc.Col([
            dcc.Markdown('Sehr gute Kenntnisse',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            
        ], width=5),

        

    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('R', style={'textAlign': 'center'})
        ], width=2),
    
        dbc.Col([
            dcc.Markdown('Gute Kenntnisse',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            
        ], width=5),

        

    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('SQL', style={'textAlign': 'center'})
        ], width=2),
    
        dbc.Col([
            dcc.Markdown('Sehr gute Kenntnisse',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            
        ], width=5),

        

    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('SPSS', style={'textAlign': 'center'})
        ], width=2),
    
        dbc.Col([
            dcc.Markdown('Sehr guze Kenntnisse',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            
        ], width=5),

        

    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('Stata', style={'textAlign': 'center'})
        ], width=2),
    
        dbc.Col([
            dcc.Markdown('Gute Kenntnisse',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            
        ], width=5),

        

    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('MS Office', style={'textAlign': 'center'})
        ], width=2),
    
        dbc.Col([
            dcc.Markdown('Gute Kenntnisse',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            
        ], width=5),

        

    ], justify='center'),


    dcc.Markdown('### Machine Learning-Algorithmen mit Python-Scikit-learn', style={'textAlign': 'center'}),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('Supervised Learning',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    'Lineare Regression'),
                html.Li(
                    'Entscheidungsbäume'),
                html.Li(
                    'Random Forest'),
                html.Li(
                    'XGBoost'), 
                html.Li(
                'Catboost'),    
              
            ])
        ], width=5)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('Unsupervised Learning',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    'K-Means Clustering'),
                html.Li(
                    'Hierarchisches Clustering'),
                html.Li(
                    'Principal Component Analysis (PCA)'),
                  
              
            ])
        ], width=5)
    ], justify='center'),



    dcc.Markdown('### Microsoft Azure', style={'textAlign': 'center'}),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('Cloud-Datenlösungen und Automatisierung',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    'Azure Blob Storage'),
                html.Li(
                    'Azure Functions (Python)'),
                html.Li(
                    'Azure Data Factory'),
                    html.Li(
                    'Azure Logic Apps'),
                  
              
            ])
        ], width=5)
    ], justify='center'),

    dcc.Markdown('### Sprachen', style={'textAlign': 'center'}),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('Deutsch', style={'textAlign': 'center'})
        ], width=2),
    
        dbc.Col([
            dcc.Markdown('Fließend in Wort und Schrift',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            
        ], width=5),

        

    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('Arabisch', style={'textAlign': 'center'})
        ], width=2),
    
        dbc.Col([
            dcc.Markdown('Muttersprache',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            
        ], width=5),

        

    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('Englisch', style={'textAlign': 'center'})
        ], width=2),
    
        dbc.Col([
            dcc.Markdown('Gut',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            
        ], width=5),

        

    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('Französisch', style={'textAlign': 'center'})
        ], width=2),
    
        dbc.Col([
            dcc.Markdown('Verhandlungssicher',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            
        ], width=5),

        

    ], justify='center'),

])
