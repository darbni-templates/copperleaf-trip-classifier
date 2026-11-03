"""The prototype classifier: every word votes for the labels it was seen with.

Examples are {"text": "...", "label": "..."}. The model is plain JSON, so it can be saved.
"""

from trip_nlp.text import simple_words


def train_baseline(examples: list[dict]) -> dict:
    votes: dict[str, dict[str, int]] = {}
    counts: dict[str, int] = {}
    for example in examples:
        label = example["label"]
        counts[label] = counts.get(label, 0) + 1
        for word in set(simple_words(example["text"])):
            word_votes = votes.setdefault(word, {})
            word_votes[label] = word_votes.get(label, 0) + 1
    # Most common label, ties broken alphabetically. Used when no word is known.
    fallback = min(counts, key=lambda label: (-counts[label], label)) if counts else "other"
    return {"votes": votes, "fallback": fallback}


def predict_baseline(model: dict, text: str) -> str:
    scores: dict[str, int] = {}
    for word in simple_words(text):
        for label, n in model["votes"].get(word, {}).items():
            scores[label] = scores.get(label, 0) + n
    if not scores:
        return model["fallback"]
    return min(scores, key=lambda label: (-scores[label], label))
