from datetime import datetime
import yfinance as yf

"""
utils.py contains general utiliy functions

"""

def check_if_options_NASDAQ() -> bool:
    # Checks if the underlying has options via NASDAQ Data Link
    pass


def check_if_options_YFinance() -> bool:
    # Checks if the underlying has options via Yahoo Finance
    pass


def get_current_date() -> str:
    # Returns the current day, month, year as a string seperated by "-". Main purpose is for naming files
    return datetime.now().strftime("%Y-%m-%d")


def log_action():
    # Prints the executed action in the command line, saves it to a log file
    pass