import streamlit as st
from utils import analyze_patient

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="MedIntel",
    page_icon="🩺",
    layout="wide"
)

# ==========================================
# Custom CSS
# ==========================================

st.markdown("""
<style>

.stApp{
    background-color:#F5F9FC;
}

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
    max-width:1200px;
}

.hero{
    background: linear-gradient(135deg,#1565C0,#42A5F5);
    padding:35px;
    border-radius:20px;
    color:white;
    margin-bottom:25px;
}

.hero h1{
    color:white;
    margin-bottom:10px;
}

.hero p{
    font-size:18px;
}

.card{
    background:white;
    padding:20px;
    border-radius:18px;
    box-shadow:0px 5px 20px rgba(0,0,0,0.08);
    margin-bottom:20px;
}

div[data-testid="metric-container"]{
    background:white;
    border-radius:18px;
    padding:20px;
    border:none;
    box-shadow:0px 4px 15px rgba(0,0,0,0.08);
}

.stButton>button{
    width:100%;
    height:55px;
    background:#1565C0;
    color:white;
    border:none;
    border-radius:12px;
    font-size:18px;
    font-weight:600;
}

.stButton>button:hover{
    background:#0D47A1;
    color:white;
}

</style>
""", unsafe_allow_html=True)

with st.sidebar:

    st.title("🩺 MedIntel")

    st.markdown("---")

    st.subheader("About")

    st.write(
        """
Estimate diabetes risk using AI and receive
personalized health insights and lifestyle
recommendations.
"""
    )

    st.markdown("---")

    st.subheader("Features")

    st.write("✅ Diabetes Risk Prediction")

    st.write("✅ Health Score")

    st.write("✅ Risk Analysis")

    st.write("✅ Personalized Recommendations")

    st.write("✅ Weekly Health Plan")

    st.markdown("---")

    st.caption("Built with ❤️ using Streamlit + XGBoost")
    
st.markdown("""
<div class="hero">

<h1>🩺 MedIntel</h1>

<h3>Your Personal AI Health Companion</h3>

<p>
Understand your diabetes risk with AI-powered insights,
personalized recommendations,
and practical lifestyle guidance.
</p>

</div>
""", unsafe_allow_html=True)


    
# ==========================================================
# Health Assessment Form
# ==========================================================

st.header("📝 Health Assessment")

st.caption("Enter your health information")

# --------------------------
# Basic Information
# --------------------------

st.subheader("👤 Basic Information")
st.info(
    "Complete the information below to receive an AI-powered diabetes risk assessment. "
    "Fields under 'Advanced Health Measurements' are optional and can be left at their default values if unknown."
)
col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=30
    )

with col2:

    pregnancies = st.number_input(
        "Number of Pregnancies",
        min_value=0,
        max_value=20,
        value=1,
        help="If not applicable, leave this as 0."
    )

family_history = st.selectbox(
    "Family History of Diabetes",
    [
        "No known family history",
        "One parent or sibling",
        "Multiple close relatives",
        "Strong family history"
    ],
    help="We'll estimate the Diabetes Pedigree Function used by the AI model based on your family history."
)

pedigree_map = {
    "No known family history": 0.15,
    "One parent or sibling": 0.45,
    "Multiple close relatives": 0.75,
    "Strong family history": 1.10
}

pedigree = pedigree_map[family_history]

st.divider()

# --------------------------
# Health Measurements
# --------------------------

st.subheader("🩺 Health Measurements")

col1, col2 = st.columns(2)

with col1:

    glucose = st.number_input(
        "Fasting Blood Glucose (mg/dL)",
        min_value=0,
        max_value=300,
        value=120,
        help="Normal fasting blood glucose is generally below 100 mg/dL."
    )

    bmi = st.number_input(
        "Body Mass Index (BMI)",
        min_value=0.0,
        max_value=70.0,
        value=25.0,
        step=0.1,
        help="BMI is calculated from your height and weight."
    )

with col2:

    blood_pressure = st.number_input(
        "Diastolic Blood Pressure (mmHg)",
        min_value=0,
        max_value=200,
        value=80,
        help="Enter the bottom number of your blood pressure. Example: if your BP is 120/80, enter 80."
    )

st.divider()

# --------------------------
# Advanced Measurements
# --------------------------

with st.expander("⚙️ Advanced Health Measurements (Optional)"):

    st.caption(
        "These measurements are commonly available from laboratory reports. "
        "If you don't know them, you can leave the default values."
    )

    col1, col2 = st.columns(2)

    with col1:

        skin_thickness = st.number_input(
            "Triceps Skin Fold Thickness (mm)",
            min_value=0,
            max_value=100,
            value=20
        )

    with col2:

        insulin = st.number_input(
            "Insulin Level (μU/mL)",
            min_value=0,
            max_value=900,
            value=80
        )

