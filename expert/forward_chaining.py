import pandas as pd

def build_forward_dict(csv_path):
    df = pd.read_csv(csv_path)
    symptom_columns = df.columns[:-1]
    forward_dict = {}

    for _, row in df.iterrows():
        disease = row['prognosis']
        for symptom in symptom_columns:
            if row[symptom] == 1:
                forward_dict.setdefault(symptom, []).append(disease)

    for k in forward_dict:
        forward_dict[k] = sorted(set(forward_dict[k]))

    return forward_dict

def diagnose_forward(symptoms, forward_dict):
    from collections import Counter
    disease_counter = Counter()

    for symptom in symptoms:
        disease_counter.update(forward_dict.get(symptom, []))

    total = sum(disease_counter.values())
    result = [(disease, round((count / total) * 100, 2)) for disease, count in disease_counter.items()]
    return sorted(result, key=lambda x: x[1], reverse=True)
