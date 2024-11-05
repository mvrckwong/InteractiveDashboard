from config.paths import *
import pandas as pd


# last_file = sorted(glob('../outputs/final_current_positions/final_current_positions_*.csv'))[-1] # path to file in the folder
# print(last_file[-(len(last_file))+(last_file.rfind('/')+1):])
# current_positions = pd.read_csv(last_file)
# current_positions = current_positions.sort_values(by='current_value', ascending=False).round(2)

# # Navigate into position data directory
# data_position_dir = DATA_DIR / "positions"

# # Get the files
# file = list(data_position_dir.glob("*.csv"))[-1]
# current_positions = pd.read_csv(file)
# current_positions = current_positions.sort_values(by='current_value', ascending=False).round(2)

def get_current_position_df():
    """ Get the current positions dataframe. """
    
    # Navigate into position data directory
    data_position_dir = DATA_DIR / "positions"

    # Get the files
    file = list(data_position_dir.glob("*.csv"))[-1]
    position_df = pd.read_csv(file).sort_values(by='current_value', ascending=False).round(2)
    
    return position_df


# Check the following
if __name__ == "__main__":
    None
    # get_current_position_df()