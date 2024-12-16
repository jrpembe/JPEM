from transformers import pipeline, AutoTokenizer
import torch
import pandas as pd

# Sentiment Analysis in Python using NLP Libraries(Transformer) Approach running on MPS(Apple's Metal Performance Shaders)

# Check if MPS is available and set the device accordingly
device = torch.device("mps") if torch.backends.mps.is_available() else torch.device("cpu")

# Initialize the sentiment analysis pipeline and tokenizer
sentiment_pipeline = pipeline("sentiment-analysis", device=device, truncation=True)
# alternative models:
# sentiment_pipeline = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
# sentiment_pipeline = pipeline("sentiment-analysis", model="finiteautomata/bertweet-base-sentiment-analysis")
# sentiment_pipeline = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")
# tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
tokenizer = AutoTokenizer.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")


# Load the Excel file from the given URL and read the first sheet
url = "https://dissidia.oss-cn-beijing.aliyuncs.com/test/20241031/Assignment_6_DataSheet.xlsx"
data = pd.read_excel(url, sheet_name=0)

# Check if the 'reviews.text' column exists
if 'reviews.text' not in data.columns:
    raise ValueError("The 'reviews.text' column is not found in the spreadsheet.")

# Define a function to truncate based on token count
def truncate_text(text, max_length=512):
    # Tokenize and truncate the text to 512 tokens
    tokens = tokenizer(text, truncation=True, max_length=max_length, return_tensors="pt")
    # Decode back to text
    truncated_text = tokenizer.decode(tokens['input_ids'][0], skip_special_tokens=True)
    return truncated_text

# Analyze each review and store the results
results = []
for index, row in data.iterrows():
    review = row['reviews.text']
    truncated_review = truncate_text(review)  # Ensure within token limit
    sentiment = sentiment_pipeline(truncated_review)[0]  # Access the first result
    results.append(sentiment)

# Add the results to the DataFrame
data['Sentiment'] = results

# Display the DataFrame
print(data[['reviews.text', 'Sentiment']])
# save the results to a new Excel file(just 'reviews.text', 'Sentiment' columns)
data[['reviews.text', 'Sentiment']].to_excel("nlp_sentiment_analysis_mps.xlsx", index=False)