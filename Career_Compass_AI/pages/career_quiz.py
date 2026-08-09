import streamlit as st

st.set_page_config(
    page_title="Career Recommendation Quiz",
    page_icon="🎯",
    layout="wide"
)

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

st.markdown("""
<div class="card">
<h1>🎯 Career Recommendation Quiz</h1>
<p>Answer a few questions to discover the career that suits you best.</p>
</div>
""", unsafe_allow_html=True)

q1 = st.radio(
    "1️⃣ Do you enjoy Programming?",
    ["Yes", "No"]
)

q2 = st.radio(
    "2️⃣ Do you like Mathematics?",
    ["Yes", "No"]
)

q3 = st.radio(
    "3️⃣ Do you enjoy Data Analysis?",
    ["Yes", "No"]
)

q4 = st.radio(
    "4️⃣ Are you interested in Cyber Security?",
    ["Yes", "No"]
)

q5 = st.radio(
    "5️⃣ Do you like Cloud Technologies?",
    ["Yes", "No"]
)

if st.button("🎯 Get Recommendation", use_container_width=True):

    if q4 == "Yes":
        st.success("🛡️ Recommended Career: Cyber Security Analyst")

    elif q5 == "Yes":
        st.success("☁️ Recommended Career: Cloud Engineer")

    elif q1 == "Yes" and q2 == "Yes":
        st.success("🤖 Recommended Career: Artificial Intelligence Engineer")

    elif q3 == "Yes":
        st.success("📊 Recommended Career: Data Scientist")

    else:
        st.success("💻 Recommended Career: Software Developer")

    st.balloons()