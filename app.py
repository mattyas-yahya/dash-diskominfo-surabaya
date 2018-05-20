import pandas_datareader.data as web
import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

app = dash.Dash()

keluhan = pd.read_csv("data/keluhan.csv", parse_dates=True, index_col="Tanggal")
bulanan = keluhan.resample("M").sum()
print(bulanan)

app.layout = html.Div(children=[
    html.H1(children='Jumlah Keluhan Terdata pada Diskominfo Surabaya'),

    dcc.Graph(
        id='graph',
        figure={
            'data': [
                {'x': bulanan.index, 'y': bulanan["Keluhan"], 'type': 'line', 'name': 'Diskominfo Surabaya'},
            ]
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)