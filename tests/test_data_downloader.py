
from stockpredictorservice.data_preparation.data_downloader import get_raw_training_data


def test_get_raw_basic():
    assert 10 == len(get_raw_training_data("PZU.WA", 10))


def test_get_raw_file_not_exists_data(monkeypatch):
    monkeypatch.setattr("yahoo_fin.stock_info.get_data", lambda: "/")
    assert 10 == len(get_raw_training_data("PZU.WA", 10))
