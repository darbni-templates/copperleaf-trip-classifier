STOPWORDS = {"a", "an", "the", "to", "i", "we", "my", "our", "is", "are", "for", "on", "in", "please"}


def prepare(text: str) -> list[str]:
    """Turn an inbox request into the words our models read."""
    # TODO(salma): every model needs a slightly different version of this. Split it up.
    words = text.split()
    lowered = []
    for w in words:
        lowered.append(w.lower())
    # punctuation around words
    stripped = []
    for w in lowered:
        w = w.strip(".,!?;:()\"'")
        if w != "":
            stripped.append(w)
    # links are never useful
    no_links = []
    for w in stripped:
        if w.startswith("http://") or w.startswith("https://") or w.startswith("www."):
            continue
        no_links.append(w)
    # email addresses are personal data: keep only that there was one
    masked = []
    for w in no_links:
        if "@" in w and "." in w.split("@")[-1]:
            masked.append("<email>")
        else:
            masked.append(w)
    # booking numbers, dates, prices: the exact number doesn't matter
    numbered = []
    for w in masked:
        if w.isdigit():
            numbered.append("<num>")
        else:
            numbered.append(w)
    result = []
    for w in numbered:
        if w not in STOPWORDS:
            result.append(w)
    final = []
    for w in result:
        if len(w) > 1:
            final.append(w)
    return final
