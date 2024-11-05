from pandas import DataFrame
import plotly.graph_objects as go

CHART_THEME = 'plotly_dark'

def create_sunburst_fig(
    df_data: DataFrame, 
    chart_theme: str = CHART_THEME, 
    average_score: float = 0, 
    max_depth: int = 2
) -> go.Figure:
      """
      Create a customized Plotly Sunburst chart with flexible configuration.

      Parameters:
      -----------
      df_data : pd.DataFrame
            DataFrame containing sunburst chart data with columns:
            - 'id': Unique identifiers for each segment
            - 'parent': Parent segment identifiers
            - 'value': Numerical values for segment sizing
            - 'color': Color scaling values

      chart_theme : str, optional
            Plotly chart theme to apply. Defaults to CHART_THEME.

      average_score : float, optional
            Midpoint for color scaling. Defaults to 0.

      max_depth : int, optional
            Maximum depth of sunburst hierarchy. Defaults to 2.

      Returns:
      --------
      go.Figure
            Configured Plotly Sunburst chart figure
      """
      # Validate input DataFrame
      required_columns = ['id', 'parent', 'value', 'color']
      if not all(col in df_data.columns for col in required_columns):
            raise ValueError(f"DataFrame must contain columns: {required_columns}")

      # Create Sunburst figure
      sunburst_fig = go.Figure(
            go.Sunburst(
                  labels=df_data["id"],
                  parents=df_data["parent"],
                  values=df_data["value"],
                  branchvalues="total",
                  marker=dict(
                        colors=df_data["color"], 
                        colorscale="mrybm", 
                        cmid=average_score
                  ),
                  hovertemplate="""
                        <b>%{label} </b> <br> Size: $ %{value}<br> Variation: %{color:.2f}%
                  """,
                  maxdepth=max_depth,
                  name="",
            )
      )

      # Apply layout customizations
      sunburst_fig.update_layout(
            template=chart_theme,
            margin=dict(t=10, b=10, r=10, l=10),
            paper_bgcolor="#272b30"
      )

      return sunburst_fig


# Check the following
if __name__ == "__main__":
      None
      
      # try:
      #       sunburst_chart = create_sunburst_chart(
      #             df_data=df_all_trees, 
      #             average_score=avg_score
      #       )
      #       sunburst_chart.show()
      # except ValueError as e:
      #       print(f"Chart creation error: {e}")