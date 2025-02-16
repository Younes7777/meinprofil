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
                    dcc.Markdown('**Lineare Regression**: Lineare Regression, Ridge/Lasso Regression, Polynomial Regression')),
                html.Li(
                    dcc.Markdown('**Baum-basierte Algorithmen**: Entscheidungsbäume, Random Forest, Gradient Boosting (XGBoost, CatBoost, LightGBM)')),
                html.Li(
                   dcc.Markdown('**Support Vector Machines (SVM)**')),
                html .Li(
                    dcc.Markdown('**Ensemble Learning**: Bagging, Boosting, Stacking')),    
              
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
                    dcc.Markdown('**Clustering-Algorithmen**: K-Means, Hierarchisches Clustering, DBSCAN')),
                html.Li(
                    dcc.Markdown('**Dimensionalitätsreduktion**:  Principal Component Analysis (PCA), t-SNE, UMAP')),
                html.Li(
                    dcc.Markdown('Principal Component Analysis (PCA)')),
                  
              
            ])
        ], width=5)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('**Feature Engineering & Datenvorbereitung**',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    dcc.Markdown('Skalierung (StandardScaler, MinMaxScaler)')),
                html.Li(
                    dcc.Markdown('One-Hot-Encoding, Label Encoding')),
                html.Li(
                    dcc.Markdown('Umgang mit fehlenden Werten')),
                html.Li(
                    dcc.Markdown('Feature Selection & Extraction')),
            
                  
              
            ])
        ], width=5)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('**Modellbewertung & Optimierung**',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    dcc.Markdown('Kreuzvalidierung, Hyperparameter-Tuning (GridSearch, RandomizedSearch, Optuna)')),
                html.Li(
                    dcc.Markdown('Metriken für Klassifikation (AUC, F1-Score, Precision-Recall) & Regression (RMSE, MAE, R²)')),
                html.Li(
                    dcc.Markdown('Umgang mit fehlenden Werten')),
                html.Li(
                    dcc.Markdown('Feature Selection & Extraction')),
            ])
        ], width=5)
    ], justify='center'),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('**Programmierung & Tools**',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    dcc.Markdown('**Programmiersprachen**: Python (Pandas, NumPy, Scikit-Learn, TensorFlow, PyTorch)')),
                html.Li(
                    dcc.Markdown('**Datenvisualisierung**: Matplotlib, Seaborn, Plotly')),
                
            ])

            
        ], width=5)
    ], justify='center')
]