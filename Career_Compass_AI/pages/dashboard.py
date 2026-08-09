import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

careers = pd.read_csv(
    os.path.join(BASE_DIR, "database", "careers.csv")
)
jobs = pd.read_csv("database/jobs.csv")
progress_file = "data/progress.json"
completed = 0
if os.path.exists(progress_file):
    with open(progress_file, "r") as f:
        progress_data = json.load(f)
        completed = sum(progress_data.values())
# -----------------------------
# Dashboard Chart Data
# -----------------------------
labels = ["Careers", "Jobs", "Roadmaps", "Completed"]

values = [
    len(careers),
    len(jobs),
    5,
    completed
]
# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
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
    padding:20px;
    border-radius:15px;
    box-shadow:0px 3px 10px rgba(0,0,0,0.1);
    text-align:center;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.title("📊 Career Compass Dashboard")
st.write("Overview of your Career Compass AI platform.")

# -----------------------------
# Dashboard Cards
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="card">
    <h2>🧭</h2>
    <h3>{len(careers)}</h3>
    <p>Careers</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="card">
    <h2>💼</h2>
    <h3>{len(jobs)}</h3>
    <p>Jobs</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="card">
    <h2>📚</h2>
    <h3>5</h3>
    <p>Learning Roadmaps</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="card">
    <h2>🚀</h2>
    <h3>{completed}</h3>
    <p>Completed Topics</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()
st.subheader("📊 Platform Overview")

fig, ax = plt.subplots(figsize=(7,4))

ax.bar(labels, values)

ax.set_ylabel("Count")
ax.set_title("Career Compass Statistics")

st.pyplot(fig)
st.subheader("📈 Platform Statistics")

career_count = len(careers)
job_count = len(jobs)

progress = (career_count + job_count) / 70

st.progress(min(progress, 1.0))

st.write(f"🧭 Careers Available : **{career_count}**")
st.write(f"💼 Jobs Available : **{job_count}**")
st.subheader("🎯 Welcome!")

st.info("""
Welcome to Career Compass AI.

Use the pages on the left to:

✅ Explore Careers

✅ Explore Jobs

✅ Follow Learning Roadmaps

✅ Compare Careers

✅ Get AI Career Guidance

✅ Discover Project Ideas
""")
