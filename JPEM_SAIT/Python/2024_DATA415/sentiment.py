import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# Load your CSV file
df = pd.read_csv('C:/JPEM_Git_Main/JPEM/JPEM_SAIT/data/DATA415_Text_Analytics_Assignment.csv')

def analyze_sentiment(review_text):
    sentiment_score = sia.polarity_scores(review_text)
    compound = sentiment_score['compound']
    
    # Customize thresholds for interpreting the compound score
    if compound >= 0.2:
        overall_sentiment = 'Positive'
    elif compound <= -0.2:
        overall_sentiment = 'Negative'
    else:
        overall_sentiment = 'Neutral'
    
    return {
        'negative': sentiment_score['neg'],
        'neutral': sentiment_score['neu'],
        'positive': sentiment_score['pos'],
        'compound': compound,
        'overall_sentiment': overall_sentiment
    }

# Apply sentiment analysis to each review
sentiment_results = df['Review Text'].apply(analyze_sentiment).apply(pd.Series)

# Merge results into the DataFrame
df = pd.concat([df, sentiment_results], axis=1)

# Save the results to a new CSV file
df.to_csv('hotel_reviews_with_custom_sentiment.csv', index=False)

# Display the DataFrame with sentiment analysis results
print(df.head())

# Calculate the percentage of each sentiment category
sentiment_counts = df['overall_sentiment'].value_counts(normalize=True) * 100

# Print the percentages of each sentiment category
print("Sentiment Percentages:")
print(sentiment_counts)




