from flask import Flask, request
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd


app = Dash(__name__)
server = app.server

df = pd.DataFrame({
    "Quem pediu": ["mv", "camila", "mv", "camila", "mv", "camila"],
    "nº de pedidos": [3, 1, 0.01, 1, 3, 0.01],
    "Filtro": ["Pedidos", "Pedidos", "Aceitos", "Aceitos", "Negados", "Negados"]
})

fig = px.bar(df, x="Quem pediu", y="nº de pedidos", color="Filtro", barmode="group")


app.layout = html.Div(children=[
    html.H1(children='Análise dos pedidos de namoro'),

    html.Div(children='''
        Gráfico referente aos pedidos aceitos e negados
    '''),

    html.Div(children='''
        Pelas minhas contas tá contabilizado assim (eu sei q vc pediu mais doq isso mas ja tava mt feio p vc
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),

    html.Div(children='''
        Quem sabe vc seja vitoriosa no de casamento
    ''')
])

if __name__ == '__main__':
    app.run_server(debug=True)