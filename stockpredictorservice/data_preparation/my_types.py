from dataclasses import dataclass
from typing import Iterable


Ticker = str


@dataclass(frozen=True)
class IndicatorSpec:
    name: str
    fun: callable
    obligatory_params: Iterable
