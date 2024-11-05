from style import *
from config.paths import *
from config.logging import *

from components.helper import *
from components.sunburst import *

import pandas as pd
import dash as dash

CHART_THEME = 'plotly_dark'
SIDEBAR_STYLE = {
      'position': 'fixed',
      'top': 0,
      'left': 0,
      'bottom': 0,
      'width': '12rem',
      'padding': '2rem 1rem',
      'background-color': 'rgba(120, 120, 120, 0.4)',
}

CONTENT_STYLE = {
      'margin-left': '15rem',
      'margin-right': '2rem',
      'padding': '2rem' '1rem',
}

# Sidebar
sidebar = dash.html.Div(
      [
            dash.html.Hr(),
            dash.html.P(
                  "Investment Tracker v0.95", 
                  className="text-center p-3 border border-dark"
            ),
            dash.html.Hr(),
            dash.dbc.Nav(
                  [
                        dash.dbc.NavLink("Portfolio", href="/", active="exact"),
                        dash.dbc.NavLink("Ticker View", href="/tickerpage", active="exact"),
                        dash.dbc.NavLink("Sunburst Chart", href="/sunburst", active="exact"),
                        dash.dbc.NavLink("Table View", href="/tableview", active="exact"),
                  ],
                  vertical=True,
                  pills=True,
            ),
      ],
      style=SIDEBAR_STYLE,
)


# Homepage
homepage = [
      dash.dbc.Row(
            dash.dbc.Col(dash.html.H2(
                  "PORTFOLIO OVERVIEW", 
                  className="text-center mb-3 p-3"
            ))      
      ), # end of first row
      # dash.dbc.Row(
      #       [
      #       dash.dbc.Col(
      #             [
      #                   dash.html.H5(
      #                         "Portfolio Value vs Net Invested ($USD)",
      #                         className="text-center",
      #                   ),
      #                   dash.html.Div(
      #                         children=f"Portfolio Value: {current_ptfvalue}",
      #                         className="text-left mb-2",
      #                   ),
      #                   dash.dcc.Graph(
      #                         id="chrt-portfolio-main",
      #                         figure=chart_ptfvalue,
      #                         style={"height": 450},
      #                         className="shadow-lg",
      #                   ),
      #                   dash.html.Hr(),
      #             ],
      #             width={
      #                   "size": 8, "offset": 0, "order": 1
      #             },
      #       ),
      #       dash.dbc.Col(
      #             [
      #                   dash.html.H5("Portfolio", className="text-center"),
      #                   dash.html.Div(children="KPI's", className="text-center fs-4"),
      #                   dash.dcc.Graph(
      #                   id="indicators-ptf",
      #                   figure=indicators_ptf,
      #                   style={"height": 450},
      #                   className="shadow-lg",
      #                   ),
      #                   dash.html.Hr(),
      #             ],
      #             width={
      #                   "size": 2, "offset": 0, "order": 2
      #             },
      #       ),
      #       dash.dbc.Col(
      #             [
      #                   dash.html.H5("S&P500", className="text-center"),
      #                   dash.html.Div(children="KPI's", className="text-center fs-4"),
      #                   dash.dcc.Graph(
      #                   id="indicators-sp",
      #                   figure=dash.indicators_sp500,
      #                   style={"height": 450},
      #                   className="shadow-lg",
      #                   ),
      #                   dash.html.Hr(),
      #             ],
      #             width={
      #                   "size": 2, "offset": 0, "order": 3
      #             },
      #       ),
      #       ]
      # ),  # end of second row
      dash.dbc.Row(
            [
            # dash.dbc.Col(
            #       [
            #             dash.dcc.Graph(
            #             id="chrt-portfolio-secondary",
            #             figure=drawdown_chart,
            #             style={"height": 300},
            #             className="shadow-lg",
            #             ),
            #             dash.html.Hr(),
            #             dash.dcc.Graph(
            #             id="chrt-portfolio-third",
            #             figure=portfolio_cashflow,
            #             style={"height": 300},
            #             className="shadow-lg",
            #             ),
            #       ],
            #       width={
            #             "size": 8, "offset": 0, "order": 1
            #       },
            # ),
            dash.dbc.Col(
                  [
                        dash.dcc.Graph(
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



# def main():
#       return app.run_server(debug=True, port=8095)


# Running the application
# if __name__ == "__main__":
#     app.run_server(debug=True, port=8095)