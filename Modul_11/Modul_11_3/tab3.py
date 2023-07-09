from dash import html
from dash import dcc
import plotly.graph_objects as go

def render_tab(df):
    # Grupowanie danych sprzedażowych według kanałów sprzedaży i dni tygodnia
    grouped = df.groupby(['Store_type', df['tran_date'].dt.day_name()])['total_amt'].sum().reset_index()

    # Tworzenie wykresu słupkowego dla każdego kanału sprzedaży
    bar_data = []
    for store_type in grouped['Store_type'].unique():
        store_data = grouped[grouped['Store_type'] == store_type]
        bar_data.append(go.Bar(x=store_data['tran_date'], y=store_data['total_amt'], name=store_type))

    # Ustawienia układu Dash
    layout = html.Div([
        html.H1('Sprzedaż według kanałów sprzedaży', style={'text-align': 'center'}),
        dcc.Graph(id='bar-sales-store-type', figure={'data': bar_data}),
    ])

    return layout