import streamlit as st
import pandas as pd
import os

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Career Explorer",
    page_icon="🧭",
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
    background: linear-gradient(to bottom, #F8FBFF, #EAF4FF);
}

.card{
    background: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Hero Section
# -----------------------------
st.markdown("""
<div class="card">

<h1>🧭 Career Explorer</h1>

<p>Discover careers that match your interests and skills.</p>

</div>
""", unsafe_allow_html=True)
# -----------------------------
# Search Career
# -----------------------------
search = st.text_input(
    "🔍 Search Career",
    placeholder="Type career name..."
)

filtered_df = df

if search:
    filtered_df = df[
        df["Career"].str.contains(search, case=False, na=False)
    ]

if filtered_df.empty:
    st.warning("❌ No career found.")
    st.stop()

# -----------------------------
# Career Dropdown
# -----------------------------
career = st.selectbox(
    "Choose Career",
    filtered_df["Career"]
)

st.success(f"✅ You selected: {career}")

# -----------------------------
# Get Selected Career Details
# -----------------------------
selected = filtered_df[filtered_df["Career"] == career].iloc[0]
image_name = (
    selected["Career"]
    .lower()
    .replace("&", "and")
    .replace("/", "_")
    .replace(" ", "_")
)

image_path = f"assets/careers/{image_name}.png"

if os.path.exists(image_path):
    st.image(image_path, width=260)
else:
    st.info("🖼️ Image will be available soon.")
# -----------------------------
# Career Details
# -----------------------------
st.subheader("📋 Career Details")

# About Card
st.markdown(f"""
<div class="card">
<h3>📝 About this Career</h3>
<p>{selected["Description"]}</p>
</div>
""", unsafe_allow_html=True)

# Two Columns
col1, col2 = st.columns(2)

with col1:
    st.info(f"💰 Salary\n\n{selected['Salary']}")
    st.success(f"🎓 Education\n\n{selected['Education']}")

with col2:
    st.warning(f"📈 Future Scope\n\n{selected['Future_Scope']}")
    st.error(f"🏢 Top Companies\n\n{selected['Top_Companies']}")

# Skills
st.markdown("### 🛠 Required Skills")

skills = selected["Skills"].split(",")

for skill in skills:
    st.write(f"✅ {skill.strip()}")
