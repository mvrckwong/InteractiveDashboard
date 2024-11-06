from config.paths import *
import pandas as pd


def get_transactions_df() -> pd.DataFrame:
    
    # Get the data.
    file = list(DATA_DIR.glob("transactions.xlsx"))[0]
    
    # Read the data.
    df_transactions = pd.read_excel(file, engine='openpyxl')
    df_transactions.date = pd.to_datetime(df_transactions.date, format='%d/%m/%Y')
    
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


def get_portfvalue_df() -> pd.DataFrame:
    
    
    return None


# Main function
if __name__ == "__main__":
    None
    # print(get_transactions_df())