from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load all models from the pickle file
with open(r"C:\Users\HP\VS Code Projects\Machine Learning\Cross Validations\Loan Approval Forecaster\Loan_Approval_Forecaster.pkl", "rb") as f:
    models = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    selected_model = None

    if request.method == "POST":
        try:
            # Collect input data
            gender = 1 if request.form['gender'] == 'Male' else 0
            married = 1 if request.form['married'] == 'Yes' else 0
            education = 1 if request.form['education'] == 'Graduate' else 0
            self_employed = 1 if request.form['self_employed'] == 'Yes' else 0
            applicant_income = float(request.form['applicant_income'])
            coapplicant_income = float(request.form['coapplicant_income'])
            loan_amount = float(request.form['loan_amount'])
            loan_term = float(request.form['loan_term'])
            credit_history = 1 if request.form['credit_history'] == 'Good' else 0
            property_area = {"Urban": 2, "Semiurban": 1, "Rural": 0}[request.form['property_area']]

            # Select model
            selected_model = request.form["model"]
            model = models[selected_model]

            # Feature vector (adjust this to your model's expectations)
            input_data = np.array([[gender, married, education, self_employed,
                                    applicant_income, coapplicant_income, loan_amount,
                                    loan_term, credit_history, property_area]])

            # Make prediction
            pred = model.predict(input_data)
            prediction = "Approved" if pred[0] == 1 else "Rejected"
        except Exception as e:
            prediction = f"Error: {e}"

    return render_template("index.html", prediction=prediction, models=models.keys(), selected_model=selected_model)

if __name__ == "__main__":
    app.run(debug=True)

