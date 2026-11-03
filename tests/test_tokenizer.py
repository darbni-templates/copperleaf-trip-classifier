from trip_nlp.tokenizer import tokenize


def test_plain_lowercase_words():
    assert tokenize("hello world") == ["hello", "world"]
