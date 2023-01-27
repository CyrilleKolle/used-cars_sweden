import dash
import os
from load_data import CarsData
from dash.dependencies import Output, Input
import plotly_express as px
import pandas as pd
from layout import Layout
import dash_bootstrap_components as dbc
from plotly.subplots import make_subplots
import plotly.graph_objects as go


directory_path = os.path.dirname(__file__)
path = os.path.join(directory_path, "carsdata")

cars_data = CarsData(path)
symbol_dict = {"used": "used"}

df = cars_data.cars_dataframe("used")

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[dict(name="viewport", content="width=device-width, initial-scale=1.0")],
)
app.layout = Layout(symbol_dict).layout()


@app.callback(
    Output("cleaned-data", "data"),
    Input("cars_dropdown", "value"),
)
def dataframe(car):
    df_used_cars = df[0]
    print(df_used_cars)
    return df_used_cars.to_json()


@app.callback(
    Output("fuel-types", "figure"),
    Input("cleaned-data", "data"),
)
def fuel_types(df):
    df = pd.read_json(df)
    df = (
        df.groupby(["fuel"])
        .agg({"model": "count"})
        .reset_index()
        .sort_values(by="model", ascending=False)
    )
    return px.pie(df, names="fuel", values="model", title="Fuel distribution among used cars in Sweden")


@app.callback(
    Output("top-dealers", "figure"),
    Input("cleaned-data", "data"),
)
def top_dealers(df):
    df = pd.read_json(df)
    df = (
        df.groupby(["provider"])
        .agg({"model": "count"})
        .reset_index()
        .sort_values(by="model", ascending=False)
    )
    df = df.head(10)
    return px.pie(df, names='provider', values='model', title='Top used car dealers in SSweden')

@app.callback(
    Output('yearly-new-car-emission','figure'),
    Input("cleaned-data", "data"),
    Input('year-range', 'value')
)
def yearly_car_emmission(df, slider_value):
    dff = pd.read_json(df)
    dff = dff.groupby(['entry_year']).agg({'co2_emission_g/km':'sum', 'model':'count'}).reset_index()
    dff = dff[(dff['entry_year'] >= slider_value[0]) & (dff['entry_year'] <= slider_value[1])]

    trace1 = px.bar(dff, x= "entry_year",
                    y='co2_emission_g/km')
    trace2 = px.bar(dff, x= "entry_year",
                    y='model')
    
    trace_list = [trace1, trace2]
    y_axis_titles = ["Co2 emission", "total amout of car registered"]

    fig = make_subplots(rows=1, cols=1)
        
    for i, (item, title) in enumerate(zip(trace_list, y_axis_titles)):
        fig.add_trace(go.Bar(name=title,
                                x=item.data[0]['x'], y=item.data[0]['y'], showlegend=True), row=1, col=1)
    fig.update_layout(title="Various countries`s individual medal", plot_bgcolor="rgba(255,255,255,0.9)")
    fig.update_xaxes(title="Medals")
    fig.update_yaxes(title_text="y-axis in logarithmic scale", type="log")
    return fig
if __name__ == "__main__":
    app.run(debug=True)
