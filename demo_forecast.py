
# Retail Demand Forecasting Demo
# This demonstrates how to use the trained model

import pandas as pd
import joblib
import matplotlib.pyplot as plt

def load_and_predict():
    """Demo function to load model and make predictions"""
    try:
        # Load the trained model
        model = joblib.load('best_demand_model.pkl')
        print("✅ Model loaded successfully!")
        
        # Load metrics
        import json
        with open('model_metrics.json', 'r') as f:
            metrics = json.load(f)
        
        print(f"Best model: {metrics['best_model']}")
        print(f"Prophet RMSE: {metrics['prophet_rmse']:.2f}")
        print(f"LSTM RMSE: {metrics['lstm_rmse']:.2f}")
        
        # Show sample prediction
        print("\nThe model is ready for demand forecasting!")
        print("Use it to predict future sales and optimize inventory.")
        
    except Exception as e:
        print(f"Error loading model: {e}")

if __name__ == "__main__":
    load_and_predict()
