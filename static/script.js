document.getElementById('prediction-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const features = [
        parseFloat(document.getElementById('Pregnancies').value),
        parseFloat(document.getElementById('Glucose').value),
        parseFloat(document.getElementById('BloodPressure').value),
        parseFloat(document.getElementById('SkinThickness').value),
        parseFloat(document.getElementById('Insulin').value),
        parseFloat(document.getElementById('BMI').value),
        parseFloat(document.getElementById('DiabetesPedigreeFunction').value),
        parseFloat(document.getElementById('Age').value)
    ];

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ features: features })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = 'Prediction: ' + (data.prediction === 1 ? 'Diabetic' : 'Not Diabetic');
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
