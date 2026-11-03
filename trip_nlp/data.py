def split_train_test(requests: list[dict], test_every: int = 5) -> dict:
    """Split labelled requests into a training set and a test set.

    Every `test_every`-th request (the 5th, 10th, ... by default) goes to the test set, the
    rest to the training set. Both keep the original order.
    """
    train, test = [], []
    for i, request in enumerate(requests):
        if (i + 1) % test_every == 0:
            test.append(request)
        else:
            train.append(request)
    return {"train": train, "test": test}
