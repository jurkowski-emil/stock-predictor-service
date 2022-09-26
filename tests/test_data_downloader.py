from stockpredictorservice.data_preparation.data_downloader import get_raw_stocks_data

from pandas import DataFrame
from pathlib import Path
from pytest import fixture

TESTING_TAG = "_testing"


@fixture
def clean_data_dir():
    yield
    for f in Path("data").glob(f"*{TESTING_TAG}.csv"):
        f.unlink()


def test_get_raw_basic(clean_data_dir):
    assert 10 == len(get_raw_stocks_data("PZU.WA", 10, file_tag=TESTING_TAG))


def test_get_raw_file_not_exists_data(monkeypatch, clean_data_dir):

    monkeypatch.setattr(
        "yahoo_fin.stock_info.get_data", lambda *args, **kwargs: DataFrame()
    )
    ticker = "PZU.WA"
    count = 1
    my_file = Path(f"data/raw_{ticker}_data_{count}{TESTING_TAG}.csv")

    assert 0 == len(
        get_raw_stocks_data(ticker=ticker, count=count, file_tag=TESTING_TAG)
    )
    assert my_file.is_file()


def test_get_raw_file_exists_data(monkeypatch, clean_data_dir):
    monkeypatch.setattr(
        "yahoo_fin.stock_info.get_data", lambda *args, **kwargs: DataFrame()
    )
    ticker = "PZU.WA"
    count = 1
    my_file = Path(f"data/raw_{ticker}_data_{count}{TESTING_TAG}.csv")
    data_expected = DataFrame(data={"col1": [1, 2], "col2": [3, 4]})
    data_expected.to_csv(my_file, index=False)

    assert data_expected.equals(
        get_raw_stocks_data(ticker=ticker, count=count, file_tag=TESTING_TAG)
    )
