# -*- coding: utf-8 -*-
"""demo.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1teIZR5eCOGqDxtAh0Ib1ePTD0Pkxt_N_
"""

from google.colab import files

# Upload ransomware dataset
uploaded = files.upload()
ransomware_file = 'ransomware.csv'  # Name of the uploaded file

# Upload benign dataset
uploaded = files.upload()
benign_file = 'benign.csv'  # Name of the uploaded file

import pandas as pd

# Load ransomware dataset
ransomware_data = pd.read_csv(ransomware_file)

# Load benign dataset
benign_data = pd.read_csv(benign_file)

# Display the first few rows of each dataset
print("Ransomware Data:")
print(ransomware_data.head())

print("\nBenign Data:")
print(benign_data.head())

# Add labels
ransomware_data['label'] = 1  # 1 for ransomware
benign_data['label'] = 0      # 0 for benign

# Combine datasets
data = pd.concat([ransomware_data, benign_data], ignore_index=True)

# Display the first few rows of the combined dataset
print(data.head())

# Check for missing values
print(data.isnull().sum())

# Fill missing values with 0
data = data.fillna(0)

# Verify no missing values remain
print(data.isnull().sum())

from sklearn.preprocessing import MinMaxScaler

# Separate features (X) and labels (y)
X = data.drop('label', axis=1)
y = data['label']

# Normalize the features (scale to range [0, 1])
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Convert back to DataFrame (optional)
X_scaled = pd.DataFrame(X_scaled, columns=X.columns)

# Display the first few rows of the scaled data
print(X_scaled.head())

from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Display the shapes of the resulting datasets
print("Training features shape:", X_train.shape)
print("Testing features shape:", X_test.shape)

from sklearn.ensemble import RandomForestClassifier

# Initialize the model
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

from sklearn.metrics import accuracy_score, f1_score, cohen_kappa_score, classification_report, confusion_matrix, roc_auc_score, roc_curve
import matplotlib.pyplot as plt
import seaborn as sns

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Calculate F1 Score
f1 = f1_score(y_test, y_pred)
print("F1 Score:", f1)

# Calculate Cohen's Kappa
kappa = cohen_kappa_score(y_test, y_pred)
print("Cohen's Kappa:", kappa)

# Generate classification report
print("Classification Report:\n", classification_report(y_test, y_pred))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

# ROC-AUC
y_pred_proba = model.predict_proba(X_test)[:, 1]
roc_auc = roc_auc_score(y_test, y_pred_proba)
print("ROC-AUC Score:", roc_auc)

# ROC Curve
fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
plt.plot(fpr, tpr, label=f'ROC Curve (AUC = {roc_auc:.2f})')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.show()

import joblib

# Save the model to a file
joblib.dump(model, 'ransomware_detection_model.pkl')

# Download the model to your local machine
from google.colab import files
files.download('ransomware_detection_model.pkl')







