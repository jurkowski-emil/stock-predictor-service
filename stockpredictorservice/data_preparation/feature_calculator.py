from pandas import DataFrame
from typing import Iterable

from .my_types import IndicatorSpec
from sklearn.preprocessing import StandardScaler


def calculate_indicators(
    data: DataFrame, ind_specs: Iterable[IndicatorSpec]
) -> DataFrame:
    features = DataFrame(
        data={
            d.name: d.fun(**{i: data.loc[:, i] for i in d.obligatory_params})
            for d in ind_specs
        },
        index=data.index,
    )

    scaler = StandardScaler()
    features = DataFrame(scaler.fit_transform(features), index=features.index, columns=features.columns)

    return features
