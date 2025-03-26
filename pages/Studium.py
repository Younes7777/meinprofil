from dash import dcc, html
import dash_bootstrap_components as dbc

Studium= [
    dbc.Row([
            dbc.Col([
                dcc.Markdown('**10/2003 – 12/2011**',
                            style={'textAlign': 'center'})
            ], width=2),
            dbc.Col([
                dcc.Markdown('**Studium der Volkswirtschaftslehre**\n'
                            'Christian-Albrechts-Universität zu Kiel, Kiel',
                            style={'white-space': 'pre'},
                            className='ms-3'),
                html.Ul([
                    html.Li('Schwerpunkt: Quantitative Wirtschaftsforschung (Statistik und Ökonometrie)', style={'padding-left': '20px'}),
                    html.Li('Nebenfach: Wirtschaftsinformatik', style={'padding-left': '20px'}),
                    html.Li('Titel der Diplomarbeit: Overeducation als Hedginginstrument gegen Arbeitslosigkeitsrisiken', style={'padding-left': '20px'}),
                ])
            ], width=5)
        ], justify='center'),

        dbc.Row([
            dbc.Col([
                dcc.Markdown('**01/1997 – 06/2001**',
                            style={'textAlign': 'center'})
            ], width=2),
            dbc.Col([
                dcc.Markdown('**Studium der Wirtschaftswissenschaften mit Schwerpunkt Betriebswirtschaft**\n'
                            'Universität Mohamed 5 in Rabat (Marokko)',
                            style={'white-space': 'pre'},
                            className='ms-3'),
                html.Ul([
                    html.Li('Schwerpunkt: Betriebswirtschaft', style={'padding-left': '20px'}),
                    
                ])
            ], width=5)
        ], justify='center')
]