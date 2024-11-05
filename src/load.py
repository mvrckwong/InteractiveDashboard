from config.paths import *
from style import *

import glob
import pandas as pd

import pandas as pd
from glob import glob
from time import strftime, sleep
import numpy as np
from datetime import datetime

import dash
from dash import dcc, html, dash_table
from dash.dependencies import Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from jupyter_dash import JupyterDash
from plotly.subplots import make_subplots

# Load the current data.
# last_file = sorted(glob('../outputs/final_current_positions/final_current_positions_*.csv'))[-1] # path to file in the folder
# print(last_file[-(len(last_file))+(last_file.rfind('/')+1):])

# Check the following
# last_file = sorted(glob('../outputs/final_current_positions/final_current_positions_*.csv'))[-1]

CHART_THEME = 'plotly_dark'

# Get the datas
data_files = DATA_DIR / 'positions'
last_file = list(data_files.glob('*.csv'))[-1]

current_positions = pd.read_csv(last_file)
current_positions = current_positions.sort_values(by='current_value', ascending=False).round(2)

ticker_dict = [{'label': current_positions.company[i], 'value': current_positions.ticker[i]} for i in range(current_positions.shape[0])]
first_stock = current_positions.ticker[0]



# Homepage layout
homepage = [
    dbc.Row(dbc.Col(html.H2('PORTFOLIO OVERVIEW', className='text-center mb-3 p-3'))),
    dbc.Row([
        dbc.Col([
            html.H5('Portfolio Value vs Net Invested ($USD)', className='text-center'),
            html.Div(children=f"Portfolio Value: {current_ptfvalue}", className='text-left mb-2'),
            dcc.Graph(id='chrt-portfolio-main',
                      figure=chart_ptfvalue,
                      style={'height': 450},
                      className='shadow-lg'
                     ),
            html.Hr(),

        ],
            width={'size': 8, 'offset': 0, 'order': 1}),
        dbc.Col([
            html.H5('Portfolio', className='text-center'),
            html.Div(children="KPI's", className='text-center fs-4'),
            dcc.Graph(id='indicators-ptf',
                      figure=indicators_ptf,
                      style={'height': 450},
                      className='shadow-lg'),
            html.Hr()
        ],
            width={'size': 2, 'offset': 0, 'order': 2}),
        dbc.Col([
            html.H5('S&P500', className='text-center'),
            html.Div(children="KPI's", className='text-center fs-4'),            
            dcc.Graph(id='indicators-sp',
                      figure=indicators_sp500,
                      style={'height': 450},
                      className='shadow-lg'),
            html.Hr()
        ],
            width={'size': 2, 'offset': 0, 'order': 3}),
    ]),  # end of second row
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='chrt-portfolio-secondary',
                      figure=drawdown_chart,
                      style={'height': 300},
                      className='shadow-lg'),
            html.Hr(),
            dcc.Graph(id='chrt-portfolio-third',
                      figure=portfolio_cashflow,
                      style={'height': 300},
                      className='shadow-lg'),
        ],
            width={'size': 8, 'offset': 0, 'order': 1}),
        dbc.Col([
            dcc.Graph(
                  id='pie-top15',
                  figure=sunburst_fig2,
                  style={'height': 630},
                  className='shadow-lg'     
            ),
        ],
            width={'size': 4, 'offset': 0, 'order': 2}),
    ])

]


# Check the following
if __name__ == "__main__":
      None