from dash import html, dcc, dash_table

import dash_bootstrap_components as dbc

def create_sidebar() -> html.Div:
      """
      Create the sidebar for the application.

      Returns:
      --------
      dash.html.Div
            The sidebar content
      """
      return html.Div(
            [
                  html.Hr(),
                  html.P('Investment Tracker v0.95', className='text-center p-3 border border-dark'),
                  html.Hr(),
                  dbc.Nav(
                        [
                              dbc.NavLink('Portfolio', href="/", active='exact'),
                              dbc.NavLink('Ticker View', href="/tickerpage", active='exact'),
                              dbc.NavLink('Sunburst Chart', href="/sunburst", active='exact'),
                              dbc.NavLink('Table View', href="/tableview", active='exact')
                        ],
                        vertical=True,
                        pills=True,
                  ),
            ],
            style=SIDEBAR_STYLE,
      )

def create_home_page() -> html.Div:
    """
    Create the homepage for the application.

    Returns:
    --------
    dash.html.Div
          The homepage content
    """
    return [
        dbc.Row(
            dbc.Col(
                  html.H2(
                        "PORTFOLIO OVERVIEW", 
                        className="text-center mb-3 p-3"
                  )
            )
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H5(
                            "Portfolio Value vs Net Invested ($USD)",
                            className="text-center",
                        ),
                        html.Div(
                            children=f"Portfolio Value: {current_ptfvalue}",
                            className="text-left mb-2",
                        ),
                        dcc.Graph(
                            id="chrt-portfolio-main",
                            figure=chart_ptfvalue,
                            style={"height": 450},
                            className="shadow-lg",
                        ),
                        html.Hr(),
                    ],
                    width={"size": 8, "offset": 0, "order": 1},
                ),
                dbc.Col(
                    [
                        html.H5("Portfolio", className="text-center"),
                        html.Div(children="KPI's", className="text-center fs-4"),
                        dcc.Graph(
                            id="indicators-ptf",
                            figure=indicators_ptf,
                            style={"height": 450},
                            className="shadow-lg",
                        ),
                        html.Hr(),
                    ],
                    width={"size": 2, "offset": 0, "order": 2},
                ),
                dbc.Col(
                    [
                        html.H5("S&P500", className="text-center"),
                        html.Div(children="KPI's", className="text-center fs-4"),
                        dcc.Graph(
                            id="indicators-sp",
                            figure=indicators_sp500,
                            style={"height": 450},
                            className="shadow-lg",
                        ),
                        html.Hr(),
                    ],
                    width={"size": 2, "offset": 0, "order": 3},
                ),
            ]
        ),  # end of second row
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Graph(
                            id="chrt-portfolio-secondary",
                            figure=drawdown_chart,
                            style={"height": 300},
                            className="shadow-lg",
                        ),
                        html.Hr(),
                        dcc.Graph(
                            id="chrt-portfolio-third",
                            figure=portfolio_cashflow,
                            style={"height": 300},
                            className="shadow-lg",
                        ),
                    ],
                    width={"size": 8, "offset": 0, "order": 1},
                ),
                dbc.Col(
                    [
                        dcc.Graph(
                            id="pie-top15",
                            figure=sunburst_fig2,
                            style={"height": 630},
                            className="shadow-lg",
                        ),
                    ],
                    width={"size": 4, "offset": 0, "order": 2},
                ),
            ]
        ),
    ]


