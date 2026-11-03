def confusion_matrix(gold: list[str], predicted: list[str]) -> dict:
    """Count which label was predicted for which correct label."""
    raise NotImplementedError("Write confusion_matrix - see your task in Darbni")


def per_class(gold: list[str], predicted: list[str]) -> dict:
    """Precision, recall and F-score of every label."""
    raise NotImplementedError("Write per_class - see your task in Darbni")
