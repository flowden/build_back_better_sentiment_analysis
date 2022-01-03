# Imports
from methods import *

# Testing functions
def test_organize_dataframe():
    """tests the organize_dataframe function from methods.py"""
    # Checking that the correct headers are created in new dataframe
    data = [[0, "tweet!", "10-11-2020", "44", "user", "austin"]]
    df = pd.DataFrame(data, columns=["N", "text", "created_at", "likes_count", "username", "user_loc"])
    new_columns = []
    df_org = organize_dataframe(df)
    for col in df_org.columns:
        new_columns.append(col)
    assert new_columns == ["text", "created_at", "likes_count", "username", "user_loc", "ID"]
    # Length of dataframe stays the same when organizing it
    assert len(df_org) == 1
    # We cannot test an empty dataframe due to using pandas library
    

def test_count_words():
    """tests the count_words function from methods.py"""
    # Testing with no sent words and empty tweet
    sent_words = [""]
    data = [[1, ""]]
    df = pd.DataFrame(data, columns = ['ID', 'text'])
    assert(count_words(df, sent_words)) == {1: {}}
    # Testing with no sent words
    sent_words = [""]
    data = [[1, "I'm so happy I went to the store."]]
    df = pd.DataFrame(data, columns = ['ID', 'text'])
    assert(count_words(df, sent_words)) == {1: {}}
    # Testing with empty text
    sent_words = ["happy"]
    data = [[1, ""]]
    df = pd.DataFrame(data, columns = ['ID', 'text'])
    assert(count_words(df, sent_words)) == {1: {}}
    # Testing with no sent words
    sent_words = ["happy"]
    data = [[1, "I went to the store"]]
    df = pd.DataFrame(data, columns = ['ID', 'text'])
    assert(count_words(df, sent_words)) == {1: {}}
    # Testing with one sentiment word with single-word text
    sent_words = ["happy"]
    data = [[1, "happy"]]
    df = pd.DataFrame(data, columns = ['ID', 'text'])
    assert(count_words(df, sent_words)) == {1: {'happy': 1}}
    # Testing with one sentiment word with multi-word text
    sent_words = ["happy"]
    data = [[1, "happy feet is a good movie"]]
    df = pd.DataFrame(data, columns = ['ID', 'text'])
    assert(count_words(df, sent_words)) == {1: {'happy': 1}}
    # Testing with one sentiment word with multi-word text with repetition
    sent_words = ["happy"]
    data = [[1, "happy feet is a good movie. I'm so happy"]]
    df = pd.DataFrame(data, columns = ['ID', 'text'])
    assert(count_words(df, sent_words)) == {1: {'happy': 2}}
    # Testing with two sentiment words with multi-word text (one used)
    sent_words = ["happy", "sad"]
    data = [[1, "happy feet is a good movie"]]
    df = pd.DataFrame(data, columns = ['ID', 'text'])
    assert(count_words(df, sent_words)) == {1: {'happy': 1}}
    # Testing with two sentiment words with multi-word text (both used)
    sent_words = ["happy", "sad"]
    data = [[1, "happy feet is a good movie. I'm sad it's leaving theaters"]]
    df = pd.DataFrame(data, columns = ['ID', 'text'])
    assert(count_words(df, sent_words)) == {1: {'happy': 1, 'sad': 1}}
    # Testing with two sentiment words with multi-word text (both used)
    sent_words = ["happy", "sad"]
    data = [[1, "happy feet is a good movie. I'm sad it's leaving theaters"]]
    df = pd.DataFrame(data, columns = ['ID', 'text'])
    assert(count_words(df, sent_words)) == {1: {'happy': 1, 'sad': 1}}
    # Testing with two sentiment words with multi-word text (both used twice)
    sent_words = ["happy", "sad"]
    data = [[1, "happy feet is so happy. I'm sad it's sad too"]]
    df = pd.DataFrame(data, columns = ['ID', 'text'])
    assert(count_words(df, sent_words)) == {1: {'happy': 2, 'sad': 2}}
    # Testing with two tweets, one word
    sent_words = ["happy", "sad"]
    data = [[1, "happy feet is so happy. I'm sad it's sad too"],
        [2, "happy feet is an awful movie. I do not like it one bit."]]
    df = pd.DataFrame(data, columns = ['ID', 'text'])
    output = {1: {'happy': 2, 'sad': 2}, 2: {'happy': 1}}
    assert(count_words(df, sent_words)) == output
    # Testing with two tweets, two words
    sent_words = ["happy", "sad", "awful"]
    data = [[1, "happy feet is so happy. I'm sad it's sad too"],
        [2, "happy feet is an awful movie. I do not like it one bit."]]
    df = pd.DataFrame(data, columns = ['ID', 'text'])
    output = {1: {'happy': 2, 'sad': 2}, 2: {'happy': 1, 'awful': 1}}
    assert(count_words(df, sent_words)) == output
    # Testing with three tweets, multiple  words
    sent_words = ["happy", "sad", "awful"]
    data = [[1, "happy feet is so happy. I'm sad it's sad too"],
        [2, "happy feet is an awful movie. I do not like it one bit."],
        [3, "I do not like the movie happy feet."]]
    df = pd.DataFrame(data, columns = ['ID', 'text'])
    output = {1: {'happy': 2, 'sad': 2},
        2: {'happy': 1, 'awful': 1},
        3: {'happy': 1}}
    assert(count_words(df, sent_words)) == output

