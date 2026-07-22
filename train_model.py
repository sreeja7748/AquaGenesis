import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

# 1) Load your dataset
df = pd.read_csv("test.csv")

# 2) Drop empty rows (if any)
df = df.dropna(subset=["taxonomy", "sequence"])

# 3) Split train / test
X_train, X_test, y_train, y_test = train_test_split(
    df["sequence"], df["taxonomy"], test_size=0.2, random_state=42
)

# 4) Convert DNA letters into counts of k-mers (bag-of-words)
vectorizer = CountVectorizer(analyzer="char", ngram_range=(4, 4))  # 4-mers
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# 5) Train a simple Naive Bayes classifier
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# 6) Evaluate
pred = model.predict(X_test_vec)
print(classification_report(y_test, pred))

# 7) Save the model + vectorizer
joblib.dump((model, vectorizer), "silva_model.joblib")
print("✅ Model saved as silva_model.joblib")