def create_ticker_page() -> html.Div:
      """
      Create the ticker for the application.

      Returns:
      --------
      dash.html.Div
            The ticker content
      """
      return [
            dbc.Row(
                  dbc.Col(
                        html.H2(
                              "TICKER VIEW", 
                              className="text-center mb-3 p-3"
                        )
                  )
            ),
            dbc.Row(
                  [
                  dbc.Col(
                        [
                              html.H5("Candlestick chart", className="text-center"),
                              dcc.Dropdown(
                              id="ticker-selector",
                              options=ticker_dict,
                              value=first_stock,
                              clearable=False,
                              ),
                              dcc.Graph(
                              id="chrt-ticker-main",
                              figure=fig_main,
                              style={"height": 920},
                              className="shadow-lg",
                              ),
                              html.Hr(),
                        ],
                        width={"size": 9, "offset": 0, "order": 1},
                  ),
                  dbc.Col(
                        [
                              #             html.H5('Metrics', className='text-center'),
                              dash_table.DataTable(
                              id="first-table",
                              columns=[],
                              data=[],
                              style_header={"display": "none"},
                              style_data={
                                    "whiteSpace": "normal",
                                    "height": "auto",
                                    "lineHeight": "15px",
                                    "border": "none",
                                    "backgroundColor": "#272b30",
                                    "color": "white"
                                    #                                                'textAlign': 'center'
                              },
                              style_cell_conditional=[
                                    {
                                          "if": {"column_id": "indicator"},
                                          "width": "40%",
                                          "textAlign": "left",
                                          "fontWeight": "bold"
                                          #                                      'backgroundColor': 'rgba(0, 116, 217, 0.3)',
                                          #                                      'color': 'rgba(0,20,80,1)'
                                    },
                              ],
                              ),
                              html.Hr(),
                              dash_table.DataTable(
                              id="second-table",
                              columns=[],
                              data=[],
                              style_header={"display": "none"},
                              style_data={
                                    "whiteSpace": "normal",
                                    "height": "auto",
                                    "lineHeight": "15px",
                                    "border": "none",
                                    "backgroundColor": "#272b30",
                                    "color": "white"
                                    #                                                'textAlign': 'center'
                              },
                              style_cell_conditional=[
                                    {
                                          "if": {"column_id": "indicator"},
                                          "width": "40%",
                                          "textAlign": "left",
                                          "fontWeight": "bold",
                                    }
                              ],
                              ),
                              html.Hr(),
                              dash_table.DataTable(
                              id="third-table",
                              columns=[],
                              data=[],
                              style_header={"display": "none"},
                              style_data={
                                    "whiteSpace": "normal",
                                    "height": "auto",
                                    "lineHeight": "15px",
                                    "border": "none",
                                    "backgroundColor": "#272b30",
                                    "color": "white"
                                    #                                                'textAlign': 'center'
                              },
                              style_cell_conditional=[
                                    {
                                          "if": {"column_id": "indicator"},
                                          "width": "40%",
                                          "textAlign": "left",
                                          "fontWeight": "bold",
                                    }
                              ],
                              ),
                              html.Hr(),
                        ],
                        width={"size": 3, "offset": 0, "order": 2},
                  ),
                  ]
            ),
      ]


def create_table_page(table_view) -> html.Div:
      """
      Create the table for the application.
      
      Returns:
      --------
      dash.html.Div
            The table content
      """
      return [
            dbc.Row(dbc.Col(html.H2('FULL TABLE VIEW', className='text-center mb-3 p-3'))),
            dbc.Row([
                  dbc.Col([
                        html.H5(
                              'Detailed view about every stock', className='text-left'
                        ),
                        html.Hr(),
                        table_view,
                        html.Hr(),

                  ],
                        width={'size': 12, 'offset': 0, 'order': 1}
                  ),
            ]),
      ]

def create_sunburst_page() -> html.Div:
      """
      Create the table for the application.
      
      Returns:
      --------
      dash.html.Div
            The table content
      """
      return [
            dbc.Row(dbc.Col(html.H2('SUNBURST VIEW', className='text-center mb-3 p-3'))),
            dbc.Row([
                  dbc.Col([
                        html.H5('Explore your portfolio interactively', className='text-left'),
                        html.Div(children=f"Portfolio Value: {current_ptfvalue}", className='text-left'),
                        html.Hr(),
                        dcc.Graph(id='chrt-sunburstpage',
                              figure=sunburst_all,
                              style={'height': 800}),
                        html.Hr(),

                  ],
                        width={'size': 12, 'offset': 0, 'order': 1}
                  ),
            ]),
      ]

if __name__ == "__main__":
      None