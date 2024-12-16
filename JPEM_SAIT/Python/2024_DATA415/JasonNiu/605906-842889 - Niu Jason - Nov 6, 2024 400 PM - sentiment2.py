import pandas as pd
import string
import pysentiment2 as ps

# Sentiment Analysis in Python using a Dictionary Approach
# Load the Excel file from the given URL and read the first sheet
url = "https://dissidia.oss-cn-beijing.aliyuncs.com/test/20241101/HotelReviews.xlsx"
df = pd.read_excel(url, sheet_name=0)

# Ensure the 'reviews.text' column exists
if 'reviews.text' not in df.columns:
    raise ValueError("The 'reviews.text' column is not present in the Excel sheet.")

# Initialize the sentiment analyzer
hiv4 = ps.HIV4()

# Function to preprocess and analyze sentiment
def analyze_sentiment(text):
    if pd.isna(text):
        return None, None, None
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Tokenize
    tokens = hiv4.tokenize(text)
    # Get sentiment scores
    score = hiv4.get_score(tokens)
    # Determine sentiment
    if score['Positive'] > score['Negative']:
        sentiment = 'Positive'
    elif score['Positive'] < score['Negative']:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    return score['Positive'], score['Negative'], sentiment

# Apply the function to each review
df[['Positive', 'Negative', 'Sentiment']] = df['reviews.text'].apply(
    lambda x: pd.Series(analyze_sentiment(x))
)

# Count the number of each sentiment
sentiment_counts = df['Sentiment'].value_counts()

# Determine overall feedback
if sentiment_counts.get('Positive', 0) > sentiment_counts.get('Negative', 0):
    overall_feedback = 'Positive'
elif sentiment_counts.get('Positive', 0) < sentiment_counts.get('Negative', 0):
    overall_feedback = 'Negative'
else:
    overall_feedback = 'Neutral'

# Output the results
print("Sentiment Counts:")
print(sentiment_counts)
print(f"Overall Feedback: {overall_feedback}")

# Save the results to a new Excel file
output_file_path = 'Sentiment_Analysis_Results.xlsx'
df.to_excel(output_file_path, index=False)