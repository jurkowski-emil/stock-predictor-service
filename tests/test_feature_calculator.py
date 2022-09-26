from stockpredictorservice.data_preparation.feature_calculator import (
    calculate_indicators,
)
from stockpredictorservice.data_preparation.feature_extractor import (
    extract_all_momentum_indicators,
)


from numpy import random
from pandas import DataFrame
from pytest import raises


def test_calculate_indicators_basic():

    _test_data_size = 100
    _test_data = DataFrame(
        {
            "low": random.uniform(0.45, 0.5, size=_test_data_size),
            "high": random.uniform(0.5, 0.6, size=_test_data_size),
            "volume": random.uniform(900, 1100, size=_test_data_size),
            "close": random.uniform(0.5, 0.55, size=_test_data_size),
        }
    )

    ind_spec = tuple(extract_all_momentum_indicators())

    result = calculate_indicators(_test_data, ind_spec)
    print(result)
    assert result.shape[1] == len(ind_spec)
    assert result.shape[0] == _test_data_size


def test_calculate_indicators_missing_colum():

    _test_data_size = 100
    _test_data = DataFrame(
        {
            "low": random.uniform(0.45, 0.5, size=_test_data_size),
            "high": random.uniform(0.5, 0.6, size=_test_data_size),
            "volume": random.uniform(900, 1100, size=_test_data_size),
        }
    )

    ind_spec = tuple(extract_all_momentum_indicators())

    with raises(KeyError):
        calculate_indicators(_test_data, ind_spec)


def test_calculate_indicators_additional_column():

    _test_data_size = 100
    _test_data = DataFrame(
        {
            "low": random.uniform(0.45, 0.5, size=_test_data_size),
            "high": random.uniform(0.5, 0.6, size=_test_data_size),
            "volume": random.uniform(900, 1100, size=_test_data_size),
            "close": random.uniform(0.5, 0.55, size=_test_data_size),
            "additional_column": random.uniform(0.5, 0.55, size=_test_data_size),
        }
    )

    ind_spec = tuple(extract_all_momentum_indicators())

    result = calculate_indicators(_test_data, ind_spec)
    assert result.shape[1] == len(ind_spec)
    assert result.shape[0] == _test_data_size
