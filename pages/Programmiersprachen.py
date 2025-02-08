import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


Programmiersprachen= [
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

]