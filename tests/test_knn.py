from trip_nlp.knn import classify


def test_copies_the_label_of_an_identical_request():
    train = [{"tokens": ["lost", "bag"], "label": "baggage"}]
    assert classify(train, ["lost", "bag"]) == "baggage"
