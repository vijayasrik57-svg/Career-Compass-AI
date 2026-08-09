import json
import os
import streamlit as st
from database.learning_resources import resources
# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Learning Roadmap",
    page_icon="📚",
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

<h1>📚 Learning Roadmap</h1>

<p>Follow a structured roadmap to achieve your dream career.</p>

</div>
""", unsafe_allow_html=True)

career = st.selectbox(
    "Choose Career",
    [
        "Artificial Intelligence Engineer",
        "Data Scientist",
        "Software Developer",
        "Cyber Security Analyst",
        "Cloud Engineer"
    ]
)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

progress_file = os.path.join(
    BASE_DIR,
    "data",
    "progress.json"
)

if os.path.exists(progress_file):
    with open(progress_file, "r") as f:
        progress_data = json.load(f)
else:
    progress_data = {}

roadmaps = {
    "Artificial Intelligence Engineer": [
        "Python Programming",
        "Data Structures",
        "Statistics & Mathematics",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow / PyTorch",
        "Projects",
        "Internship"
    ],

    "Data Scientist": [
        "Python",
        "SQL",
        "Statistics",
        "Pandas & NumPy",
        "Data Visualization",
        "Machine Learning",
        "Projects",
        "Portfolio"
    ],

    "Software Developer": [
        "C / Java / Python",
        "Data Structures",
        "OOP",
        "DBMS",
        "Web Development",
        "Git & GitHub",
        "Projects",
        "Internship"
    ],

    "Cyber Security Analyst": [
        "Networking",
        "Linux",
        "Python",
        "Ethical Hacking",
        "OWASP",
        "Penetration Testing",
        "Projects",
        "Certifications"
    ],

    "Cloud Engineer": [
        "Linux",
        "Networking",
        "AWS",
        "Azure",
        "Docker",
        "Kubernetes",
        "Projects",
        "Cloud Certification"
    ]
}

st.subheader(f"🚀 {career} Roadmap")

completed = 0
total = len(roadmaps[career])

st.subheader("📖 Learning Checklist")
if "progress" not in st.session_state:
    st.session_state.progress = {}

for step in roadmaps[career]:

    key = f"{career}_{step}"

    checked = st.checkbox(
        step,
        value=progress_data.get(key, False)
    )

    progress_data[key] = checked

    if checked:
        completed += 1

with open(progress_file, "w") as f:
    json.dump(progress_data, f, indent=4)

progress = completed / total

st.markdown("---")

st.subheader("📊 Your Progress")

st.progress(progress)

st.success(f"✅ Completed : {completed} / {total}")

st.info(f"🎯 Progress : {int(progress*100)}%")
st.markdown("---")

st.subheader("🌐 Learning Resources")

for skill in roadmaps[career]:

    if skill in resources:

        with st.expander(f"📚 {skill}"):

            for name, link in resources[skill]:
                st.markdown(f"- [{name}]({link})")
