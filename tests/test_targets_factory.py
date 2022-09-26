from stockpredictorservice.data_preparation.targets_factory import (
    binary_trend_n_periods,
)

from pandas import DataFrame
import pytest


@pytest.mark.parametrize(
    "close_input, periods_input, expected_shape, nan_count",
    [([1, 2, 4, 2, 1], 1, (5, 1), 1), ([1, 2, 4, 2, 1], 2, (5, 1), 2)],
)
def test_binary_trend_n_periods_basic(
    close_input, periods_input, expected_shape, nan_count
):
    data = DataFrame(data={"close": close_input})
    result = binary_trend_n_periods(data, periods=periods_input)

    assert result.shape == expected_shape
    assert result["target"].isna().sum() == nan_count
