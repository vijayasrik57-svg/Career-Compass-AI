import streamlit as st

st.set_page_config(
    page_title="AI Mentor",
    page_icon="🤖",
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

<h1>🤖 AI Career Mentor</h1>

<p>Ask anything about careers, skills, placements or higher studies.</p>

</div>
""", unsafe_allow_html=True)

question = st.text_area(
    "💬 Ask your question",
    placeholder="Example: How can I become an AI Engineer?"
)

if st.button("🚀 Get Advice", use_container_width=True):

    if question.strip() == "":
        st.warning("Please enter a question.")
    else:

        q = question.lower()

        if "ai" in q:
            st.success("""
### 🤖 AI Mentor

To become an AI Engineer:

✅ Learn Python

✅ Learn Machine Learning

✅ Learn Deep Learning

✅ Build Projects

✅ Learn TensorFlow / PyTorch

✅ Complete an Internship

✅ Build a strong GitHub Portfolio
""")

        elif "data" in q:

            st.success("""
### 📊 Data Science Roadmap

✅ Python

✅ SQL

✅ Statistics

✅ Pandas

✅ Machine Learning

✅ Power BI

✅ Kaggle Projects
""")

        elif "placement" in q:

            st.success("""
### 🎯 Placement Tips

✅ Practice Aptitude

✅ DSA

✅ Resume

✅ Communication

✅ Mock Interviews

✅ Projects
""")

        else:

            st.info("""
I'm still learning 😊

Soon I'll answer any career question using AI.
""")