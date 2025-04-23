# Disease Diagnosis Expert System

## Objective
Identify diseases from symptoms using rule-based logic

## Possible Computational Techniques
1. Forward chaining rules
2. Decision trees

## Flask UI Component
1. Checkboxes for symptoms
2. "Diagnose" button
3. result display

## Types of Dataset
1. Medical symptoms and disease correlations

## Possible Sources for Dataset
1. WHO
2. CDC
3. medical journals
4. Kaggle medical datasets

## Dataset URLs
1. https://www.who.int/data/gho
2. https://data.cdc.gov
3. https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset

## Setup Instructions
1. Medical Diagnosis Expert System
1. Create a Flask application with a form that includes checkboxes for common symptoms. 
2. Implement a rule-based expert system using forward chaining to map symptoms to diseases. 
3. Design a decision tree algorithm that processes the checked symptoms. 
4. Create a symptom-disease database from medical datasets. 
5. Handle errors from incomplete selections. 
6. Add a "Diagnose" button for analysis. 
7. Display confidence levels for each diagnosis. 
8. Add a medical disclaimer. 
9. Test with various verified symptom combinations.



# 🩺 Medical Diagnosis Expert System

This Flask-based expert system predicts diseases using two AI approaches:

- ✅ **Forward Chaining (Rule-Based)**
- ✅ **Decision Tree Classifier (Data-Driven)**

Users select symptoms from a checklist, and the system returns probable diseases with confidence levels.

---

## 🚀 Features

- ✔ Interactive web form with checkboxes for symptoms
- ✔ Single-page result display
- ✔ Uses both **rule-based inference** and **machine learning**
- ✔ Trained on a medically structured dataset
- ✔ Fast, lightweight, and responsive UI

---

## ⚙️ How to Run

### 🔧 Setup
bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# run application
bash
run "python app.py" and navigate to the specified url
