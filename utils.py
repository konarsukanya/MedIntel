import joblib
import numpy as np

# ============================
# Load Trained Model
# ============================

model = joblib.load("diabetes_model2.pkl")


# ============================
# Diabetes Prediction
# ============================

def predict_diabetes(
    pregnancies,
    glucose,
    blood_pressure,
    skin_thickness,
    insulin,
    bmi,
    pedigree,
    age
):
    """
    Predict diabetes using the trained ML model.
    Returns:
        prediction (0/1)
        probability (0-1)
    """

    patient = np.array([[
        pregnancies,
        glucose,
        blood_pressure,
        skin_thickness,
        insulin,
        bmi,
        pedigree,
        age
    ]])

    probability = model.predict_proba(patient)[0][1]
    prediction = model.predict(patient)[0]

    return prediction, probability


# ============================
# Risk Level
# ============================

def get_risk_level(probability):

    probability *= 100

    if probability < 30:
        return "🟢 Low Risk"

    elif probability < 70:
        return "🟡 Moderate Risk"

    else:
        return "🔴 High Risk"


# ============================
# Health Score
# ============================

def get_health_score(
    glucose,
    bmi,
    blood_pressure,
    age,
    pedigree
):

    score = 100

    if glucose >= 140:
        score -= 35
    elif glucose >= 100:
        score -= 20

    if bmi >= 30:
        score -= 20
    elif bmi >= 25:
        score -= 10

    if blood_pressure >= 90:
        score -= 15

    if age >= 45:
        score -= 10

    if pedigree >= 0.8:
        score -= 10

    return max(score, 0)
# ============================
# Identify Risk Factors
# ============================

def identify_risk_factors(glucose, bmi, age, blood_pressure):

    risks = []

    if glucose >= 140:
        risks.append("High Glucose")

    elif glucose >= 100:
        risks.append("Elevated Glucose")

    if bmi >= 30:
        risks.append("High BMI")

    elif bmi >= 25:
        risks.append("Overweight")

    if age >= 45:
        risks.append("Age Risk")

    if blood_pressure >= 90:
        risks.append("High Blood Pressure")

    return risks

# ============================
# AI Explanation
# ============================

def explain_prediction(risk_factors):

    if len(risk_factors) == 0:
        return (
            "Your health indicators are generally within healthy ranges. "
            "Keep maintaining a healthy lifestyle."
        )

    return (
        "The prediction was mainly influenced by: "
        + ", ".join(risk_factors) + "."
    )

# ============================
# Patient Persona
# ============================

def get_patient_persona(probability):

    probability *= 100

    if probability < 30:
        return "Healthy Lifestyle"

    elif probability < 70:
        return "Needs Lifestyle Improvements"

    else:
        return "High Risk Individual"

# ============================
# Personalized Recommendations
# ============================

# ============================
# Personalized Recommendations
# ============================

def get_personalized_recommendations(glucose, bmi, blood_pressure, age):

    recommendations = {
        "🥗 Nutrition": [],
        "🏃 Exercise": [],
        "🩺 Monitoring": [],
        "💧 Lifestyle": []
    }

    # Nutrition
    if glucose >= 140:
        recommendations["🥗 Nutrition"].append(
            "Reduce sugary drinks, sweets, and refined carbohydrates."
        )
        recommendations["🥗 Nutrition"].append(
            "Choose whole grains, vegetables, and high-fiber foods."
        )

    if bmi >= 30:
        recommendations["🥗 Nutrition"].append(
            "Follow portion-controlled, balanced meals."
        )

    # Exercise
    if bmi >= 25:
        recommendations["🏃 Exercise"].append(
            "Exercise for at least 30 minutes on most days."
        )
        recommendations["🏃 Exercise"].append(
            "Include strength training 2–3 times per week."
        )

    # Monitoring
    if blood_pressure >= 90:
        recommendations["🩺 Monitoring"].append(
            "Monitor your blood pressure regularly."
        )

    if glucose >= 140 or age >= 45:
        recommendations["🩺 Monitoring"].append(
            "Schedule regular diabetes screening and health check-ups."
        )

    # Lifestyle
    recommendations["💧 Lifestyle"].append(
        "Drink at least 2 liters of water daily."
    )

    recommendations["💧 Lifestyle"].append(
        "Aim for 7–8 hours of quality sleep every night."
    )

    recommendations["💧 Lifestyle"].append(
        "Practice stress management through meditation or yoga."
    )

    return recommendations

# def get_personalized_recommendations(
#     glucose,
#     bmi,
#     blood_pressure,
#     age
# ):

#     recommendations = []

