import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Project Explorer",
    page_icon="🚀",
    layout="wide"
)

# -----------------------------
# CSS
# -----------------------------
st.markdown("""
<style>

.stApp{
    background: linear-gradient(to bottom,#F8FBFF,#EAF4FF);
}

.card{
    background:white;
    padding:25px;
    border-radius:15px;
    box-shadow:0px 3px 10px rgba(0,0,0,0.1);
    margin-bottom:20px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown("""
<div class="card">

<h1>🚀 Project Explorer</h1>

<p>Discover project ideas based on your career.</p>

</div>
""", unsafe_allow_html=True)

career = st.selectbox(
    "🎯 Select Career",
    [
        "Artificial Intelligence Engineer",
        "Data Scientist",
        "Software Developer",
        "Cyber Security Analyst",
        "Cloud Engineer"
    ]
)

projects = {

    "Artificial Intelligence Engineer":[
        "🤖 AI Chatbot",
        "🩺 Disease Prediction System",
        "😊 Face Emotion Detection",
        "🚗 Driver Drowsiness Detection",
        "🎵 Music Recommendation System"
    ],

    "Data Scientist":[
        "📈 Sales Prediction",
        "🏠 House Price Prediction",
        "🛒 Customer Segmentation",
        "📊 Data Dashboard",
        "🎬 Movie Recommendation System"
    ],

    "Software Developer":[
        "🛍️ E-Commerce Website",
        "🏥 Hospital Management System",
        "📚 Library Management System",
        "🎓 Student Management System",
        "💰 Expense Tracker"
    ],

    "Cyber Security Analyst":[
        "🔐 Password Strength Checker",
        "🌐 Network Scanner",
        "🛡️ Phishing Detection",
        "📁 File Encryption Tool",
        "🔍 Vulnerability Scanner"
    ],

    "Cloud Engineer":[
        "☁️ AWS Deployment",
        "🐳 Docker Project",
        "⚙️ Kubernetes Cluster",
        "💾 Cloud Backup System",
        "📊 Cloud Monitoring Dashboard"
    ]

}

st.subheader(f"🚀 Recommended Projects for {career}")

for project in projects[career]:
    st.success(project)

st.info("💡 Complete at least 3 projects before applying for internships.")