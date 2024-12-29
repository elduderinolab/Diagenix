import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load the dataset
df = pd.read_csv('diabetes (1).csv')  # Adjust the path if necessary
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# Train the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=7)
model = RandomForestClassifier(n_estimators=200)
model.fit(X_train, y_train)

# Save the model
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model saved successfully.")
