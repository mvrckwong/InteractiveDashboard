import plotly.graph_objects as go

sunburst_fig2 = go.Figure()
sunburst_fig2.layout.template = CHART_THEME
sunburst_fig2.add_trace(
      go.Sunburst(
            labels=df_all_trees["id"],
            parents=df_all_trees["parent"],
            values=df_all_trees["value"],
            branchvalues="total",
            marker=dict(
                  colors=df_all_trees["color"], 
                  colorscale="mrybm", 
                  cmid=average_score
            ),
            hovertemplate="<b>%{label} </b> <br> Size: $ %{value}<br> Variation: %{color:.2f}%",
            maxdepth=2,
            name="",
      )
)

sunburst_fig2.update_layout(margin=dict(t=10, b=10, r=10, l=10))
sunburst_fig2.update_layout(paper_bgcolor="#272b30")
sunburst_fig2.show()