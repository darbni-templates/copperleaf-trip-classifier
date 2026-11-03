from trip_nlp.data import split_train_test


def test_every_fifth_request_is_tested():
    requests = [{"text": text, "label": "other"} for text in ["a", "b", "c", "d", "e"]]
    result = split_train_test(requests, 5)
    assert result == {"train": requests[:4], "test": requests[4:]}
