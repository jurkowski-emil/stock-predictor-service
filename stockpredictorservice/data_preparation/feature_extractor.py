from inspect import getmembers, isfunction, getfullargspec
from typing import Generator
from functools import partial

import ta.trend
import ta.momentum
import ta.volatility
import ta.volume

from .my_types import IndicatorSpec


def _extract_indicators_from_ta_module(
    sub_module,
) -> Generator[IndicatorSpec, None, None]:
    return (
        IndicatorSpec(
            name=a[0],
            fun=a[1],
            obligatory_params=getfullargspec(a[1]).args[
                : len(getfullargspec(a[1]).args) - len(getfullargspec(a[1]).defaults)
            ],
        )
        for a in getmembers(sub_module)
        if isfunction(a[1])
        if not a[0].startswith("_")
    )


extract_all_momentum_indicators = partial(
    _extract_indicators_from_ta_module, ta.momentum
)

extract_all_trend_indicators = partial(_extract_indicators_from_ta_module, ta.trend)

extract_all_volatility_indicators = partial(
    _extract_indicators_from_ta_module, ta.volatility
)

extract_all_volume_indicators = partial(_extract_indicators_from_ta_module, ta.volume)