#     if glucose >= 140:
#         recommendations.append(
#             "Reduce sugary drinks, sweets, and refined carbohydrates."
#         )

#     elif glucose >= 100:
#         recommendations.append(
#             "Monitor your sugar intake and choose whole grains."
#         )

#     if bmi >= 30:
#         recommendations.append(
#             "Aim for gradual weight loss through balanced meals and regular exercise."
#         )

#     elif bmi >= 25:
#         recommendations.append(
#             "Increase physical activity and watch portion sizes."
#         )

#     if blood_pressure >= 90:
#         recommendations.append(
#             "Reduce sodium intake and monitor your blood pressure regularly."
#         )

#     if age >= 45:
#         recommendations.append(
#             "Schedule regular health check-ups and diabetes screening."
#         )

#     recommendations.append(
#         "Exercise for at least 30 minutes on most days."
#     )

#     recommendations.append(
#         "Drink plenty of water and stay hydrated."
#     )

#     return recommendations

# ============================
# Health Priorities
# ============================

def get_health_priorities(risk_factors):

    priorities = []

    if "High Glucose" in risk_factors:
        priorities.append("Control Blood Sugar")

    if "High BMI" in risk_factors:
        priorities.append("Weight Management")

    if "High Blood Pressure" in risk_factors:
        priorities.append("Blood Pressure Monitoring")

    if "Age Risk" in risk_factors:
        priorities.append("Routine Health Checkups")

    return priorities

# ============================
# Weekly Health Plan
# ============================


def generate_weekly_plan(risk_factors):

    plan = {}

    if "High Glucose" in risk_factors:
        plan["Monday"] = "Avoid sugary drinks and walk for 30 minutes."
        plan["Tuesday"] = "Eat whole grains instead of refined carbohydrates."

    if "High BMI" in risk_factors:
        plan["Wednesday"] = "Complete a 45-minute brisk walk."
        plan["Thursday"] = "Prepare a balanced, low-calorie meal."

    if "High Blood Pressure" in risk_factors:
        plan["Friday"] = "Reduce salt intake and monitor your blood pressure."

    if "Age Risk" in risk_factors:
        plan["Saturday"] = "Schedule a routine health check-up."

    plan["Sunday"] = "Relax, stretch, and prepare healthy meals for the coming week."

    return plan

# ============================
# AI Health Summary
# ============================

def generate_health_summary(
    prediction,
    probability,
    risk_factors
):

    probability = probability * 100

    if prediction == 1:
        return (
            f"Based on your health information, your estimated diabetes risk is {probability:.1f}%. "
            f"The main contributing factors are {', '.join(risk_factors)}. "
            "Making gradual improvements in these areas may help reduce your future diabetes risk."
        )

    return (
        "Your current health indicators suggest a relatively low diabetes risk. "
        "Continue maintaining healthy habits and schedule routine health check-ups."
    )

# ============================
# Complete Patient Analysis
# ============================

def analyze_patient(
    pregnancies,
    glucose,
    blood_pressure,
    skin_thickness,
    insulin,
    bmi,
    pedigree,
    age
):

    # Prediction
    prediction, probability = predict_diabetes(
        pregnancies,
        glucose,
        blood_pressure,
        skin_thickness,
        insulin,
        bmi,
        pedigree,
        age
    )

    # Analysis
    risk_level = get_risk_level(probability)
    #health_score = get_health_score(probability)
    health_score = get_health_score(
    glucose,
    bmi,
    blood_pressure,
    age,
    pedigree
    )

    risk_factors = identify_risk_factors(
        glucose,
        bmi,
        age,
        blood_pressure
    )

    explanation = explain_prediction(risk_factors)

    persona = get_patient_persona(probability)
    summary = generate_health_summary(
    prediction,
    probability,
    risk_factors
)

    recommendations = get_personalized_recommendations(
        glucose,
        bmi,
        blood_pressure,
        age
    )

    priorities = get_health_priorities(risk_factors)

    #weekly_plan = generate_weekly_plan()
    weekly_plan = generate_weekly_plan(risk_factors)

    return {

        #"prediction": "Likely Diabetic" if prediction == 1 else "Low Diabetes Risk",
        
        "prediction": "High Diabetes Risk" if prediction == 1 else "Low Diabetes Risk",

        "risk_percentage": round(float(probability) * 100, 2),

        "risk_level": risk_level,

        "health_score": health_score,

        "risk_factors": risk_factors,

        "explanation": explanation,

        "persona": persona,
        
        "summary": summary,

        "recommendations": recommendations,

        "priorities": priorities,

        "weekly_plan": weekly_plan
    }