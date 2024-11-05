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

# from style import *
from config.paths import *
from config.logging import *
from static.style import *

from components.helper import *
from components.sunburst import create_sunburst_fig

import pandas as pd
import dash as dash

from load import get_current_position_df


levels = ['ticker', 'industry', 'sector']
color_columns = ['current_value', 'cml_cost']
value_column = 'current_value'

current_positions = get_current_position_df()

def build_hierarchical_dataframe(df, levels, value_column, color_columns=None, total_name='total'):
      """ Build a hierarchy of levels for Sunburst or Treemap charts.

      Levels are given starting from the bottom to the top of the hierarchy,
      ie the last level corresponds to the root.
      """
      df_all_trees = pd.DataFrame(columns=['id', 'parent', 'value', 'color'])
      for i, level in enumerate(levels):
            df_tree = pd.DataFrame(columns=['id', 'parent', 'value', 'color'])
            dfg = df.groupby(levels[i:]).sum()
            dfg = dfg.reset_index()
            df_tree['id'] = dfg[level].copy()
            if i < len(levels) - 1:
                  df_tree['parent'] = dfg[levels[i+1]].copy()
            else:
                  df_tree['parent'] = total_name
            df_tree['value'] = dfg[value_column]
            df_tree['color'] = round((dfg[color_columns[0]] / dfg[color_columns[1]]-1)*100, 2)
            df_all_trees = df_all_trees._append(df_tree, ignore_index=True)
      total = pd.Series(dict(id=total_name, parent='',
                                    value=df[value_column].sum(),
                                    color=100*round(df[color_columns[0]].sum() / df[color_columns[1]].sum()-1,2)))
      df_all_trees = df_all_trees._append(total, ignore_index=True)
      return df_all_trees

df_all_trees = build_hierarchical_dataframe(
      current_positions, levels, value_column, color_columns, total_name='Portfolio'
)

sunburst_fig = create_sunburst_fig(df_all_trees)



def create_sidebar() -> dash.html.Div:
      """  
      Create the sidebar for the application.
      """
      
      sidebar = dash.html.Div(
            [
                  dash.html.Hr(),
                  dash.html.P(
                        "Investment Tracker v0.95", 
                        className="text-center p-3 border border-dark"
                  ),
                  dash.html.Hr(),
                  dash.dcc.Nav(
                        [
                              dash.dcc.NavLink("Portfolio", href="/", active="exact"),
                              dash.dcc.NavLink("Ticker View", href="/tickerpage", active="exact"),
                              dash.dcc.NavLink("Sunburst Chart", href="/sunburst", active="exact"),
                              dash.dcc.NavLink("Table View", href="/tableview", active="exact"),
                        ],
                        vertical=True,
                        pills=True,
                  ),
            ],
            style=SIDEBAR_STYLE,
      )
      
      return sidebar

def create_homepage() -> dash.html.Div:

    homepage = [
        dbc.Row(
            dbc.Col(html.H2("PORTFOLIO OVERVIEW", className="text-center mb-3 p-3"))
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Graph(
                            id="pie-top15",
                            figure=sunburst_fig,
                            style={"height": 630},
                            className="shadow-lg",
                        ),
                    ],
                    width={"size": 4, "offset": 0, "order": 2},
                ),
            ]
        ),
    ]

    return homepage


def main() -> bool:
      return None



print("WORKING")


# Running the application
# if __name__ == "__main__":
#     app.run_server(debug=True, port=8095)