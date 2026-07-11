# MedIntel

An AI-powered diabetes risk assessment application that combines machine learning with personalized health insights to support preventive healthcare. MedIntel provides risk prediction, explainable AI, tailored lifestyle recommendations, and actionable health plans to help users better understand and manage their diabetes risk.

---

## Overview

Diabetes is one of the fastest-growing chronic diseases worldwide, yet many people only become aware of their risk after developing serious health complications. Existing prediction tools often provide only a risk score without helping users understand what it means or what actions they should take.

MedIntel addresses this gap by combining an XGBoost-based prediction model with AI-generated explanations and personalized recommendations. Rather than simply predicting diabetes risk, the application helps users interpret their results and identify practical lifestyle changes that may improve their long-term health.

---

## Features

- AI-powered diabetes risk prediction
- Risk percentage and overall health score
- Explainable AI health summary
- Identification of key diabetes risk factors
- Personalized lifestyle recommendations
- Weekly health improvement plan
- Downloadable health report
- Curated educational resources on diabetes
- Healthcare provider search integration

---

## Application Workflow

1. Enter patient health information.
2. Generate a diabetes risk assessment using a trained machine learning model.
3. View an AI-generated explanation of the prediction.
4. Review personalized health recommendations.
5. Follow a structured weekly health improvement plan.
6. Download the generated health report for future reference.

---

## Technology Stack

**Frontend**
- Streamlit

**Machine Learning**
- XGBoost
- Scikit-learn

**Programming Language**
- Python

**Libraries**
- Pandas
- NumPy
- Joblib

---

## Project Structure

```
MedIntel/
│
├── app.py
├── utils.py
├── diabetes_model2.pkl
├── requirements.txt
├── README.md
└── assets/
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/konarsukanya/MedIntel.git
```

Navigate to the project directory:

```bash
cd MedIntel
```

Create a virtual environment:

```bash
python -m venv medintel
```

Activate the virtual environment.

Windows:

```bash
medintel\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Screenshots

Add screenshots of the application in the `assets` folder.

Suggested screenshots:

- Landing page
- Health assessment form
- AI health dashboard
- Personalized recommendations

---

## Future Enhancements

- Blood test report upload using OCR
- Long-term health progress tracking
- AI-powered health coach
- Wearable device integration
- Medication and appointment reminders
- Personalized behavior-change interventions
- User authentication and health history
- Enhanced recommendation personalization

---

## Motivation

MedIntel was inspired by my personal experience with pre-diabetes. Receiving a diagnosis often raises more questions than answers, and many people struggle to understand how to improve their health before diabetes develops.

The goal of this project is to move beyond prediction by providing users with meaningful explanations and practical guidance that encourage preventive healthcare and healthier lifestyle choices.

---

## Disclaimer

This application is intended for educational and research purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Users should consult qualified healthcare professionals regarding medical concerns and treatment decisions.

---

## Author

**Sukanya Konar**

Built as part of **Hack Your Summer 2026**.
