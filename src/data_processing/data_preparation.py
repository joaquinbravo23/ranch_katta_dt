import pandas as pd
import os
import nltk
from nltk import bigrams
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import SnowballStemmer

# Define the file name you want to read
FILE_NAME = 'hey_data.csv'

file_path = os.path.join(os.path.dirname(__file__), '../..', 'data', FILE_NAME)

# Read the CSV file
df = pd.read_csv(file_path)

df = df.drop('time', axis=1)

df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

#Function to clean the text to the dataframe
def preprocess_text(df, text_column):
    clean_text_column = f"{text_column}_cleaned"
    stemmer = SnowballStemmer('spanish', ignore_stopwords=True)
    
    #Function for cleaning a single text
    def clean_single_text(text):
        if not isinstance(text, str):
            return []

        text = text.lower()
        tokens = word_tokenize(text, language='spanish')
        tokens = [token for token in tokens if token.isalpha()]
        tokens = [token for token in tokens if not token.isdigit()]
        # tokens = [stemmer.stem(token) for token in tokens]
        tokens = [token for token in tokens if token not in stop_words]

        # Add bigrams to the list of tokens
        bigram_tokens = list(bigrams(tokens))
        tokens += [' '.join(bigram) for bigram in bigram_tokens]

        return tokens

    # Apply the cleaning function to the specified column
    df[clean_text_column] = df[text_column].apply(clean_single_text)

    return df

# Define custom stopwords and stop words
stop_words = set(stopwords.words('spanish'))

df = preprocess_text(df, "tweet")

print(df)