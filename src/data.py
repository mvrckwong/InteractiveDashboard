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
    df_portfolio = pd.read_csv(file)
    df_portfolio = df_portfolio.set_index('date')
    
    return df_portfolio

def prepare_portfolio_analysis(
    portf_allvalues, all_transactions, initial_date='2020-01-09'
):
    """
    Prepare portfolio analysis DataFrame with comprehensive metrics
    """
    
    # Get the data
    
    # Filter portfolio values from initial date
    plotlydf_portfval = portf_allvalues[
            portf_allvalues.index > initial_date
        ].copy()
    
    # Select and round relevant columns
    columns_to_keep = [
        'portf_value', 'sp500_mktvalue', 'ptf_value_pctch', 
        'sp500_pctch', 'ptf_value_diff', 'sp500_diff'
    ]
    plotlydf_portfval = plotlydf_portfval[columns_to_keep].reset_index().round(2)
    plotlydf_portfval.rename(columns={'index': 'date'}, inplace=True)
    plotlydf_portfval['date'] = pd.to_datetime(plotlydf_portfval['date'])
    
    # Calculate cumulative cashflow
    invested_df = (
        all_transactions.groupby('date')['cashflow'].sum() * -1
    )
    date_range = pd.date_range(all_transactions.date.min(), plotlydf_portfval.date.max())
    invested_df = invested_df.reindex(date_range, fill_value=0).reset_index()
    invested_df.columns = ['date', 'cashflow']
    invested_df['alltime_cashflow'] = invested_df['cashflow'].cumsum()
    
    # Merge portfolio values with cashflow
    plotlydf_portfval = pd.merge(plotlydf_portfval, invested_df, on='date', how='inner')
    
    # Calculate net investment and portfolio growth metrics
    plotlydf_portfval['net_invested'] = plotlydf_portfval['cashflow'].cumsum()
    plotlydf_portfval['net_value'] = plotlydf_portfval['portf_value'] - plotlydf_portfval['net_invested']
    
    # Compute growth and performance metrics
    first_net_value = plotlydf_portfval['net_value'].iloc[0]
    first_sp500_value = plotlydf_portfval['sp500_mktvalue'].iloc[0]
    
    plotlydf_portfval['ptf_growth'] = plotlydf_portfval['net_value'] / first_net_value
    plotlydf_portfval['sp500_growth'] = plotlydf_portfval['sp500_mktvalue'] / first_sp500_value
    
    # Calculate adjusted portfolio change and drawdown
    plotlydf_portfval['adjusted_ptfchg'] = (plotlydf_portfval['net_value'].pct_change() * 100).round(2)
    plotlydf_portfval['highvalue'] = plotlydf_portfval['net_value'].cummax()
    plotlydf_portfval['drawdownpct'] = (
        (plotlydf_portfval['net_value'] / plotlydf_portfval['highvalue'] - 1) * 100
    ).round(4)
    
    return plotlydf_portfval


# Main function
if __name__ == "__main__":
    None