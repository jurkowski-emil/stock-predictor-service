from stockpredictorservice.data_preparation.feature_extractor import (
    extract_all_momentum_indicators,
    extract_all_trend_indicators,
    extract_all_volatility_indicators,
    extract_all_volume_indicators,
)

from ta import volatility, volume, trend, momentum


def test_extract_all_momentum_indicators_basic():

    assert set(i.name for i in extract_all_momentum_indicators()) <= set(dir(momentum))
    assert set(i.name for i in extract_all_trend_indicators()) <= set(dir(trend))
    assert set(i.name for i in extract_all_volatility_indicators()) <= set(
        dir(volatility)
    )
    assert set(i.name for i in extract_all_volume_indicators()) <= set(dir(volume))
