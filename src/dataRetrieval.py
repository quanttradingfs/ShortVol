import yfinance as yf
import pandas as pd
from datetime import datetime
import json
from utils import log_function as log

"""
dataRetrieval.py contains functions to download and parse data from third party vendors
"""


class DataRetrieval:
    def __init__(self):
        self.alpaca_key, self.nasdaq_key = self.setup()

    @staticmethod
    def setup(write_log_to_file : bool = False) ->  tuple[str, str]:
        try:
            with open("keys.json","r") as file:
                keys_file = json.load(file)
                alpaca_key = keys_file["Alpaca_API_Key"]
                nasdaq_key = keys_file["Nasdaq_Data_Link_API_Key"]          
                file.close()

                log("Read API Keys")

            return alpaca_key, nasdaq_key

        except FileNotFoundError as e:
            print(f"[FileNotFoundError] {e}")
            return None
        except Exception as e:
            print(f"[Exception] {e}")
            return None

    @staticmethod
    def get_equity_data_YF(tickers: list[str],start: str = "1950-01-01", end: str = "2025-1-1") -> dict[str, pd.DataFrame]:
        """
        Function returns historical data on equities using Yahoo Finance.

        Args:
            tickers (list[str]): List of tickers to be downloaded.
            start (str, optional): The start date of the dataset in 'YYYY-MM-DD' format. Defaults to '1950-01-01'.
            end (str, optional): The end date of the dataset in 'YYYY-MM-DD' format. Defaults to '2025-01-01'.

        Returns:
            dict[str, pd.DataFrame]: A dictionary, keys represent the ticker, the value data
        """
        
        try: 
            # Validate dates
            start_date = datetime.strptime(start, "%Y-%m-%d")
            end_date = datetime.strptime(end, "%Y-%m-%d")
            if start_date > end_date:
                raise ValueError("Start date can't be after end date")

            df = yf.download(tickers=tickers, interval="1d", start=start, end=end, group_by='ticker')

            # Restructure the dataframe
            df_sorted = {
                ticker: df.xs(ticker, axis=1, level=0, drop_level=True).rename_axis(None, axis=1)
                for ticker in df.columns.get_level_values(0).unique()
            }

            log("Requested data from Yahoo Finance")
            return df_sorted

        except ValueError as e:
            print(f"[ValueError] Was the date wrong? [start = {start}] [end = {end}] {e}")
            return None
        
        except ConnectionError as e:
            print(f"[ConnectionError] {e}")
            return None

    @staticmethod
    def get_option_data_YF():
        # Returns the option of the underlying that is closest to the current strike price (Needed for Implied Vol Calculation) using Yahoo Finance
        pass
    
    def get_option_data_Alpaca(self): 
        # Returns the option of the underlying that is closest to the current strike price (Needed for Implied Vol Calculation) using Alpaca Data Link
        pass

    def get_option_data_NASDAQ(self): 
        # Returns the option of the underlying that is closest to the current strike price (Needed for Implied Vol Calculation) using NASDAQ Data Link
        # Without API Key up to 50 API Calls per Day -> Can create free account
        pass


if __name__ == "__main__":

    return_vals = DataRetrieval().get_equity_data_YF(["RHM.DE", "^VIX"],start="2000-12-01", end="2000-12-6")

    print(return_vals["RHM.DE"].head())
    print(return_vals["^VIX"].head())

