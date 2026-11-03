from trip_nlp.ngrams import features


def test_one_word_has_no_pairs():
    assert features(["hotel"]) == ["hotel"]
