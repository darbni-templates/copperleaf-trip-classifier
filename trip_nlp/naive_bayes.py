def train(examples: list[dict]) -> dict:
    """Learn a multinomial Naive Bayes model."""
    raise NotImplementedError("Write train - see your task in Darbni")


def predict(model: dict, tokens: list[str]) -> dict:
    """The best label for `tokens`, with every label's score."""
    raise NotImplementedError("Write predict - see your task in Darbni")


def train_and_predict(examples: list[dict], docs: list[list[str]]) -> list[dict]:
    """Train on `examples`, then predict every doc."""
    raise NotImplementedError("Write train_and_predict - see your task in Darbni")


def probabilities(examples: list[dict], tokens: list[str]) -> dict:
    """Train on `examples`, then how likely each label is for `tokens`."""
    raise NotImplementedError("Write probabilities - see your task in Darbni")
