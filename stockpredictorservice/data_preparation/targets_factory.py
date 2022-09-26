from pandas import DataFrame
from numpy import isnan, nan


def binary_trend_n_periods(data: DataFrame, periods=1):
    target = DataFrame(data={"close": data["close"]}, index=data.index)
    target = target.assign(pct_change=target["close"].pct_change(periods=periods))
    target["pct_change"] = target["pct_change"].shift(-periods)
    target["target"] = target["pct_change"].map(
        lambda x: x > 0 if not isnan(x) else nan
    )
    return target.drop(columns=["pct_change", "close"])
