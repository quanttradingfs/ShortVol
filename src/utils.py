from datetime import datetime
import yfinance as yf
import inspect
"""
utils.py contains general utiliy functions
"""

def log_function(action : str, write_log_to_file : bool = False):
    caller_function = inspect.stack()[1].function
    time = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[LOG] Performed action \'{action}\' in function \'{caller_function}\' at [{time}]")


def check_if_options_NASDAQ() -> bool:
    # Checks if the underlying has options via NASDAQ Data Link
    pass


def check_if_options_YFinance() -> bool:
    # Checks if the underlying has options via Yahoo Finance
    # If yes, returns the option type (european no div, european div, american no div, american div)
    pass


def get_current_date() -> str:
    # Returns the current day, month, year as a string seperated by "-". Main purpose is for naming files
    return datetime.now().strftime("%Y-%m-%d")


def calculate_iv_bs():
    # Calculates implied volatility using the Black-Scholes formula
    pass


def calculate_iv_binomial():
    # Calculates implied volatility using the binomial tree method
    pass



