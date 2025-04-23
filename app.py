from dotenv import load_dotenv
from flask import Flask, render_template, request
import os
from expert.forward_chaining import build_forward_dict, diagnose_forward
from expert.decision_tree import predict_decision_tree
import json

load_dotenv()

app = Flask(__name__)
app.secret_key =  os.getenv('SECRET_KEY', 'default_secret_key')

# Load models and symptom list
FORWARD_DICT = build_forward_dict('data/cleaned/cleaned_training.csv')

with open('models/feature_names.json') as f:
    ALL_SYMPTOMS = json.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected = request.form.getlist('symptoms')
        if not selected:
            return render_template('index.html', symptoms=ALL_SYMPTOMS, error="⚠ Please select at least one symptom.")

        # Forward Chaining
        forward_results = diagnose_forward(selected, FORWARD_DICT)

        # Decision Tree
        decision_result, decision_conf = predict_decision_tree(selected, ALL_SYMPTOMS)
        

        return render_template('index.html',
                               symptoms=ALL_SYMPTOMS,
                               selected=selected,
                               forward=forward_results,
                               decision=(decision_result, decision_conf))

    return render_template('index.html', symptoms=ALL_SYMPTOMS)

if __name__ == '__main__':
    app.run(debug=True)