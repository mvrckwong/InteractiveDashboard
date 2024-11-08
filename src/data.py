from config.paths import *
import pandas as pd


def get_transactions_df() -> pd.DataFrame:
    
      # Get the data.
      file = list(DATA_DIR.glob("transactions.xlsx"))[0]
      
      # Read the data.
      df_transactions = pd.read_excel(file, engine='openpyxl')
      df_transactions.date = pd.to_datetime(
            df_transactions.date, format='%d/%m/%Y'
      )
      
      return df_transactions

def get_positions_df() -> pd.DataFrame:
      
      # Get the data.
      file = list(DATA_DIR.glob("positions.csv"))[0]
      
      # Read the data.
      df_positions = pd.read_csv(file)
      df_positions = df_positions.sort_values(
            by='current_value', ascending=False
      ).round(2)
      
      return df_positions

def get_portfolio_df() -> pd.DataFrame:
    
      # Get the data.
      file = list(DATA_DIR.glob("portfolio.csv"))[0]
      
      # Read the data.
      df_pfvalue = pd.read_csv(file)
      df_pfvalue = df_pfvalue.set_index('date')
      
      return df_pfvalue

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
      
      # Get the range based on the data
      idx = pd.date_range(
            df_transactions.date.min(), df_pfvalue.date.max()
      )
      
      # Calculated the returns and invested
      df_invested = (df_transactions.groupby('date').sum()['cashflow']*-1)
      df_invested = df_invested.reindex(idx, fill_value=0).reset_index()
      df_invested.rename(columns={'index': 'date'}, inplace=True)
      df_invested['alltime_cashflow'] = df_invested['cashflow'].cumsum()
      
      # Combine the following data
      df_combine_pfvalues = pd.merge(df_pfvalue, df_invested, on='date', how='inner')
      
      # Calculations
      df_combine_pfvalues['net_invested'] = df_combine_pfvalues['cashflow'].cumsum()
      df_combine_pfvalues['net_value'] = df_combine_pfvalues.portf_value - df_combine_pfvalues.net_invested
      df_combine_pfvalues['ptf_growth'] = df_combine_pfvalues.net_value/df_combine_pfvalues['net_value'].iloc[0]
      df_combine_pfvalues['sp500_growth'] = df_combine_pfvalues.sp500_mktvalue/df_combine_pfvalues['sp500_mktvalue'].iloc[0]
      
      # Calculating the adjusted portfolio growth
      df_combine_pfvalues['adjusted_ptfchg'] = (df_combine_pfvalues['net_value'].pct_change()*100).round(2)
      df_combine_pfvalues['highvalue'] = df_combine_pfvalues['net_value'].cummax()
      df_combine_pfvalues['drawdownpct'] = (df_combine_pfvalues['net_value']/df_combine_pfvalues['highvalue']-1).round(4)*100
      
      return df_pfvalue, df_invested


if __name__ == '__main__':
      # df_pfvalue, df_invested = prepare_portfolio_analysis()
      # print(df_pfvalue)
      # print(df_invested)
      
      None