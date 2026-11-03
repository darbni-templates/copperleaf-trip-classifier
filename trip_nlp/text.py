import re


def simple_words(text: str) -> list[str]:
    """The prototype's word splitter: lowercase runs of letters and digits.

    simple_words("Move my trip to May 3!") -> ["move", "my", "trip", "to", "may", "3"]
    """
    return re.findall(r"[a-z0-9]+", text.lower())
