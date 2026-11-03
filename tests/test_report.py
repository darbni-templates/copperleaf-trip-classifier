from trip_nlp.report import run_experiment


def test_counts_the_test_requests():
    train = [{"text": "cancel my trip", "label": "cancel"}]
    test = [{"text": "cancel it", "label": "cancel"}, {"text": "cancel now", "label": "cancel"}]
    result = run_experiment(train, test)
    assert result["test_size"] == 2
    assert result["accuracy"] == 1.0
