from typing import Optional, Union

import plotly.graph_objs as go
import pandas as pd


def create_drawdown_chart(
    df: pd.DataFrame, 
    date_col: str = 'date', 
    drawdown_col: str = 'drawdownpct',
    chart_theme: Optional[str] = None,
    height: int = 250,
    color_palette: dict = None
) -> go.Figure:
    """
    Create an optimized drawdown chart with configurable parameters.

    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame containing date and drawdown percentage data
    date_col : str, optional
        Name of the date column (default: 'date')
    drawdown_col : str, optional
        Name of the drawdown percentage column (default: 'drawdownpct')
    chart_theme : str, optional
        Plotly chart theme to apply
    height : int, optional
        Chart height in pixels (default: 250)
    color_palette : dict, optional
        Custom color configuration for the chart

    Returns:
    --------
    go.Figure
        Configured Plotly figure for drawdown visualization
    """
    # Default color palette
    default_colors = {
        'fill': 'tomato',
        'line': 'firebrick',
        'background': "#272b30",
        'active_range_selector': 'tomato'
    }
    colors = color_palette or default_colors

    # Create figure with optimized configuration
    fig = go.Figure(
        data=go.Scatter(
            x=df[date_col],
            y=df[drawdown_col],
            fill='tozeroy',
            fillcolor=colors['fill'],
            line=dict(
                color=colors['line'],
                width=2
            ),
            mode='lines',
            name='Drawdown %'
        )
    )

    # Comprehensive layout configuration
    fig.update_layout(
        margin=dict(t=45, b=30, l=25, r=25),
        yaxis={
            'title': '%',
            'titlefont_size': 14,
            'tickfont_size': 12
        },
        title={
            'text': 'Drawdown Charts',
            'x': 0.5,
            'xanchor': 'center'
        },
        paper_bgcolor=colors['background'],
        plot_bgcolor=colors['background'],
        height=height,
        template=chart_theme
    )

    # Advanced x-axis range selector
    range_buttons = [
        {'count': 7, 'label': "1w", 'step': "day", 'stepmode': "backward"},
        {'count': 14, 'label': "2w", 'step': "day", 'stepmode': "backward"},
        {'count': 1, 'label': "1m", 'step': "month", 'stepmode': "backward"},
        {'count': 6, 'label': "6m", 'step': "month", 'stepmode': "backward"},
        {'count': 12, 'label': "12m", 'step': "month", 'stepmode': "backward"},
        {'count': 1, 'label': "YTD", 'step': "year", 'stepmode': "todate"},
        {'label': 'All', 'step': "all"}
    ]

    fig.update_xaxes(
        rangeslider_visible=False,
        rangeselector={
            'buttons': range_buttons,
            'bgcolor': colors['background'],
            'activecolor': colors['active_range_selector']
        }
    )

    return fig


# Main Function
if __name__ == '__main__':
    None


# Usage examples
# Basic usage
# drawdown_chart = create_drawdown_chart(plotlydf_portfval)

# Advanced usage with custom configuration
# custom_colors = {
#     'fill': 'lightblue', 
#     'line': 'darkblue', 
#     'background': '#f0f0f0',
#     'active_range_selector': 'blue'
# }
# drawdown_chart = create_drawdown_chart(
#     plotlydf_portfval, 
#     chart_theme='plotly_white', 
#     height=300,
#     color_palette=custom_colors
# )