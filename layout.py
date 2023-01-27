from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd


class Layout:
    def __init__(self, symbol_dict: dict) -> None:
        self._symbol_dict = symbol_dict

        self._cars_dropdown = [
            {"label": name, "value": symbol} for symbol, name in symbol_dict.items()
        ]

    def layout(self):
        return dbc.Container(
            [
                dbc.Card(
                    dbc.CardBody(html.H1("Used cars in Sweden")), className="mt-5"
                ),
                dbc.Row(
                    dcc.Dropdown(
                        id="cars_dropdown", options=self._cars_dropdown, value="used"
                    ),
                ),
                dbc.Row(
                    children=[
                        dbc.Col(
                            [
                                dbc.Card(
                                    dbc.CardBody(
                                        children=[
                                            dbc.Col([dcc.Graph(id="fuel-types")]),
                                        ],
                                    )
                                ),
                            ]
                        ),
                        dbc.Col(
                            [
                                dbc.Card(
                                    dbc.CardBody(
                                        children=[
                                            dbc.Col([dcc.Graph(id="top-dealers")]),
                                        ],
                                    )
                                ),
                            ]
                        ),
                    ]
                ),
                dbc.Row(
                    dbc.Card(
                        className="",
                        children=[
                            dbc.CardBody(
                                className="",
                                children=[
                                    dcc.Graph(
                                        id="yearly-new-car-emission",
                                    ),
                                ],
                            )
                        ],
                    )
                ),
                dbc.Row(
                    dbc.Card(
                        className="",
                        children=[
                            dbc.CardBody(
                                className="",
                                children=[
                                    dcc.RangeSlider(
                                        id="year-range",
                                        min=1896,
                                        max=2016,
                                        step=2,
                                        marks=None,
                                        value=[
                                            1900,
                                            2040,
                                        ],
                                        tooltip={
                                            "placement": "bottom",
                                            "always_visible": True,
                                        },
                                    ),
                                ],
                            )
                        ],
                    )
                ),
                dcc.Store(id="cleaned-data"),
            ],
            fluid=False,
        )