def test_count_polarity():
    """tests the count_polarity function from methods.py"""
    # Testing contents of default polarity dict
    polarity_dict = {"positive": 0, "neutral": 0, "negative": 0}
    assert(len(polarity_dict)) == 3
    assert(polarity_dict["positive"]) == 0
    assert(polarity_dict["neutral"]) == 0
    assert(polarity_dict["negative"]) == 0
    # Testing contents of empty input
    sent_dict = {1: {}}
    polarity_dict = count_polarity(sent_dict)
    assert(len(polarity_dict)) == 1
    assert(polarity_dict[1]["positive"]) == 0
    assert(polarity_dict[1]["neutral"]) == 0
    assert(polarity_dict[1]["negative"]) == 0
    # Testing contents of one Tweet one word input
    sent_dict = {1: {'happy': 1}}
    polarity_dict = count_polarity(sent_dict)
    assert(len(polarity_dict)) == 1
    assert(polarity_dict[1]["positive"]) == 1
    assert(polarity_dict[1]["neutral"]) == 0
    assert(polarity_dict[1]["negative"]) == 0
    # Testing contents of one Tweet one word (2x) input
    sent_dict = {1: {'happy': 2}}
    polarity_dict = count_polarity(sent_dict)
    assert(len(polarity_dict)) == 1
    assert(polarity_dict[1]["positive"]) == 2
    assert(polarity_dict[1]["neutral"]) == 0
    assert(polarity_dict[1]["negative"]) == 0
    # Testing contents of one Tweet two word input
    sent_dict = {1: {'happy': 1, 'sad': 1}}
    polarity_dict = count_polarity(sent_dict)
    assert(len(polarity_dict)) == 1
    assert(polarity_dict[1]["positive"]) == 1
    assert(polarity_dict[1]["neutral"]) == 0
    assert(polarity_dict[1]["negative"]) == 1
    # Testing contents of two Tweets two word input
    sent_dict = {1: {'happy': 1, 'sad': 1},
                2: {'happy': 1}}
    polarity_dict = count_polarity(sent_dict)
    assert(len(polarity_dict)) == 2
    assert(polarity_dict[1]["positive"]) == 1
    assert(polarity_dict[1]["neutral"]) == 0
    assert(polarity_dict[1]["negative"]) == 1
    assert(polarity_dict[2]["positive"]) == 1
    assert(polarity_dict[2]["neutral"]) == 0
    assert(polarity_dict[2]["negative"]) == 0
    # Testing contents of two Tweets with varied word input
    sent_dict = {1: {'happy': 1, 'sad': 2},
                2: {'happy': 2}}
    polarity_dict = count_polarity(sent_dict)
    assert(len(polarity_dict)) == 2
    assert(polarity_dict[1]["positive"]) == 1
    assert(polarity_dict[1]["neutral"]) == 0
    assert(polarity_dict[1]["negative"]) == 2
    assert(polarity_dict[2]["positive"]) == 2
    assert(polarity_dict[2]["neutral"]) == 0
    assert(polarity_dict[2]["negative"]) == 0
    # Testing contents of three Tweets with varied word input
    sent_dict = {1: {'happy': 1, 'sad': 2},
                2: {'happy': 2},
                3: {'sad': 4, 'angry': 2, 'evil': 1}}
    polarity_dict = count_polarity(sent_dict)
    assert(len(polarity_dict)) == 3
    assert(polarity_dict[1]["positive"]) == 1
    assert(polarity_dict[1]["neutral"]) == 0
    assert(polarity_dict[1]["negative"]) == 2
    assert(polarity_dict[2]["positive"]) == 2
    assert(polarity_dict[2]["neutral"]) == 0
    assert(polarity_dict[2]["negative"]) == 0
    assert(polarity_dict[3]["positive"]) == 0
    assert(polarity_dict[3]["neutral"]) == 0
    assert(polarity_dict[3]["negative"]) == 7