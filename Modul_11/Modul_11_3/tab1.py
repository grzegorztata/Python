from dash import html
from dash import dcc
import plotly.graph_objects as go

# Sprzedaż globalna (tab1)

def render_tab(df):

    # DatePickerRange jest widgetem dcc
    # Nadajemy widgetowi unikalne id, datę początkową, datę końcową oraz format daty
    # Na końcu tworzymy html.Div, w którym dodamy 2 wykresy umieszczone obok siebie
    layout = html.Div([html.H1('Sprzedaż globalna',style={'text-align':'center'}),
                        html.Div([dcc.DatePickerRange(id='sales-range',
                        start_date=df['tran_date'].min(),
                        end_date=df['tran_date'].max(),
                        display_format='YYYY-MM-DD')],style={'width':'100%','text-align':'center'}),
                        html.Div([html.Div([dcc.Graph(id='bar-sales')],style={'width':'50%'}),
                        html.Div([dcc.Graph(id='choropleth-sales')],style={'width':'50%'})],style={'display':'flex'})
                        ])

    return layout