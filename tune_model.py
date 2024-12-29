import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score

# Load the dataset
df = pd.read_csv('diabetes (1).csv')  # Adjust the path if necessary
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=7)

# Hyperparameter tuning using GridSearchCV
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(RandomForestClassifier(), param_grid, cv=5)
grid_search.fit(X_train, y_train)

# Best model from grid search
best_model = grid_search.best_estimator_

# Save the best model
with open('model.pkl', 'wb') as file:
    pickle.dump(best_model, file)

# Calculate accuracy
predictions = best_model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Model saved successfully. Accuracy: {accuracy:.2f}")
