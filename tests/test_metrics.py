from trip_nlp.metrics import confusion_matrix


def test_all_correct_with_one_label():
    assert confusion_matrix(["visa", "visa"], ["visa", "visa"]) == {
        "labels": ["visa"],
        "matrix": [[2]],
    }
