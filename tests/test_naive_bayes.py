from trip_nlp.naive_bayes import train_and_predict


def test_one_label_always_wins():
    examples = [{"tokens": ["lost", "bag"], "label": "baggage"}]
    assert train_and_predict(examples, [["lost"]])[0]["label"] == "baggage"
