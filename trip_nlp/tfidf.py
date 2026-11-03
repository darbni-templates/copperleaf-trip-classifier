class TfidfVectorizer:
    """Learns IDF weights from training documents, then turns documents into TF-IDF vectors."""

    def fit(self, docs: list[list[str]]) -> "TfidfVectorizer":
        raise NotImplementedError("Write TfidfVectorizer - see your task in Darbni")

    def transform(self, docs: list[list[str]]) -> list[dict[str, float]]:
        raise NotImplementedError("Write TfidfVectorizer - see your task in Darbni")


def run_vectorizer(train_docs: list[list[str]], test_docs: list[list[str]]) -> list[dict]:
    """Fit on train_docs, then transform test_docs."""
    raise NotImplementedError("Write run_vectorizer - see your task in Darbni")


def fitted_idf(train_docs: list[list[str]]) -> dict:
    """Fit on train_docs, then return the learned IDF of every term."""
    raise NotImplementedError("Write fitted_idf - see your task in Darbni")
