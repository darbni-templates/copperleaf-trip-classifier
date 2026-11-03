from trip_nlp.labels import map_label


def test_booking_tags_stay_booking():
    assert map_label("  New   Booking ") == "booking"
