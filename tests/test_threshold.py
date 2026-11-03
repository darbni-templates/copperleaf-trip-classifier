from trip_nlp.threshold import decide


def test_a_certain_model_answers():
    assert decide({"visa": 100}) == "visa"
