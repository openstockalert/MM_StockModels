import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, mean_absolute_error
from sklearn.metrics import mean_squared_error, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
import matplotlib.pyplot as plt
import joblib

# Load the processed data
file_path = 'features/processed_data/prediction_data_01.csv'
df = pd.read_csv(file_path)


# Define features and target
features = [col for col in df.columns if col.startswith('VIX_') or col.startswith('FNG_')  or col.startswith('RSI_') or col.startswith('BB_')]
target_type = '1day'
target = f'S&P_{target_type}_up'  # Change to 'S&P_3day_up' or 'S&P_5day_up' as needed

X_future = df[features]
y_future = df[target]

# Prepare dataframe to store predictions
# predictions_df = X_future.copy()
predictions_df = pd.DataFrame()
predictions_df['True_Future'] = y_future

model_files = {
    "Logistic Regression": f"models/trained_models/Logistic Regression_{target_type}_model.pkl",
    "Random Forest": f"models/trained_models/Random Forest_{target_type}_model.pkl",
    "Support Vector Machine (SVM)": f"models/trained_models/Support Vector Machine (SVM)_{target_type}_model.pkl",
}

# Loop through models, load them, and predict
for name, file in model_files.items():
    print(f"Loading {name}...")
    
    # Load model
    model = joblib.load(file)
    
    # Predict probabilities and classes
    proba = model.predict_proba(X_future)
    class_preds = model.predict(X_future)
    
    # Add predictions to dataframe
    predictions_df[f"{name}_Probability_Up"] = proba[:, 1]
    predictions_df[f"{name}_Probability_Down"] = proba[:, 0]
    predictions_df[f"{name}_Prediction"] = class_preds
    predictions_df[f"{name}_Correct"] = (class_preds == y_future).astype(int)
    
    # Evaluate the model
    accuracy = accuracy_score(y_future, class_preds)
    print(f"{name} Accuracy: {accuracy:.2%}")
    print(classification_report(y_future, class_preds))

# Save predictions to a CSV file
predictions_df = predictions_df.round(2)
predictions_df.to_csv("models/predictions/future_predictions_by_models.csv", index=False)
print("Predictions saved to 'models/predictions/future_predictions_by_models.csv'")
