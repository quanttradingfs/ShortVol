import yfinance as yf
import pandas as pd

"""
dataRetrieval.py contains functions for retrieving financial data
"""


def get_equity_data_YFinance()-> tuple[int, list[pd.DataFrame]]:
    """

    Function returns historical data on equities using Yahoo Finance


    """
    pass


# Maybe also implement get_equity_data and get_option_data using Alpaca


def get_option_data_YFinance():
    # Returns the option of the underlying that is closest to the current strike price (Needed for Implied Vol Calculation) using Yahoo Finance

    pass


def get_option_data_NASDAQ(): 
    # Returns the option of the underlying that is closest to the current strike price (Needed for Implied Vol Calculation) using NASDAQ Data Link
    # Without API Key up to 50 API Calls per Day -> Can create free account
    
    pass

