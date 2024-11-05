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
from dash import dcc
from dash import html
from dash.dependencies import Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from dash import dash_table
from jupyter_dash import JupyterDash
from plotly.subplots import make_subplots

# Load the current data.
# last_file = sorted(glob('../outputs/final_current_positions/final_current_positions_*.csv'))[-1] # path to file in the folder
# print(last_file[-(len(last_file))+(last_file.rfind('/')+1):])

# Check the following
# last_file = sorted(glob('../outputs/final_current_positions/final_current_positions_*.csv'))[-1]

# Get the datas
data_files = DATA_DIR / 'positions'
last_file = list(data_files.glob('*.csv'))[-1]

current_positions = pd.read_csv(last_file)
current_positions = current_positions.sort_values(by='current_value', ascending=False).round(2)

ticker_dict = [{'label': current_positions.company[i], 'value': current_positions.ticker[i]} for i in range(current_positions.shape[0])]
first_stock = current_positions.ticker[0]

sidebar = html.Div(
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


# Check the following
if __name__ == "__main__":
      None