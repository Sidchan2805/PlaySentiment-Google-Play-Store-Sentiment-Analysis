from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

def train_model(df):
    """
    Trains a Logistic Regression model on TF-IDF transformed text data.
    """
    print("🔄 Transforming text data into numerical features...")
    
    # Convert text into numerical vectors using TF-IDF
    vectorizer = TfidfVectorizer(max_features=2000)
    X = vectorizer.fit_transform(df['Cleaned_Review'])
    
    # Encode sentiment labels
    y = df['Sentiment'].map({'Positive': 1, 'Negative': 0, 'Neutral': 2})
    
    # Split dataset into training (80%) and testing (20%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train Logistic Regression model
    print("🔄 Training sentiment classification model...")
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Evaluate performance
    print("✅ Model trained successfully!")
    print(f"🎯 Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
    print("\n🔹 Classification Report:\n", classification_report(y_test, y_pred))
    
    return model, vectorizer
