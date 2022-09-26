import os

# type: ignore
from pandas import DataFrame, Timestamp, read_csv

# type: ignore
from yahoo_fin import stock_info

# type: ignore
import exchange_calendars

from .my_types import Ticker


def _ticker_to_market(ticker: str) -> str:

    if ticker.endswith(".WA"):
        return "XWAR"
    else:
        raise ValueError


def get_raw_stocks_data(ticker: Ticker, count, file_tag="") -> DataFrame:

    file_name = f"data/raw_{ticker}_data_{count}{file_tag}.csv"

    if os.path.isfile(file_name):
        data = read_csv(file_name, index_col=0)

    else:
        xwar = exchange_calendars.get_calendar(_ticker_to_market(ticker))
        last_session_date = xwar.previous_close(Timestamp.today())
        session_window = xwar.sessions_window(
            last_session_date.replace(hour=0, minute=0, second=0).date(), -count
        )

        data = stock_info.get_data(
            ticker,
            start_date=session_window[0],
            end_date=session_window[-1].replace(hour=23, minute=59, second=59),
        )
        data = data.dropna()
        data.to_csv(file_name)

    return data
