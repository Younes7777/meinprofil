import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

sprachen= [
    dbc.Row([
        dbc.Col([
            dcc.Markdown('**Deutsch**', style={'textAlign': 'center'})
        ], width=2),
    
        dbc.Col([
            dcc.Markdown('Fließend in Wort und Schrift',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            
        ], width=5),

        

    ], justify='center'),

    

    dbc.Row([
        dbc.Col([
            dcc.Markdown('**Englisch**', style={'textAlign': 'center'})
        ], width=2),
    
        dbc.Col([
            dcc.Markdown('Gut',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            
        ], width=5),

        

    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('**Französisch**', style={'textAlign': 'center'})
        ], width=2),
    
        dbc.Col([
            dcc.Markdown('Verhandlungssicher',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            
        ], width=5),

        

    ], justify='center'),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('**Arabisch**', style={'textAlign': 'center'})
        ], width=2),
    
        dbc.Col([
            dcc.Markdown('Muttersprache',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            
        ], width=5),

        

    ], justify='center')
]