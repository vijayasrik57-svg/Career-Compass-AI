import streamlit as st
import pandas as pd
import os
# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Compare Careers",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# Read Career Database
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv(
    os.path.join(BASE_DIR, "database", "careers.csv")
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

<h1>📊 Compare Careers</h1>

<p>Compare two careers and choose the best path.</p>

</div>
""", unsafe_allow_html=True)

# -----------------------------
# Career Selection
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    career1 = st.selectbox(
        "Choose First Career",
        df["Career"],
        key="career1"
    )

with col2:
    career2 = st.selectbox(
        "Choose Second Career",
        df["Career"],
        index=1,
        key="career2"
    )

c1 = df[df["Career"] == career1].iloc[0]
c2 = df[df["Career"] == career2].iloc[0]

# -----------------------------
# Comparison Table
# -----------------------------
comparison = pd.DataFrame({
    "Feature": [
        "Salary",
        "Education",
        "Future Scope",
        "Skills",
        "Top Companies"
    ],
    career1: [
        c1["Salary"],
        c1["Education"],
        c1["Future_Scope"],
        c1["Skills"],
        c1["Top_Companies"]
    ],
    career2: [
        c2["Salary"],
        c2["Education"],
        c2["Future_Scope"],
        c2["Skills"],
        c2["Top_Companies"]
    ]
})

st.subheader("📋 Career Comparison")

st.dataframe(comparison, use_container_width=True)
