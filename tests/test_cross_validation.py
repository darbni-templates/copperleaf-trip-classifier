from trip_nlp.cross_validation import fold_indices


def test_every_index_is_in_exactly_one_fold():
    folds = fold_indices(10, 5)
    assert len(folds) == 5
    assert sorted(i for fold in folds for i in fold) == list(range(10))
