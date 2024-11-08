from data import get_portfolio_df, get_transactions_df, get_positions_df
import pandas as pd




def prepare_portfolio_analysis():
      
      # Get the following data
      df_pfvalue = get_portfolio_df()
      df_transactions = get_transactions_df()
      
      # Static Variables
      initial_date = '2020-01-09'
      
      # Processing the data
      df_pfvalue = df_pfvalue[
            df_pfvalue.index > initial_date
      ]
      df_pfvalue = df_pfvalue[
            [
                  'portf_value', 
                  'sp500_mktvalue', 
                  'ptf_value_pctch',                         
                  'sp500_pctch', 
                  'ptf_value_diff', 
                  'sp500_diff'
            ]
      ]
      df_pfvalue.reset_index(inplace=True)
      df_pfvalue.round(2)
      
      # Calculating the cumulative growth.
      df_pfvalue.rename(columns={'index': 'date'}, inplace=True)
      df_pfvalue.date = pd.to_datetime(df_pfvalue.date)
      
      return df_pfvalue



print(prepare_portfolio_analysis())


# # plotlydf_portfval = portf_allvalues.copy()

# # calculating cumulative growth since initial date
# plotlydf_portfval.rename(columns={'index': 'date'}, inplace=True)  # needed for later
# plotlydf_portfval.date = pd.to_datetime(plotlydf_portfval.date)
# plotlydf_portfval




# # Going to use the column cashflow to calculate a net return on the assets
# invested_df = (all_transactions.groupby('date').sum()['cashflow']*-1)
# idx = pd.date_range(all_transactions.date.min(), plotlydf_portfval.date.max())
# invested_df = invested_df.reindex(idx, fill_value=0).reset_index()
# invested_df.rename(columns={'index': 'date'}, inplace=True)
# invested_df['alltime_cashflow'] = invested_df['cashflow'].cumsum()


# plotlydf_portfval = pd.merge(plotlydf_portfval, invested_df, on='date', how='inner')
# # net invested will let us know how much we invested during the period in analysis
# # then we take this out of the portfolio value, to calculate the returns
# plotlydf_portfval['net_invested'] = plotlydf_portfval['cashflow'].cumsum()
# plotlydf_portfval['net_value'] = plotlydf_portfval.portf_value - plotlydf_portfval.net_invested
# plotlydf_portfval['ptf_growth'] = plotlydf_portfval.net_value/plotlydf_portfval['net_value'].iloc[0]
# plotlydf_portfval['sp500_growth'] = plotlydf_portfval.sp500_mktvalue/plotlydf_portfval['sp500_mktvalue'].iloc[0]
# # adjusted ptfchg will be the accurate variation (net of investments)
# plotlydf_portfval['adjusted_ptfchg'] = (plotlydf_portfval['net_value'].pct_change()*100).round(2)
# plotlydf_portfval['highvalue'] = plotlydf_portfval['net_value'].cummax()
# plotlydf_portfval['drawdownpct'] = (plotlydf_portfval['net_value']/plotlydf_portfval['highvalue']-1).round(4)*100
