import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

def clean_text(text: str):
    """
    Cleans text by removing punctuation, special characters, and stopwords.
    """
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    words = text.split()
    words = [word for word in words if word not in stopwords.words('english')]
    return ' '.join(words)

def preprocess_reviews(df):
    """
    Applies text cleaning to the dataset.
    """
    print("🔄 Cleaning text data...")
    df['Cleaned_Review'] = df['Translated_Review'].astype(str).apply(clean_text)
    print("✅ Text cleaning completed!")
    return df
