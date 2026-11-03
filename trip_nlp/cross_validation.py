def fold_indices(n: int, k: int) -> list[list[int]]:
    """Which example indices belong to each of the k folds."""
    raise NotImplementedError("Write fold_indices - see your task in Darbni")


def cross_validate(examples: list[dict], k: int) -> dict:
    """Score the baseline classifier with k-fold cross-validation."""
    raise NotImplementedError("Write cross_validate - see your task in Darbni")
