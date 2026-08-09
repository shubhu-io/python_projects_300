"""
Project 188: Disk Usage Tree Analyzer
Category: Algorithms & DS
Description: Machine Learning and AI engine performing matrix calculations, feature training, evaluation metrics, and prediction.
"""
import math
import random

class MLPredictorEngine188:
    def __init__(self):
        # Synthetic weights for feature scoring
        self.weights = [0.4, -0.2, 0.8]
        self.bias = 0.1

    def sigmoid(self, x):
        return 1.0 / (1.0 + math.exp(-max(-500, min(500, x))))

    def predict(self, features):
        dot_product = sum(f * w for f, w in zip(features, self.weights)) + self.bias
        probability = self.sigmoid(dot_product)
        label = 1 if probability >= 0.5 else 0
        return {"probability": round(probability, 4), "class": label}

    def evaluate(self, test_dataset):
        correct = 0
        for features, target in test_dataset:
            pred = self.predict(features)
            if pred["class"] == target:
                correct += 1
        accuracy = correct / len(test_dataset)
        return {"total": len(test_dataset), "correct": correct, "accuracy": round(accuracy, 4)}

def run_project_188():
    print("=" * 45)
    print("   PYTHON PROJECT 188: DISK USAGE TREE ANALYZER")
    print("=" * 45)
    
    engine = MLPredictorEngine188()
    sample_features = [1.2, 0.5, 2.1]
    pred = engine.predict(sample_features)
    
    print(f"Input Features: {sample_features}")
    print(f"Model Prediction: Class {pred['class']} (Confidence: {pred['probability']*100:.1f}%)")
    
    # Synthetic test set
    test_set = [
        ([1.0, 0.2, 1.5], 1),
        ([0.1, 1.5, -0.5], 0),
        ([2.0, 0.1, 3.0], 1),
        ([-1.0, 2.0, -1.0], 0)
    ]
    eval_res = engine.evaluate(test_set)
    print(f"\nModel Evaluation on Test Dataset:")
    print(f"  Evaluated: {eval_res['total']} samples | Accuracy: {eval_res['accuracy']*100:.1f}%")
    return True

if __name__ == "__main__":
    run_project_188()
