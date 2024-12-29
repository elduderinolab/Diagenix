import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the dataset
df = pd.read_csv('diabetes (1).csv')  # Adjust the path if necessary
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Calculate accuracy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=7)
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Model accuracy: {accuracy:.2f}")
