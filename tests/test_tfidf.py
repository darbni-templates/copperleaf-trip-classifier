from trip_nlp.tfidf import run_vectorizer


def test_one_word_document():
    assert run_vectorizer([["paris"]], [["paris"]]) == [{"paris": 1.0}]
