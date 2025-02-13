import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

azure = [
    dbc.Row([
        dbc.Col([
            dcc.Markdown('**Cloud-Datenlösungen und Automatisierung**',
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
    ], justify='center')
]