from trip_nlp.pipeline import run_steps


def test_no_steps_only_splits():
    assert run_steps([], "Hello  World") == ["Hello", "World"]
