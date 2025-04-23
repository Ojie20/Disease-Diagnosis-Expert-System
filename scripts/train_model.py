import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib
import os
import json

# Paths
DATA_PATH = os.path.join('data', 'cleaned', 'cleaned_training.csv')
MODEL_PATH = os.path.join('models', 'decision_tree_model.joblib')
ENCODER_PATH = os.path.join('models', 'label_encoder.joblib')

def train_model():
    # Load cleaned data
    df = pd.read_csv(DATA_PATH)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]  # remove unnamed cols if any

    # Features and label
    X = df.iloc[:, :-1]  # symptom columns
    y = df['prognosis']

    # Encode labels
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=0.2, random_state=42)

    # Train classifier
    clf = DecisionTreeClassifier(criterion='entropy', random_state=42)
    clf.fit(X_train, y_train)

    # Save models
    os.makedirs('models', exist_ok=True)
    joblib.dump(clf, MODEL_PATH)
    joblib.dump(le, ENCODER_PATH)

    with open('models/feature_names.json', 'w') as f:
        json.dump(X.columns.tolist(), f)

    print(f"✅ Model trained and saved to {MODEL_PATH}")
    print(f"✅ Label encoder saved to {ENCODER_PATH}")
    print(f"Training accuracy: {clf.score(X_train, y_train):.2f}")
    print(f"Test accuracy: {clf.score(X_test, y_test):.2f}")

if __name__ == '__main__':
    train_model()
