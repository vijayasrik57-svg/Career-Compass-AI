import streamlit as st
import pandas as pd
import os
# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Job Explorer",
    page_icon="💼",
    layout="wide"
)

# -----------------------------
# Read Job Database
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv(
    os.path.join(BASE_DIR, "database", "jobs.csv")
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

<h1>💼 Job Explorer</h1>

<p>Find jobs based on your skills and interests.</p>

</div>
""", unsafe_allow_html=True)

# -----------------------------
# Search
# -----------------------------
search = st.text_input(
    "🔍 Search Job",
    placeholder="Example: AI Engineer"
)

filtered_df = df

if search:
    filtered_df = df[
        df["Job"].str.contains(search, case=False, na=False)
    ]

# -----------------------------
# Job Dropdown
# -----------------------------
job = st.selectbox(
    "Choose Job",
    filtered_df["Job"]
)

selected = filtered_df[
    filtered_df["Job"] == job
].iloc[0]

# -----------------------------
# Job Details
# -----------------------------
st.subheader("📋 Job Details")

col1, col2 = st.columns(2)

with col1:
    st.info(f"🏢 Company\n\n{selected['Company']}")
    st.success(f"📍 Location\n\n{selected['Location']}")
    st.write(f"💰 Salary : {selected['Salary']}")

with col2:
    st.warning(f"📅 Experience\n\n{selected['Experience']}")
    st.write(f"🕒 Type : {selected['Type']}")

st.markdown("### 🛠 Required Skills")

skills = selected["Skills"].split(",")

for skill in skills:
    st.write(f"✅ {skill.strip()}")
