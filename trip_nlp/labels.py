"""Maps the tags our clients' staff put on inbox requests to the labels our models learn."""

LABEL_MAP = {
    "booking": "booking",
    "new booking": "booking",
    "reservation": "booking",
    "change": "change",
    "date change": "change",
    "reschedule": "change",
    "cancel": "cancel",
    "cancellation": "cancel",
    "refund": "refund",
    "money back": "refund",
    "baggage": "baggage",
    "luggage": "baggage",
    "lost bag": "baggage",
    "visa": "visa",
    "passport": "visa",
    "esta": "visa",
    "complaint": "other",
    "bad service": "other",
}


def map_label(raw: str) -> str:
    """The label for one inbox tag. Case and extra spaces don't matter; unknown tags are "other"."""
    return LABEL_MAP.get(" ".join(raw.lower().split()), "other")