st.write("")

if st.button("Generate My Health Report"):
    
    st.session_state["report"] = analyze_patient(
        pregnancies,
        glucose,
        blood_pressure,
        skin_thickness,
        insulin,
        bmi,
        pedigree,
        age
    )

if "report" in st.session_state:

    report = st.session_state["report"]
    
    
    st.divider()

    st.header("📊 Your AI Health Dashboard")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "🩺 Prediction",
            report["prediction"]
        )

    with c2:
        st.metric(
            "📈 Diabetes Risk",
            f"{report['risk_percentage']:.1f}%"
        )
        st.progress(report["risk_percentage"] / 100)

    with c3:
        st.metric(
            "❤️ Health Score",
            f"{report['health_score']}/100"
        )
        st.progress(report["health_score"] / 100)

    st.subheader("🚦 Overall Risk")

    if "High" in report["risk_level"]:
        st.error(report["risk_level"])
    elif "Moderate" in report["risk_level"]:
        st.warning(report["risk_level"])
    else:
        st.success(report["risk_level"])

    st.subheader("🧠 AI Health Summary")
    st.info(report["summary"])

    st.subheader("🔬 Why did the AI predict this?")
    st.write(report["explanation"])

    st.subheader("⚠️ Risk Factors")
    for factor in report["risk_factors"]:
        st.write(f"• {factor}")

    st.subheader("💡 Personalized Recommendations")

    cols = st.columns(2)

    categories = list(report["recommendations"].items())

    for i, (category, tips) in enumerate(categories):

        with cols[i % 2]:
            with st.container(border=True):

                st.markdown(f"### {category}")

            for tip in tips:
                st.write(f"✅ {tip}")

    st.subheader("🎯 Health Priorities")

    for priority in report["priorities"]:
        st.write(f"⭐ {priority}")

    

    st.subheader("📅 Your Weekly Health Plan")

    for day, task in report["weekly_plan"].items():

        with st.container(border=True):
            st.checkbox(
                f"**{day}** — {task}",
                value=False,
                key=day
        )

    st.info(
        "⚠️ This AI tool provides an estimate of diabetes risk and should not replace professional medical advice."
    )
    
st.divider()
st.subheader("📄 Download Your Health Report")

report_text = f"""
MEDINTEL HEALTH REPORT
========================

Prediction: {report['prediction']}
Risk Percentage: {report['risk_percentage']:.1f}%
Risk Level: {report['risk_level']}
Health Score: {report['health_score']}/100

Summary
-------
{report['summary']}

Risk Factors
------------
"""

for factor in report["risk_factors"]:
    report_text += f"\n• {factor}"

report_text += "\n\nRecommendations\n----------------\n"

for category, tips in report["recommendations"].items():
    report_text += f"\n{category}\n"
    for tip in tips:
        report_text += f"  - {tip}"

st.download_button(
    "📄 Download Report",
    data=report_text,
    file_name="MedIntel_Health_Report.txt",
    mime="text/plain"
)
import urllib.parse

st.divider()
st.subheader("🏥 Find Healthcare Services")

col1, col2 = st.columns(2)

with col1:

    doctor = urllib.parse.quote("Diabetologist near me")

    st.link_button(
        "👨‍⚕️ Find Diabetes Specialists",
        f"https://www.google.com/maps/search/{doctor}"
    )

with col2:

    hospital = urllib.parse.quote("Hospital near me")

    st.link_button(
        "🏥 Find Nearby Hospitals",
        f"https://www.google.com/maps/search/{hospital}"
    )
    
st.divider()
st.subheader("🎥 Learn More About Diabetes")

col1, col2, col3 = st.columns(3)

with col1:

    st.link_button(
        "📘 Understanding Diabetes",
        "https://www.youtube.com/results?search_query=Understanding+Diabetes"
    )

with col2:

    st.link_button(
        "🥗 Healthy Diet",
        "https://www.youtube.com/results?search_query=Diabetes+Healthy+Diet"
    )

with col3:

    st.link_button(
        "🏃 Exercise Guide",
        "https://www.youtube.com/results?search_query=Exercise+for+Diabetes"
    )
st.divider()

st.subheader("🩺 Recommended Next Steps")

st.info(
"""
• Discuss your results with a qualified healthcare professional.

• Continue routine health screenings.

• Maintain a balanced diet and regular physical activity.

• Seek medical advice if you experience symptoms such as excessive thirst,
frequent urination, unexplained weight loss, or persistent fatigue.
"""
)
st.success("🌱 Every healthy choice you make today contributes to a healthier future. Keep going!")