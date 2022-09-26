from stockpredictorservice.data_provider import get_training_data


def test_get_training_data_basic():
    result = get_training_data("PZU.WA")
    print(result)
