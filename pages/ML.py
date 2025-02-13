import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

ML= [
    dbc.Row([
        dbc.Col([
            dcc.Markdown('**Supervised Learning**',
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
            dcc.Markdown('**Unsupervised Learning**',
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
    ], justify='center')
]