import gradio as gr
import pickle
import numpy as np

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

def predict_diabetes(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):
    features = np.array([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]).reshape(1, -1)
    prediction = model.predict(features)
    risk = "Positive" if prediction[0] == 1 else "Negative"
    
    return f"Diabetes Risk: {risk}"

# Create Gradio interface
iface = gr.Interface(
    fn=predict_diabetes,
    inputs=[
        gr.Number(label="Pregnancies"),
        gr.Number(label="Glucose"),
        gr.Number(label="Blood Pressure"),
        gr.Number(label="Skin Thickness"),
        gr.Number(label="Insulin"),
        gr.Number(label="BMI"),
        gr.Number(label="Diabetes Pedigree Function"),
        gr.Number(label="Age")
    ],
    outputs="text",
    title="Diagenix - Diabetes Prediction Tool",
    description="Enter the details to predict diabetes risk.",
    theme="default",
    article="<p><a href='templates/about.html' target='_blank'>About Us</a></p><footer><p>&copy; 2024. .</p></footer>"
)

if __name__ == "__main__":
    iface.launch()
