# type: ignore
from pandas import DataFrame

from stockpredictorservice.data_preparation.data_downloader import get_raw_stocks_data

from stockpredictorservice.data_preparation.feature_calculator import (
    calculate_indicators,
)
from stockpredictorservice.data_preparation.targets_factory import (
    binary_trend_n_periods,
)


from stockpredictorservice.data_preparation.feature_extractor import (
    extract_all_momentum_indicators,
    extract_all_volume_indicators,
    extract_all_trend_indicators,
    extract_all_volatility_indicators,
)

from stockpredictorservice.data_preparation.my_types import Ticker


def get_training_data(ticker: Ticker, count=1000) -> DataFrame:
    data = get_raw_stocks_data(ticker, count)

    ind_spec = extract_all_momentum_indicators()
    indicators = calculate_indicators(data=data, ind_specs=ind_spec)

    return data


def get_forecast_data(_: Ticker, _1=1000) -> DataFrame:
    pass
