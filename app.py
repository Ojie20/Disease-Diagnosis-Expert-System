from flask import Flask, render_template, request

app = Flask(__name__)

# Define some example rules
RULES = {
    "Flu": {"fever", "cough", "body ache", "runny nose"},
    "Common Cold": {"cough", "sneezing", "runny nose"},
    "Malaria": {"fever", "chills", "sweating"},
    "COVID-19": {"fever", "cough", "loss of taste", "shortness of breath"}
}

# List of possible symptoms
SYMPTOMS = sorted({symptom for symptoms in RULES.values() for symptom in symptoms})

@app.route('/', methods=['GET', 'POST'])
def index():
    diagnosis = None
    if request.method == 'POST':
        selected_symptoms = set(request.form.getlist('symptoms'))
        for disease, disease_symptoms in RULES.items():
            if disease_symptoms.issubset(selected_symptoms):
                diagnosis = disease
                break
        if not diagnosis:
            diagnosis = "No clear diagnosis. Please consult a doctor."
    return render_template('index.html', symptoms=SYMPTOMS, diagnosis=diagnosis)

if __name__ == '__main__':
    app.run(debug=True)
