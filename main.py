from data_loader import load_data
from preprocessing import preprocess_reviews
from visualization import plot_sentiment_distribution
from model_train import train_model

# Define dataset URL
DATASET_URL = "https://raw.githubusercontent.com/amankharwal/Website-data/master/user_reviews.csv"

def main():
    """
    Runs the full sentiment analysis pipeline.
    """
    # Step 1: Load Dataset
    df = load_data(DATASET_URL)
    
    # Step 2: Preprocess Text
    df = preprocess_reviews(df)
    
    # Step 3: Visualize Sentiment Distribution
    plot_sentiment_distribution(df)
    
    # Step 4: Train Model
    train_model(df)

if __name__ == "__main__":
    main()
