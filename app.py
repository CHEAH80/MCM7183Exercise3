from dash import Dash, html
import numpy as np 
import pandas as pd 
import plotly.express as px

app = Dash(__name__)
server = app.server

df = pd.read_csv("https://raw.githubusercontent.com/wenjiun/MCM7183Exercise3/main/assets/gdp_1960_2020.csv")
subset_Malaysia = df[df['country'].isin(["Malaysia"])]
fig = px.scatter(subset_Malaysia, x="year", y="gdp")

image_path = 'assets/logo-mmu.png'

app.layout = [html.H1('MCM7183 Exercise 3'), html.Img(src=image_path), dcc.Graph(figure=fig)]

if __name__ == '__main__':
    app.run(debug=True)
