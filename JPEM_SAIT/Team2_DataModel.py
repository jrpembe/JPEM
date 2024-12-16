import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import ADASYN
from imblearn.combine import SMOTETomek

# File path
file_path = r"C:/JPEM_Git_Main/JPEM/JPEM_SAIT/data/test.csv"

# Load dataset
data = pd.read_csv(file_path)

# Check for non-numeric columns and convert them to numeric if necessary
for column in data.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])

# Prepare the data
# Drop irrelevant columns
data = data.drop(columns=["company_name", "year"])  # Drop "company_name" and "year"

# Drop highly collinear variables (columns 14 and 17 by index)
data = data.drop(columns=[data.columns[14], data.columns[17]])

# Encode the target variable ("status_label")
data["status_label"] = LabelEncoder().fit_transform(data["status_label"])  # 0 for "alive", 1 for "failed"

# Split the dataset into features (X) and target (y)
X = data.drop(columns=["status_label"])
y = data["status_label"]

# Handle missing values
X = X.fillna(X.median())
y = y.fillna(y.median())

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# ---- Choose one of the following oversampling techniques ---- #

# Option 1: ADASYN
# adasyn = ADASYN(random_state=42)
# X_train_resampled, y_train_resampled = adasyn.fit_resample(X_train, y_train)

# Option 2: SMOTE + Tomek Links
# smote_tomek = SMOTETomek(random_state=42)
# X_train_resampled, y_train_resampled = smote_tomek.fit_resample(X_train, y_train)

# ---- Train and evaluate the model ---- #

# Train a Random Forest Classifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
print("Classification Report:/n", classification_report(y_test, y_pred))
cm = confusion_matrix(y_test, y_pred)
print("/nConfusion Matrix:/n", cm)

# Confusion matrix labels
TN, FP, FN, TP = cm.ravel()
print(f"/nTrue Negatives (TN): {TN}")
print(f"False Positives (FP): {FP}")
print(f"False Negatives (FN): {FN}")
print(f"True Positives (TP): {TP}")

# Feature Importance
importances = model.feature_importances_
features = X.columns
feature_importance = pd.DataFrame({'Feature': features, 'Importance': importances})

# Sort feature importance by importance value
feature_importance = feature_importance.sort_values(by='Importance', ascending=False)

# Bar chart for Feature Importance
plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=feature_importance, palette="viridis")
plt.title('Feature Importance')
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.show()
