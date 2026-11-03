from trip_nlp.split import stratified_split


def test_every_request_lands_on_exactly_one_side():
    requests = [{"id": f"r{i}", "text": "hi", "label": "ab"[i % 2]} for i in range(10)]
    result = stratified_split(requests, 30, seed=1)
    assert sorted(result["train"] + result["test"]) == sorted(r["id"] for r in requests)
