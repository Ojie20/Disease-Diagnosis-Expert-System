import unittest
from expert.forward_chaining import build_forward_dict, diagnose_forward
from expert.decision_tree import predict_decision_tree
import os
import json
class TestExpertSystem(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.csv_path = 'data/cleaned/cleaned_training.csv'
        cls.forward_dict = build_forward_dict(cls.csv_path)
        with open('models/feature_names.json') as f:
            cls.all_symptoms = json.load(f)
        

    def test_forward_chaining(self):
        result = diagnose_forward(['fatigue', 'high_fever'], self.forward_dict)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        self.assertIsInstance(result[0], tuple)

    def test_decision_tree(self):
        disease, confidence = predict_decision_tree(['fatigue', 'high_fever'], self.all_symptoms)
        self.assertIsInstance(disease, str)
        self.assertTrue(0 <= confidence <= 100)

    def test_empty_forward_chaining(self):
        result = diagnose_forward([], self.forward_dict)
        self.assertEqual(result, [])

    def test_invalid_symptom_decision_tree(self):
        disease, confidence = predict_decision_tree(['invalid_symptom'], self.all_symptoms)
        self.assertIsInstance(disease, str)

if __name__ == '__main__':
    unittest.main()