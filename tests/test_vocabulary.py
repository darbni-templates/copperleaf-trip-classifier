from trip_nlp.vocabulary import build_vocabulary


def test_ids_are_numbered_from_zero():
    vocabulary = build_vocabulary([["rome", "trip"], ["rome", "bus"], ["paris", "trip"]] * 2)
    assert sorted(vocabulary.values()) == list(range(len(vocabulary)))
