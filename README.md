# build_back_better_sentiment_analysis

Goal → Scrape a corpus of Tweets using Twitter API to understand people's
thoughts on President Biden’s Build Back Better Framework using dictionary-based
sentiment analysis. 

Twitter API & Search Query → I submitted the following query to the Twitter API 
to download 10,000 tweets associated with the following phrases: '"build back better"
OR "BBB" OR "spending bill" OR "reconciliation". This data was then downloaded
and saved as a csv.

Sentiment analysis → I used the University of Pittsburgh’s
Multi-Perspective Question Answering website (accessible here:
http://mpqa.cs.pitt.edu/). I cleaned my text data by removing stopwords (e.g., a, 
and, the, to, which our, etc.) and punctuation and then wrote the count_polarity
function to measure how many positive, negative, and neutral words appeared in 
my corpus. I also wrote a count words function that measures how often every word
in the corpus is used in the corpus. 

Data visualization → I used matplotlib to generate graphs of polarity data. 

The Multi-Perspective Question Answering Citation:

Theresa Wilson, Janyce Wiebe and Paul Hoffmann (2005). Recognizing Contextual
Polarity in Phrase-Level Sentiment Analysis. Proceedings of HLT/EMNLP 2005,
Vancouver, Canada.
