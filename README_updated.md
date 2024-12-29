# Diabetes-Prediction-using-Machine-Learning-Algorithms

Diabetes Prediction using Machine Learning Algorithms

In our project on "Diabetes Prediction using Machine Learning Algorithms," we followed a structured approach to build and evaluate different machine learning models for predicting diabetes. Here's a summary of our project:

**1. Exploratory Data Analysis and Data Visualization (EDA):**

     - I began by conducting EDA and data visualization to understand the dataset and its characteristics.

**2. Data Correlation:**

     - Then I analyzed the data correlation to identify relationships and dependencies among variables.

# Model Building     

**1. Random Forest Model:**

     - First built a machine-learning model using the Random Forest algorithm.
     
     - The model achieved an accuracy score of 0.802, indicating an 80.2% accuracy in diabetes prediction.
     
     - The precision, recall, and F1 scores for class 0 and class 1 were also presented.

**2. Decision Tree Model:**

     - Implemented a Decision Tree model for diabetes prediction.
     
     - The model achieved an accuracy score of 0.740, with associated precision, recall, and F1-score values.

**3. XGBoost Model:**

     - **Next,** we used the XGBoost classifier to create another predictive model.
     
     - The XGBoost model achieved an accuracy score 0.724, with precision, recall, and F1-score metrics provided.

**4. Support Vector Machine (SVM) Model:**

     - Then explored the Support Vector Machine as another modeling technique.
     
     - The SVM model achieved an accuracy score 0.755, with precision, recall, and F1-score metrics for both classes.

# Conclusion:

After evaluating these machine learning models, we concluded that the Random Forest model performed the best with an accuracy score of 0.78
This model is considered the most reliable for predicting diabetes based on your dataset.

We highlighted that the project not only focused on model building but also involved data analysis and visualization, enabling insights to be drawn from the data.
Our project showcases a systematic approach to solving a real-world problem using various machine learning algorithms, and the results suggest that the Random Forest model is the most suitable for predicting diabetes in your dataset due to its high accuracy.

## How to Use the Gradio Application

1. **Run the Application:**
   - Execute the command `python gradio_app_fixed.py` in your terminal to start the Gradio application.

2. **Access the Application:**
   - Open your web browser and navigate to `http://127.0.0.1:7860` to access the application interface.

3. **Input Data:**
   - Fill in the required fields with the following information:
     - **Pregnancies:** Number of times pregnant.
     - **Glucose:** Plasma glucose concentration a 2 hours in an oral glucose tolerance test.
     - **Blood Pressure:** Diastolic blood pressure (mm Hg).
     - **Skin Thickness:** Triceps skin fold thickness (mm).
     - **Insulin:** 2-Hour serum insulin (mu U/ml).
     - **BMI:** Body mass index (weight in kg/(height in m)^2).
     - **Diabetes Pedigree Function:** Diabetes pedigree function.
     - **Age:** Age (years).

4. **Get Prediction:**
   - Click the "Submit" button to receive the diabetes risk prediction based on the input data.

5. **View Results:**
   - The application will display whether the diabetes risk is "Positive" or "Negative."
