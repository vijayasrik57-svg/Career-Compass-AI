import os
import streamlit as st
import pandas as pd

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Career Compass AI",
    page_icon="🚀",
    layout="wide"
)

# -----------------------------
# CSS
# -----------------------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(to bottom, #F8FBFF, #EAF4FF);
}

/* Hero */
.hero {
    background: linear-gradient(135deg, #2563EB, #4F46E5);
    padding: 45px 30px;
    border-radius: 24px;
    text-align: center;
    color: white;
    margin-bottom: 25px;
    box-shadow: 0px 8px 25px rgba(37, 99, 235, 0.25);
}

.hero h1 {
    color: white;
    font-size: 48px;
    margin-bottom: 10px;
}

.hero h3 {
    color: white;
    font-weight: 400;
}

/* Welcome Card */
.welcome {
    background: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    margin: 20px 0;
}

/* Feature heading */
.feature-title {
    text-align: center;
    margin: 25px 0;
}

/* Buttons */
.stButton > button {
    border-radius: 12px;
    min-height: 48px;
    font-weight: 600;
    border: none;
}

/* Footer */
.footer {
    text-align: center;
    padding: 25px;
    color: #64748B;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Hero Section
# -----------------------------
st.markdown("""
<div class="hero">

<h1>🚀 Career Compass AI</h1>

<h3>Discover Your Perfect Career with Artificial Intelligence</h3>

<p>Learn • Explore • Build • Grow</p>

</div>
""", unsafe_allow_html=True)

# -----------------------------
# Start Button
# -----------------------------
if st.button("🚀 Start Your Journey", use_container_width=True):
    st.info("✨ Choose any feature below to begin your career journey!")

# -----------------------------
# Read Database
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

careers = pd.read_csv(
    os.path.join(BASE_DIR, "database", "careers.csv")
)

jobs = pd.read_csv(
    os.path.join(BASE_DIR, "database", "jobs.csv")
)

# -----------------------------
# Statistics
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🧭 Careers", len(careers))

with col2:
    st.metric("💼 Jobs", len(jobs))

with col3:
    st.metric("📚 Roadmaps", 5)

# -----------------------------
# Search
# -----------------------------
st.markdown("### 🔍 Find Your Career Path")

search = st.text_input(
    "Search Career, Skill, Job or Project",
    placeholder="Example: AI Engineer"
)

if search:
    career_match = careers[
        careers["Career"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

    job_match = jobs[
        jobs["Job"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

    if not career_match.empty:
        st.success(f"🎯 Found {len(career_match)} career result(s).")

    if not job_match.empty:
        st.success(f"💼 Found {len(job_match)} job result(s).")

    if career_match.empty and job_match.empty:
        st.warning("❌ No matching career or job found.")

st.divider()

# -----------------------------
# Welcome Section
# -----------------------------
st.markdown("""
<div class="welcome">

<h2>👋 Welcome, Pattukutty!</h2>

<p>
Your personalized career journey starts here.
Explore careers, discover jobs, build skills,
and find projects that help you grow.
</p>

</div>
""", unsafe_allow_html=True)

# -----------------------------
# Features
# -----------------------------
st.markdown(
    '<div class="feature-title"><h2>🚀 Explore Features</h2></div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

# -----------------------------
# Left Column
# -----------------------------
with col1:

    if st.button(
        "🧭 Explore Careers",
        use_container_width=True
    ):
        st.switch_page("pages/career_explorer.py")

    if st.button(
        "📚 Learning Roadmap",
        use_container_width=True
    ):
        st.switch_page("pages/learning_roadmap.py")

    if st.button(
        "🤖 AI Mentor",
        use_container_width=True
    ):
        st.switch_page("pages/ai_mentor.py")

    if st.button(
        "🎯 Career Recommendation",
        use_container_width=True
    ):
        st.switch_page("pages/career_recommender.py")

# -----------------------------
# Right Column
# -----------------------------
with col2:

    if st.button(
        "💼 Explore Jobs",
        use_container_width=True
    ):
        st.switch_page("pages/job_explorer.py")

    if st.button(
        "🚀 Project Explorer",
        use_container_width=True
    ):
        st.switch_page("pages/project_explorer.py")

    if st.button(
        "📊 Compare Careers",
        use_container_width=True
    ):
        st.switch_page("pages/compare_careers.py")

# -----------------------------
# Footer
# -----------------------------
st.divider()

st.markdown("""
<div class="footer">

<p>Made with ❤️ using Streamlit & Python</p>

<p>🚀 Career Compass AI © 2026</p>

</div>
""", unsafe_allow_html=True)
