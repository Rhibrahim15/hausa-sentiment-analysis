# hausa-sentiment-analysis
Machine learning project for sentiment analysis of Hausa text using TF-IDF and classification models.

# Hausa Sentiment Analysis using Machine Learning

This project builds a machine learning model to classify Hausa text sentiment.

The dataset used is from the NaijaSenti project which contains annotated Hausa tweets.

Example:

Ina son wannan fim → Positive  
Wannan abu ba shi da kyau → Negative  

Technologies Used

Python  
Pandas  
Scikit-learn  
NLTK  

Project Structure

data/ – raw dataset  
src/ – data preparation and model training scripts  
notebooks/ – exploratory data analysis  

Workflow

1. Load NaijaSenti dataset
2. Combine train, dev, and neutral datasets
3. Preprocess text
4. Convert text into TF-IDF features
5. Train sentiment classification model

Dataset Source

https://github.com/hausanlp/NaijaSenti

Goal

To explore Natural Language Processing techniques for African languages such as Hausa.