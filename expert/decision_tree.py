import pandas as pd
import joblib
import json

# Load trained models
clf = joblib.load('models/decision_tree_model.joblib')
label_encoder = joblib.load('models/label_encoder.joblib')

with open('models/feature_names.json') as f:
    all_symptoms = json.load(f)
def predict_decision_tree(symptoms, all_symptoms):
    input_data = pd.DataFrame([[1 if s in symptoms else 0 for s in all_symptoms]], columns=all_symptoms)
    prediction = clf.predict(input_data)[0]
    confidence = clf.predict_proba(input_data).max()
    return label_encoder.inverse_transform([prediction])[0], round(confidence * 100, 2)

def get_important_symptoms(top_n=10):
    importances = clf.feature_importances_
    symptom_importance = sorted(zip(all_symptoms, importances), key=lambda x: x[1], reverse=True)
    return symptom_importance[:top_n]
