import matplotlib.pyplot as plt

def plot_sentiment_distribution(df):
    """
    Plots sentiment distribution in the dataset.
    """
    sentiment_counts = df['Sentiment'].value_counts()
    
    plt.figure(figsize=(8, 5))
    plt.bar(sentiment_counts.index, sentiment_counts.values, color=['green', 'red', 'blue'])
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.title("Distribution of Sentiments in Google Play Store Reviews")
    plt.show()
