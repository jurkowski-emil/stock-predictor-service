# type: ignore
from pandas import DataFrame

from stockpredictorservice.data_preparation.my_types import Ticker


def get_training_data(_: Ticker, _1=1000) -> DataFrame:
    pass


def get_forecast_data(_: Ticker, _1=1000) -> DataFrame:
    pass
