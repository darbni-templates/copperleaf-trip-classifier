def decide(probs: dict) -> str:
    """The label to answer with, or the unsure label."""
    raise NotImplementedError("Write decide - see your task in Darbni")


def choose_threshold(dev: list[dict]) -> int:
    """The best threshold for a labelled dev set."""
    raise NotImplementedError("Write choose_threshold - see your task in Darbni")
