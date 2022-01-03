# Imports
from numpy import negative, positive
import pandas as pd
from pandas.core.frame import DataFrame

# Loading our data
# Dictionaries downloaded from University of Pittsburg: http://mpqa.cs.pitt.edu/
subjectivity_dictionary = "subjectivity_dict.tff"
necessities_dictionary = "necessity.tff"
current_dict = subjectivity_dictionary

# Processing subjectivity_dictionary tff file into usable data
sentiment_dict = {}
with open(current_dict, mode='r') as file:
    lines = file.readlines()
    for row in lines:
        temp_dict = {}
        temp_list = row.split()
        temp_dict["type"] = temp_list[0].split("=")[1]
        temp_dict["len"] = temp_list[1].split("=")[1]
        temp_dict["word"] = temp_list[2].split("=")[1]
        temp_dict["pos"] = temp_list [3].split("=")[1]
        temp_dict["stemmed"] = temp_list[4].split("=")[1]
        temp_dict["polarity"] = temp_list[5].split("=")[-1]
        sentiment_dict[temp_dict["word"]] = temp_dict

# Importing SOME Tweets we've saved in CSVs with our scraper.py function
# tweets_nov_22 = pd.read_csv("tweets-10000-11_22.csv", nrows = 10)
# tweets_dec_4 = pd.read_csv("tweets-10000-12_4(1).csv", nrows = 10)
# tweets_dec_7 = pd.read_csv("tweets-10000-12_7.csv", nrows = 10)

# Importing ALL Tweets we've saved in CSVs with our scraper.py function
tweets_nov_22 = pd.read_csv("tweets-10000-11_22.csv")
tweets_dec_4 = pd.read_csv("tweets-10000-12_4(1).csv")
tweets_dec_7 = pd.read_csv("tweets-10000-12_7.csv")

# Joining all smaller Tweet dataframes
tweets_frames = [tweets_nov_22, tweets_dec_4, tweets_dec_7]
tweets_frames_cleaned = []

############# Quick check of data error in one of our csv files ################
# dec4_1_ids = (len(tweets_dec_4["text"].unique()))
# dec4_ids = (len(tweets_dec_4_W["text"].unique()))
# print("{} has {} unique IDs".format("tweets-10000-12_4(1).csv", dec4_1_ids))
# print("{} has {} unique IDs".format("tweets-10000-12_4.csv", dec4_ids))
# printout:
    # tweets-10000-12_4(1).csv has 10000 unique IDs
    # tweets-10000-12_4.csv has 48 unique IDs
################################################################################

# Cleaning our data
def organize_dataframe(dataframe):
    """standardizes dataframe column names"""
    dataframe = dataframe.rename(columns={"text": "id", "N": "text"})
    dataframe["ID"] = dataframe["id"]
    dataframe = dataframe.set_index("id")
    return(dataframe)

# Standardizing dataframe that represents each CSV file
for dataframe in tweets_frames:
    dataframe = organize_dataframe(dataframe)
    tweets_frames_cleaned.append(dataframe)

# Creating our larger corpus
tweets = pd.concat(tweets_frames_cleaned)

# Creating variables to store data created below
sentiment_dict_keys = []
polarity_dict = {}

# Getting a list of keys in downloaded sentiment_dictionary
for key in sentiment_dict:
    sentiment_dict_keys.append(key)

# Functions
def count_words(corpus: DataFrame, sent_words: dict) -> dict:
    """counts num words in an entire corpus in an inputted dictionary"""
    all_tweet_data = {}
    # Iterating through all Tweets in our corpus
    for tweet in corpus.iterrows():
        word_counts = {}
        tweet_id = int(tweet[1]["ID"])
        # Cleaning the text
        tweet_text = tweet[1]["text"]
        tweet_text = tweet_text.lower() # Converting all text to lowercase
        punctuation= '''!()-[]{;}:'", <>./?@#$%^&*_~'''
        for x in punctuation:
            tweet_text = tweet_text.replace(x, " ")
        tweet_as_list = tweet_text.split()
        for word in tweet_as_list:
            if word not in {"build", "back", "better", "BBB", "spending", "bill", "reconciliation"}:
                if word in sent_words:
                    if word not in word_counts:
                        word_counts[word] = 1
                    else:
                        word_counts[word] = word_counts[word] + 1
                else:
                    continue
        all_tweet_data[tweet_id] = word_counts
    return(all_tweet_data)

def count_polarity(words_dict) -> dict:
    """counts polarity of each word in sent words for each Tweet in corpus"""
    all_polarities = {}
    for tweet_ID in words_dict:
        polarity_dict = {"positive": 0, "neutral": 0, "negative": 0}
        for word in words_dict[tweet_ID]:
            sentiment = sentiment_dict[word]["polarity"]
            word_count = words_dict[tweet_ID][word]
            if sentiment == "positive":
                polarity_dict["positive"] = polarity_dict["positive"] + word_count
            elif sentiment == "neutral":
                polarity_dict["neutral"] = polarity_dict["neutral"] + word_count
            else: # when sentiment == "negative"
                polarity_dict["negative"] = polarity_dict["negative"] + word_count
        all_polarities[tweet_ID] = polarity_dict
        for tweet_ID in all_polarities:
            sum = all_polarities[tweet_ID]["positive"] - all_polarities[tweet_ID]["negative"]
            all_polarities[tweet_ID]["total"] = sum
    return all_polarities