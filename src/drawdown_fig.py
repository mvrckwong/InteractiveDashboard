import plotly.graph_objects as go
from data import prepare_portfolio_analysis

CHART_THEME = 'plotly_dark'  # others include seaborn, ggplot2, plotly_white, plotly_dark

# 
df_pfvalue, df_invested = prepare_portfolio_analysis()

# drawdown_chart = go.Figure()  # generating a figure that will be updated in the following lines
# drawdown_chart.add_trace(
#     go.Scatter(
#         x=plotlydf_portfval.date,
#         y=plotlydf_portfval.drawdownpct,
#         fill='tozeroy',
#         fillcolor='tomato',
#         line = dict(
#             color='firebrick',
#             width=2),
#         mode='lines',  # you can also use "lines+markers", or just "markers"
#         name='Drawdown %'))

# drawdown_chart.update_layout(
#     margin = dict(t=45, b=30, l=25, r=25),
#     yaxis=dict(
#         title='%',
#         titlefont_size=14,
#         tickfont_size=12,
#         ),
#     title='Drawdown',
#     title_x=0.5,
#     paper_bgcolor="#272b30",
#     plot_bgcolor="#272b30"
# )

# drawdown_chart.update_xaxes(
#     rangeslider_visible=False,
#         rangeselector=dict(
#             buttons=list([
#                 dict(count=7, label="1w", step="day", stepmode="backward"),
#                 dict(count=14, label="2w", step="day", stepmode="backward"),
#                 dict(count=1, label="1m", step="month", stepmode="backward"),
#                 dict(count=6, label="6m", step="month", stepmode="backward"),
#                 dict(count=12, label="12m", step="month", stepmode="backward"),
#                 dict(count=1, label="YTD", step="year", stepmode="todate"),
#                 dict(label='All', step="all"),
#             ]),
#             bgcolor="#272b30",
#             activecolor='tomato',
# #             y=1.02,
# #             x=0.05
#         )
# )

# drawdown_chart.layout.template = CHART_THEME
# drawdown_chart.layout.height=250
# drawdown_chart.show()