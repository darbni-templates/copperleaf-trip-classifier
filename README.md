# Copperleaf Digital trip-request classifier

Copperleaf Digital is an agency that builds customer-service assistants for travel clients:
tour operators, an airline, a rail company. Their inboxes get thousands of requests a week
("can I move my Lisbon trip to May?", "my bag never arrived"), and staff sort them by hand.
This repo is the classifier that will sort them for them.

The client's IT rules allow **only the Python standard library**: no scikit-learn, no numpy.
So we build the machine-learning parts ourselves, which is also the best way to understand them.

Some parts exist already (our first prototype), some are empty stubs waiting for you. You'll
work on it task by task, all in this one repo. Read the existing code before you change it:
other modules and other people's tasks depend on it.

## Your tasks
**Your exact task is in Darbni.** Open the task there and read its description: it has the
rules for YOUR version. Every intern gets their own version of each task, so a solution
copied from someone else will fail the tests.

## Where things are
| File | What it does |
|---|---|
| `trip_nlp/text.py` | the prototype's word splitter (used by the baseline) |
| `trip_nlp/baseline.py` | the prototype classifier: words vote for labels |
| `trip_nlp/labels.py` | maps the clients' inbox tags to our labels |
| `trip_nlp/data.py` | splits labelled requests into train and test |
| `trip_nlp/preprocess.py` | cleans a request into the words our models read |
| `trip_nlp/idf.py` | IDF weights: how rare is each word? |
| `trip_nlp/tokenizer.py` | the real tokenizer |
| `trip_nlp/vocabulary.py` | which words the models know |
| `trip_nlp/ngrams.py` | word pairs and negation as features |
| `trip_nlp/tfidf.py` | TF-IDF vectors |
| `trip_nlp/knn.py` | nearest-neighbour classifier |
| `trip_nlp/naive_bayes.py` | Naive Bayes classifier |
| `trip_nlp/threshold.py` | when to answer "unsure" |
| `trip_nlp/metrics.py` | confusion matrix and per-class scores |
| `trip_nlp/split.py` | stratified train/test split |
| `trip_nlp/cross_validation.py` | k-fold cross-validation |
| `trip_nlp/report.py` | the experiment report for the client |

## Run the tests
Only the Python standard library is used. You need pytest:
```
pip install pytest
pytest tests/test_tfidf.py        # the tests of the file your task is about
pytest                            # everything (tests for tasks you haven't done yet fail)
```
There is one example test per file. It works for every version, and it is far from enough:
write your own tests for the edge cases in your task. Darbni runs many more tests, made for
your version, when you submit.

## Submitting
Commit and push your work, then submit your repo URL and the full commit SHA in Darbni.
