import csv
from flask import Flask, render_template, request

app = Flask(__name__)

#  Define some example rules
# RULES = {
#     "Flu": {"fever", "cough", "body ache", "runny nose"},
#     "Common Cold": {"cough", "sneezing", "runny nose"},
#     "Malaria": {"fever", "chills", "sweating"},
#     "COVID-19": {"fever", "cough", "loss of taste", "shortness of breath"}
# }

#  List of possible symptoms
# SYMPTOMS = sorted({symptom for symptoms in RULES.values() for symptom in symptoms})

# Load the rules from the CSV
RULES = {}
SYMPTOMS = set()

with open('disease_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        disease = row['disease']
        symptoms_list = row['symptoms'].split(';')
        RULES[disease] = set(symptoms_list)
        SYMPTOMS.update(symptoms_list)

SYMPTOMS = sorted(SYMPTOMS)  


@app.route('/', methods=['GET', 'POST'])
def index():
    diagnosis = None
    error_message = None
    confidence_levels = {}

    if request.method == 'POST':
        selected_symptoms = set(request.form.getlist('symptoms'))

        if not selected_symptoms:
            error_message = "Please select at least one symptom before diagnosing."
        else:
            for disease, disease_symptoms in RULES.items():
                match_count = len(disease_symptoms.intersection(selected_symptoms))
                total_symptoms = len(disease_symptoms)
                confidence = (match_count / total_symptoms) * 100
                if match_count > 0:
                    confidence_levels[disease] = round(confidence, 2)

            if confidence_levels:
                # Pick the disease with the highest confidence as the 'main' diagnosis
                diagnosis = max(confidence_levels, key=confidence_levels.get)
            else:
                diagnosis = "No clear diagnosis. Please consult a doctor."

    return render_template('index.html', symptoms=SYMPTOMS, diagnosis=diagnosis, error_message=error_message, confidence_levels=confidence_levels)


if __name__ == '__main__':
    app.run(debug=True)
