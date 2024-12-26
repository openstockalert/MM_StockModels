import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
import matplotlib.pyplot as plt
import joblib

# Load the processed data
file_path = 'features/processed_data/feature_data_01.csv'
df = pd.read_csv(file_path)

# Calculate the number of rows to select for prediction data
num_rows = int(0.1 * len(df))

# Select the last 10% of rows as prediction data
prediction_data = df.tail(num_rows)

# Save the prediction data to a CSV file
prediction_data.to_csv('features/processed_data/prediction_data_01.csv', index=False)

# Select the remaining rows as training data
training_data = df.head(len(df) - num_rows)

# Define features and target
features = [col for col in df.columns if col.startswith('VIX_') or col.startswith('FNG_')  or col.startswith('RSI_') or col.startswith('BB_')]
target_type = '1day'
target = f'S&P_{target_type}_up'  # Change to 'S&P_3day_up' or 'S&P_5day_up' as needed


X = training_data[features]
y = training_data[target]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=False)

# Initialize models
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "Support Vector Machine (SVM)": svm.SVC(kernel='rbf', C=1, probability=True, random_state=42),
}

# Train and evaluate models
results = []
for name, model in models.items():
    # Train the model
    print(type(model))
    model.fit(X_train, y_train)
    
    # Predict on the test set
    y_pred = model.predict(X_test)
    # y_prob = model.predict_proba(X_test)[:, 1] if hasattr(model, "predict_proba") else None
    y_prob = model.predict_proba(X_test)[:, 1] if hasattr(model, "predict_proba") else model.decision_function(X_test) if isinstance(model, svm.SVC) else None

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_prob) if y_prob is not None else np.nan

    results.append({
        "Model": name,
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1,
        "ROC AUC": roc_auc
    })

    print(f"{name} Results:")
    print(f"  Accuracy: {accuracy:.4f}")
    print(f"  Precision: {precision:.4f}")
    print(f"  Recall: {recall:.4f}")
    print(f"  F1 Score: {f1:.4f}")
    print(f"  ROC AUC: {roc_auc:.4f}")
    print("-" * 40)

    joblib.dump(model, f'models/trained_models/{name}_{target_type}_model.pkl')

# Convert results to a DataFrame for comparison
results_df = pd.DataFrame(results)

# Plot model comparison
results_df.set_index("Model").plot(kind="bar", figsize=(10, 6), title="Model Performance Metrics")
plt.ylabel("Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
