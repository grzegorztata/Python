from dash import html
from dash import dcc
import plotly.graph_objects as go

def render_tab(df):

    # Wykres kołowy ze strukturą sprzedaży wg podstawowych grup produktów jest statyczny i nie zależy od żadnego innego widgetu.
    # Z tego powodu będziemy mogli stworzyć go w tym samym miejscu, co layout.
    
    # df[df['total_amt']>0] - wybieramy wiersze z 'df' gdzie wartość 'total_amt' jest większa od 0
    # Grupujemy wybrane wiersze według kolumny 'prod_cat' i sumujemy wartości w kolumnie 'total_amt'
    # Tworzymy wykres kołowy Pie
    # Dane do wykresu przekazywane są poprzez argumenty 'labels' i 'values' funkcji 'go.Pie'
    
    grouped = df[df['total_amt']>0].groupby('prod_cat')['total_amt'].sum()
    fig = go.Figure(data=[go.Pie(labels=grouped.index,values=grouped.values)],layout=go.Layout(title='Udział grup produktów w sprzedaży'))

    layout = html.Div([html.H1('Produkty',style={'text-align':'center'}),

                        # Kontener główny zawiera 2 podkontenery html.Div ułożone obok siebie
                        # Ustawienie stylu 'display':'flex' oznacza, że elementy w tych podkontenerach będą ułożone w linii poziomej
                        # pierwszym wykresem będzie wykres kołowy, który został utworzony w zmiennej 'fig'. 'Figure' oznacza wizualizację danych
                        html.Div([html.Div([dcc.Graph(id='pie-prod-cat',figure=fig)],style={'width':'50%'}),
                        html.Div([dcc.Dropdown(id='prod_dropdown',
                                    options=[{'label':prod_cat,'value':prod_cat} for prod_cat in df['prod_cat'].unique()],
                                    value=df['prod_cat'].unique()[0]),
                                    dcc.Graph(id='barh-prod-subcat')],style={'width':'50%'})],style={'display':'flex'}),
                                    html.Div(id='temp-out')
                        ])

    return layout