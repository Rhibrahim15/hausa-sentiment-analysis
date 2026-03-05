import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# load dataset
df = pd.read_csv("data/hausa_sentiment.csv")

X = df["text"]
y = df["label"]

# convert text into numerical features
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X_vec, y, test_size=0.2, random_state=42
)

# train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# predictions
pred = model.predict(X_test)

print(classification_report(y_test, pred))

# save trained model
joblib.dump(model, "model/sentiment_model.pkl")

print("Model saved successfully")