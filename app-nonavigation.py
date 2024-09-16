from dash import Dash, html, dcc, callback, Input, Output
import numpy as np 
import pandas as pd 
import plotly.express as px
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.PULSE])
app.title = "MCM7183 Exercise 3"
server = app.server

df = pd.read_csv("https://raw.githubusercontent.com/wenjiun/MCM7183Exercise3/main/assets/gdp_1960_2020.csv")

image_path = 'https://raw.githubusercontent.com/wenjiun/MCM7183Exercise3/main/assets/logo-mmu.png'

app.layout = dbc.Container([dbc.Row([
dbc.Col(html.H1('MCM7183 Exercise 3', className="p-2 bg-light border text-center"),  width=10), 
dbc.Col(html.Img(src=image_path, className="m-2"))]), 
dbc.Row(dbc.Col(dcc.Dropdown(['Malaysia', 'Indonesia', 'China'], 'Malaysia', id='dropdown-country'), width={"size": 4, "offset": 4})), 
dbc.Row(dcc.Graph(id="graph-scatter"), className="mb-4 border-bottom border-5"), 
dbc.Row(dbc.Col(dcc.Slider(1960, 2020, 5, value=2020, id='slider-year',
                         marks = {i: str(i) for i in range(1960, 2021, 5)}), width={"size": 10, "offset": 1}), className="mt-5"), 
dbc.Row(dcc.Graph(id="graph-pie"))])

@callback(
    Output('graph-scatter', 'figure'),
    Output('graph-pie', 'figure'),
    Input('dropdown-country', 'value'),
    Input('slider-year', 'value')
)
def update_graph(country_selected, year_selected):
    subset_Country = df[df['country'].isin([country_selected])]
    fig = px.scatter(subset_Country, x="year", y="gdp")

    subset_Year = df[df['year'].isin([year_selected])]
    subset_Year_Asia = subset_Year[subset_Year['state'].isin(["Asia"])]
    subset_Year_Africa = subset_Year[subset_Year['state'].isin(["Africa"])]
    subset_Year_America = subset_Year[subset_Year['state'].isin(["America"])]
    subset_Year_Europe = subset_Year[subset_Year['state'].isin(["Europe"])]
    subset_Year_Oceania = subset_Year[subset_Year['state'].isin(["Oceania"])]
    pie_data = [sum(subset_Year_Asia['gdp']),sum(subset_Year_Africa['gdp']),sum(subset_Year_America['gdp']),sum(subset_Year_Europe['gdp']),sum(subset_Year_Oceania['gdp'])];
    mylabels = ["Asia", "Africa", "America", "Europe","Oceania"]
    pie_df = {'Continent': mylabels,'GDP': pie_data}
    fig2 = px.pie(pie_df,values="GDP",names="Continent")
    fig2.update_traces(sort=False) 

    return fig, fig2




if __name__ == '__main__':
    app.run(debug=True)
