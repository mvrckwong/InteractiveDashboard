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
    """
    Prepare portfolio analysis DataFrame with comprehensive metrics
    """

    # Static Variable
    initial_date = '2020-01-09'

    # Get relevant data
    df_transactions = get_transactions_df().copy()
    df_portfolio_value = get_portfolio_df().copy()

    # Filter portfolio values from initial date
    df_portfolio_value = df_portfolio_value[
            df_portfolio_value.index > initial_date
        ]

    # Select and round relevant columns
    columns_to_keep = [
        'portf_value', 
        'sp500_mktvalue', 
        'ptf_value_pctch', 
        'sp500_pctch', 
        'ptf_value_diff', 
        'sp500_diff'
    ]

    # Processing the data.
    df_portfolio_value = df_portfolio_value[columns_to_keep].reset_index().round(2)
    df_portfolio_value.rename(columns={'index': 'date'}, inplace=True)
    df_portfolio_value['date'] = pd.to_datetime(df_portfolio_value['date'])

    # Calculate the date range.
    date_range = pd.date_range(
        df_transactions.date.min(), 
        df_portfolio_value.date.max()
    )

    # Calculate the cashflow
    df_invested = (df_transactions.groupby('date')['cashflow'].sum() * -1)
    df_invested = df_invested.reindex(date_range, fill_value=0).reset_index()
    df_invested.columns = ['date', 'cashflow']
    df_invested['alltime_cashflow'] = df_invested['cashflow'].cumsum()

    # Merge portfolio values with cashflow
    df_combine_pfvalue = pd.merge(
        df_transactions, 
        df_invested, 
        on='date', 
        how='inner'
    )

    # Calculate net investment and portfolio growth metrics
    df_combine_pfvalue['net_invested'] = df_combine_pfvalue['cashflow'].cumsum()
    df_combine_pfvalue['net_value'] = df_combine_pfvalue['portf_value'] - \
        df_combine_pfvalue['net_invested']

    # Compute growth and performance metrics
    first_net_value = df_combine_pfvalue['net_value'].iloc[0]
    first_sp500_value = df_combine_pfvalue['sp500_mktvalue'].iloc[0]

    # Calculate the growth
    df_combine_pfvalue['ptf_growth'] = df_combine_pfvalue['net_value'] / first_net_value
    df_combine_pfvalue['sp500_growth'] = df_combine_pfvalue['sp500_mktvalue'] / first_sp500_value

    # Calculate adjusted portfolio change and drawdown
    df_combine_pfvalue['adjusted_ptfchg'] = (df_combine_pfvalue['net_value'].pct_change() * 100).round(2)
    df_combine_pfvalue['highvalue'] = df_combine_pfvalue['net_value'].cummax()
    df_combine_pfvalue['drawdownpct'] = (
        (df_combine_pfvalue['net_value'] / df_combine_pfvalue['highvalue'] - 1) * 100
    ).round(4)

    return df_invested, df_combine_pfvalue

# Main function
if __name__ == "__main__":
    df_invested, df_combine_pfvalue = prepare_portfolio_analysis()
    print(df_invested)