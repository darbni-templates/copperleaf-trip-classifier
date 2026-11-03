import math


def compute_idf(docs: list[list[str]]) -> dict:
    """The smoothed IDF of every term in `docs` (each doc is a list of tokens).

    idf(term) = ln((1 + n) / (1 + df)) + 1, where n is the number of documents and df the
    number of documents that contain the term. Rounded to 4 digits.
    """
    n = len(docs)
    df: dict[str, int] = {}
    for doc in docs:
        for term in doc:
            df[term] = df.get(term, 0) + 1
    return {term: round(math.log(1 + n / (1 + count)) + 1, 4) for term, count in df.items()}
