# Imports
from data_visualization import *

# Testing functions
def test_make_corpus_word_count_dict():
    """tests the make_corpus_word_count_dict function from viz.py"""
    # Empty Tweet Dict case
    test_dict = {}
    count_dict = make_corpus_word_count_dict(test_dict)
    assert count_dict == {}
    # Empty Tweet case
    test_dict = {"tweet1": {}, "tweet2": {"hi": 1, "world": 1}}
    count_dict = make_corpus_word_count_dict(test_dict)
    assert count_dict == {"hi": 1, "world": 1}
    # Repeating words in different Tweets to make sure they are all counted
    test_dict = {"tweet1": {"hi": 1, "there": 1}, "tweet2": {"hi": 1, "world": 1}}
    count_dict = make_corpus_word_count_dict(test_dict)
    assert count_dict == {"hi": 2, "there": 1, "world": 1}

def test_most_common():
    """tests the most_common function from viz.py"""
    # Test empty corpus dict
    corpus = {}
    num = 1
    result = most_common(corpus, num)
    assert result == {}
    # Test num = 0
    corpus = {"Hi": 4, "world": 2}
    num = 0
    result = most_common(corpus, num)
    assert result == {}
    # Test to get top word
    corpus = {"Hi": 4, "world": 2}
    num = 1
    result = most_common(corpus, num)
    assert result == {"Hi": 4}
    # Test to get top 2 words
    corpus = {"Hi": 4, "world": 2, "melon": 1}
    num = 2
    result = most_common(corpus, num)
    assert result == {"Hi": 4, "world": 2}
    # Test when num is greater than corpus length
    corpus = {"Hi": 4, "world": 2, "melon": 1}
    num = 4
    result = most_common(corpus, num)
    assert result == {"Hi": 4, "world": 2, "melon": 1}