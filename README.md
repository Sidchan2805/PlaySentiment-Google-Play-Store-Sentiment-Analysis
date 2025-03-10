# PlaySentiment-Google-Play-Store-Sentiment-Analysis
PlaySentiment is a sentiment analysis tool that examines user reviews from the Google Play Store and classifies them as Positive, Negative, or Neutral. Using Machine Learning (Logistic Regression) and Natural Language Processing (NLP), this project helps developers understand user feedback and improve their apps.
# 📊 PlaySentiment: Google Play Store Sentiment Analysis

🚀 **Analyze user sentiment in Google Play Store reviews using Machine Learning!**

![Sentiment Analysis](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Google_Play_Store_badge_EN.svg/512px-Google_Play_Store_badge_EN.svg.png?20210302213514)

## 📌 Overview
**PlaySentiment** is a sentiment analysis tool that examines user reviews from the **Google Play Store** and classifies them as **Positive, Negative, or Neutral**. Using **Machine Learning (Logistic Regression)** and **Natural Language Processing (NLP)**, this project helps developers understand user feedback and improve their apps.

✅ **Key Features**:
- 🔍 **Analyze Sentiments**: Classifies app reviews as Positive, Negative, or Neutral.
- 📊 **Visualize Sentiment Distribution**: Generates sentiment charts for easy understanding.
- 🔠 **Text Processing & Cleaning**: Removes noise from user reviews for accurate analysis.
- 🤖 **Machine Learning Model**: Trains a Logistic Regression model for classification.
- 📡 **Uses Real Google Play Data**: Fetches app reviews from a real dataset.

---

## 📂 Project Structure
PlaySentiment/ 

│── data/ 

│ └── user_reviews.csv # (Google Play Store reviews dataset)

│── src/

│ ├── data_loader.py # (Loads and cleans the dataset)

│ ├── preprocessing.py # (Text processing: stopwords removal, tokenization) 

│ ├── visualization.py # (Sentiment analysis plots) 

│ ├── model.py # (Trains and evaluates the ML model) 

│ ├── main.py # (Runs the full pipeline) 

│── requirements.txt # (Required Python libraries) 

│── README.md # (Project Overview & Instructions)


## Install Dependencies
pip install -r requirements.txt

## Run full sentiment analysis pipeline
python src/main.py
