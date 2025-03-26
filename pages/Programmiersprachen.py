from dash import dcc, html
import dash_bootstrap_components as dbc


Programmiersprachen= [
    dbc.Row([
        dbc.Col([
            dcc.Markdown('**Python**', style={'textAlign': 'center'})
        ], width=2),
    
        dbc.Col([
            dcc.Markdown('',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    dcc.Markdown('**Dash & Web-Apps**: Entwicklung interaktiver Dash-Webanwendungen zur Datenvisualisierung und Analyse. Die Webseite, auf der Sie sich gerade befinden, habe ich ebenfalls mit Dash programmiert')), 
                html.Li(
                    dcc.Markdown('**Statistische Analyse & Machine Learning**: Anwendung statistischer Methoden und einfacher Machine-Learning-Modelle mit Scikit-Learn für Vorhersagen und Mustererkennung')),    
                html.Li(
                    dcc.Markdown('**Datenanalyse & -verarbeitung**: Umfangreiche Erfahrung mit Pandas und NumPy zur Datenbereinigung, Transformation und Aggregation')),
                html.Li(
                    dcc.Markdown('**Datenvisualisierung**: Erstellung aussagekräftiger Diagramme mit Matplotlib und Seaborn zur datengetriebenen Entscheidungsfindung')),
                html.Li(
                    dcc.Markdown('**SQL & Datenbankmanagement**: Abfrage und Analyse großer Datenmengen mit SQL (PostgreSQL, MySQL, SQLite) und Anbindung über SQLAlchemy')),
                
                html.Li(
                dcc.Markdown('**ETL & Automatisierung**: Entwicklung effizienter ETL-Pipelines für die Datenintegration aus verschiedenen Quellen (CSV, APIs, SQL-Datenbanken)')),    
              
            ])
        ], width=5)

        

    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('**R**', style={'textAlign': 'center'})
        ], width=2),
    
        dbc.Col([
            html.Ul([
                html.Li(
                        dcc.Markdown('**Shiny & Web-Apps**: Entwicklung interaktiver Shiny-Webanwendungen zur Datenvisualisierung und Analyse')),
                html.Li(
                        dcc.Markdown('**Datenanalyse & -verarbeitung**: Tiefgehende Erfahrung mit dplyr und tidyr zur effizienten Datenbereinigung, Transformation und Aggregation')), 
                html.Li(
                        dcc.Markdown('**Datenvisualisierung**: Erstellung aussagekräftiger Visualisierungen mit ggplot2 für explorative und erklärende Analysen')), 
                html.Li(
                        dcc.Markdown('**Statistische Analyse & Machine Learning**: Anwendung statistischer Methoden, Hypothesentests und Machine-Learning-Modelle mit caret und randomForest')), 
                html.Li(
                        dcc.Markdown('**Datenautomatisierung & Berichte**: Entwicklung automatisierter Reports mit RMarkdown und Shiny zur dynamischen Präsentation von Analyseergebnissen')), 
            ])
        ], width=5),

        

    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('**SQL**', style={'textAlign': 'center'})
        ], width=2),
    
        dbc.Col([
            html.Ul([
                html.Li(
                        dcc.Markdown('**Datenabfrage & -manipulation**: Umfangreiche Erfahrung in der Abfrage und Manipulation großer Datenmengen mit SQL (z. B. JOINs, Subqueries, Aggregationen)')),
                html.Li(
                        dcc.Markdown('**Datenmodellierung**: Entwurf und Verwaltung relationaler Datenbanken sowie Erstellung effizienter Datenmodelle und Indizes')), 
                html.Li(
                        dcc.Markdown('**Datenbereinigung & -transformation***: Nutzung von SQL-Funktionen zur Bereinigung, Transformation und Aggregation von Daten für die Analyse')), 
                
            ])
            
        ], width=5),

        

    ], justify='center'),

    

]