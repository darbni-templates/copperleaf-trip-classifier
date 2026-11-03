from trip_nlp.idf import compute_idf


def test_a_word_in_every_document_weighs_one():
    assert compute_idf([["rome"]]) == {"rome": 1.0}
