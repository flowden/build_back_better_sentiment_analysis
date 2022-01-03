# Imports
from methods import *
import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter

# Generating data for charts using functions from methods.py
total_word_count_output = count_words(tweets, sentiment_dict_keys)
total_polarity_output = count_polarity(total_word_count_output)

# Making charts with matplotlib.pyplot

# 1) Histogram -> Shows the distribution of polarity values of all Tweets
# Getting dictionary of all Tweets' polarity values
polarity_dict = {}
for tweet in total_polarity_output:
    sum = total_polarity_output[tweet]["total"]
    if sum not in polarity_dict:
        polarity_dict[sum] = 1
    else:
        polarity_dict[sum] = polarity_dict[sum] + 1

# Splitting dictionary into lists for x and y axes
sums = list(polarity_dict.keys())
counts = list(polarity_dict.values())

# Generating chart
plt.bar(sums,counts)
plt.xticks([i for i in range(min(sums), (max(sums)+1))])
plt.xlabel("Tweet Sentiment from Negative to Positive")
plt.ylabel("Number of Tweets")
plt.title("Overall Sentiments in Tweets")
plt.savefig("NEW_FINAL_test_overall_sentiment_counts.png")
plt.clf() # Clears figure before moving on


# 2) Bar Chart -> Shows the distribution of polarity by date
# Creating lists to hold polarity data
positive_sentiments = []
neutral_sentiments = []
negative_sentiments = []

# Generating total counts of positive, negative, and netural words in Tweets
for dataset in tweets_frames_cleaned:
    dataset_count_output = count_words(dataset, sentiment_dict_keys)
    dataset_polarity_output = count_polarity(dataset_count_output)

    total_positive = 0
    total_neutral = 0
    total_negative = 0

    for tweet in dataset_polarity_output:
        total_positive += dataset_polarity_output[tweet]["positive"]
        total_neutral += dataset_polarity_output[tweet]["neutral"]
        total_negative += dataset_polarity_output[tweet]["negative"]
    
    num_tweets = len(dataset_polarity_output)
    avg_positive = total_positive / num_tweets
    avg_neutral = total_neutral / num_tweets
    avg_negative = total_negative / num_tweets

    positive_sentiments.append(avg_positive)
    neutral_sentiments.append(avg_neutral)
    negative_sentiments.append(avg_negative)

# Generating chart with saved data
dates_x = ["nov 21-22", "dec 3-4", "dec 6-7"]
X = np.arange(len(dates_x))
width = 0.25
plt.style.use('Solarize_Light2')
plt.grid() # Adding grids to chart as a visual aid
plt.bar(X - width, positive_sentiments, color = 'b',
    width=width, label="Positive")
plt.bar(X, neutral_sentiments, color = 'g', width=width, label="Neutral")
plt.bar(X + width, negative_sentiments, color = 'r',
    width=width, label="Negative")
plt.xticks(ticks=X, labels=(dates_x))

# Adding a legend, axis labels, and title to the chart
plt.legend()
plt.title("Average Sentiment Occurrence by Date",
    fontsize='x-large', fontweight="roman")
plt.xlabel("Dates", fontsize='large', fontweight="medium")
plt.ylabel("Avg. Number of Occurrence", fontsize='large', fontweight="medium")
plt.savefig("NEW_FINAL_test_dataset_avg_sentiment.png")
plt.clf() # Clears figure before moving on


# 3) Bar chart -> Shows most frequently used sentiment words in corpus
# Generating list of word frequencies for all sentiment words in Tweets
def make_corpus_word_count_dict(dict):
    total_word_use = {}
    for tweet in dict:
        for word in dict[tweet]:
            if word not in total_word_use:
                total_word_use[word] = dict[tweet][word]
            else:
                total_word_use[word] += dict[tweet][word]
    return total_word_use

# Getting corpus-wide word count
corpus_word_count = make_corpus_word_count_dict(total_word_count_output)

# Finds the num most common words from the larger dictionary generated above
num = 20 # Number of favorite words to display in chart
def most_common(corpus, num):
    output = dict(sorted(corpus.items(),
        key = itemgetter(1), reverse = True)[:num])
    return output

# Applying most_common function to output from above
most_common_dict = most_common(corpus_word_count, num)

# Splitting dictionary into lists for x and y axes
common_words = list(most_common_dict.keys())
words_freq = list(most_common_dict.values())

# Generating chart
plt.bar(common_words,words_freq)
plt.xticks([i for i in range(num)], labels=common_words, rotation=45)
plt.xlabel("Sentiment Words") # Adding axis labels, title, and saving figure
plt.ylabel("Word Usage Frequency")
plt.title("Most Common Sentiment Words")
plt.savefig("NEW_FINAL_test_word_usage_freq_top_20.png")

print("complete!")