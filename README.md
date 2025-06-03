# 🏦 Loan Approval Forecaster Web Application

This project is a **Flask-based web application** designed to predict whether a loan application will be approved based on user input. The app uses multiple machine learning models stored in a single `.pkl` file, providing flexibility in model selection and comparative analysis.

---

## 🚀 Features

- 🌐 Intuitive web interface built with **Flask**.
- 🧠 Supports **multiple ML models** dynamically loaded from a single `.pkl` file.
- 📊 Real-time loan approval forecaster based on financial and demographic input.
- ✅ Easy-to-use dropdowns and form controls for input features.
- ⚙️ Modular and extendable code structure for future improvements.

---

## 🧠 Models Used

The models are pre-trained and stored in a dictionary format inside a single pickle file (`Loan_Approval_Forecaster.pkl`). Each model is keyed by its name, allowing the user to select which one to use for prediction.

These could include:
- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost
- Support Vector Machine (SVM)

*Note: Actual models can be inspected in the `Loan Approval.ipynb` notebook.*

---

## 🛠 How It Works

1. The app loads all trained models from the `Loan_Approval_Forecaster.pkl` file on startup.
2. The user inputs details such as:
   - Gender
   - Marital Status
   - Education Level
   - Employment Type
   - Applicant & Coapplicant Income
   - Loan Amount
   - Loan Term
   - Credit History
   - Property Area
3. The selected model processes these inputs and predicts whether the loan will be **Approved** or **Rejected**.
4. The result is displayed dynamically on the same page.

---

## 🧩 Input Features Explained

| Feature              | Type      | Encoding/Range                            |
|----------------------|-----------|-------------------------------------------|
| Gender               | Categorical | Male: 1, Female: 0                        |
| Married              | Categorical | Yes: 1, No: 0                             |
| Education            | Categorical | Graduate: 1, Not Graduate: 0             |
| Self Employed        | Categorical | Yes: 1, No: 0                             |
| Applicant Income     | Numeric    | e.g., 5000                                |
| Coapplicant Income   | Numeric    | e.g., 2000                                |
| Loan Amount          | Numeric    | e.g., 150                                 |
| Loan Term            | Numeric    | e.g., 360 (months)                        |
| Credit History       | Binary     | Good: 1, Bad: 0                           |
| Property Area        | Categorical | Urban: 2, Semiurban: 1, Rural: 0        |

---

## 🖥️ Running the App Locally

> **Prerequisite:** Ensure Python is installed along with Flask and required ML libraries.

### 1. Install dependencies
```bash
pip install flask numpy scikit-learn
```
### 2. Start the Flask app
```bash
python app.py
```

### 3. Open in Browser
Navigate to: http://127.0.0.1:5000

---
### 📌 Notes
- The model file path in `app.py` is hardcoded:

```bash
"C:\\Users\\HP\\VS Code Projects\\Machine Learning\\Cross Validations\\Loan Approval Forecaster\\Loan_Approval_Forecaster.pkl"
```
🔧 You should replace this with a relative path or ensure it's configurable via environment variable or `config.py`.

- The app assumes binary classification output: `1` for approved, `0` for rejected.

- Exception handling is implemented to catch input errors or model prediction failures gracefully.

---
### Thank You
---

