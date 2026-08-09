import streamlit as st
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

st.set_page_config(
    page_title="Career Recommender",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Career Recommendation")

name = st.text_input("👤 Enter Your Name")

qualification = st.selectbox(
    "🎓 Qualification",
    [
        "12th",
        "Diploma",
        "B.E/B.Tech",
        "B.Sc",
        "M.Tech",
        "Other"
    ]
)

interest = st.selectbox(
    "Choose your interest",
    [
        "Artificial Intelligence",
        "Programming",
        "Cyber Security",
        "Cloud Computing",
        "Data Science",
        "UI/UX Design"
    ]
)

skill = st.slider(
    "⭐ Rate your skill level",
    min_value=1,
    max_value=10,
    value=5
)

recommendations = {
    "Artificial Intelligence": [
        "Artificial Intelligence Engineer",
        "Machine Learning Engineer",
        "AI Research Scientist",
        "Data Scientist"
    ],
    "Programming": [
        "Software Developer",
        "Full Stack Developer",
        "Backend Developer",
        "Frontend Developer"
    ],
    "Cyber Security": [
        "Cyber Security Analyst",
        "Ethical Hacker",
        "SOC Analyst",
        "Security Engineer"
    ],
    "Cloud Computing": [
        "Cloud Engineer",
        "DevOps Engineer",
        "Solutions Architect"
    ],
    "Data Science": [
        "Data Scientist",
        "Data Analyst",
        "Data Engineer"
    ],
    "UI/UX Design": [
        "UI/UX Designer",
        "Frontend Developer"
    ]
}
skill_recommendations = {
    "Artificial Intelligence": [
        "Python",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow / PyTorch"
    ],
    "Programming": [
        "Python / Java",
        "Data Structures",
        "OOP",
        "Git & GitHub"
    ],
    "Cyber Security": [
        "Networking",
        "Linux",
        "Python",
        "Ethical Hacking"
    ],
    "Cloud Computing": [
        "Linux",
        "AWS / Azure",
        "Docker",
        "Kubernetes"
    ],
    "Data Science": [
        "Python",
        "SQL",
        "Statistics",
        "Pandas & NumPy"
    ],
    "UI/UX Design": [
        "Figma",
        "UI Design",
        "UX Research",
        "Prototyping"
    ]
}
st.subheader("📚 Skills You Should Learn")
st.divider()

st.subheader("🛣️ Continue Your Learning")

if st.button("📚 Open Learning Roadmap", use_container_width=True):
    st.switch_page("pages/learning_roadmap.py")
for skill_name in skill_recommendations[interest]:
    st.write(f"✅ {skill_name}")

if skill <= 3:
    st.info("📘 Recommendation Level : Beginner")
elif skill <= 7:
    st.success("🚀 Recommendation Level : Intermediate")
else:
    st.warning("🏆 Recommendation Level : Advanced")

salary = st.selectbox(
    "💰 Expected Salary",
    [
        "Below ₹5 LPA",
        "₹5 - ₹10 LPA",
        "₹10 - ₹20 LPA",
        "Above ₹20 LPA"
    ]
)

work_style = st.radio(
    "🏢 Preferred Work Style",
    [
        "Office",
        "Hybrid",
        "Remote"
    ],
    horizontal=True
)

base_score = 95

if skill <= 3:
    base_score -= 10
elif skill >= 8:
    base_score += 3

if salary == "Above ₹20 LPA":
    base_score -= 5

if work_style == "Remote":
    base_score -= 2
best_score = max(
    60,
    base_score - 5
)

best_career = recommendations[interest][0]

if best_score >= 90:
    best_grade = "A+"
elif best_score >= 80:
    best_grade = "A"
elif best_score >= 70:
    best_grade = "B"
else:
    best_grade = "C"

st.markdown("---")

st.subheader("🏆 Best Career Match")

st.success(
    f"⭐ {best_career}\n\n"
    f"🎯 Match Score: {best_score}%\n\n"
    f"🏅 Grade: {best_grade}"
)
for i, career in enumerate(recommendations[interest], start=1):

    score = max(60, base_score - (i * 5))

    st.success(f"⭐ {career}")

    st.progress(score / 100)

    st.caption(f"🎯 Match Score : {score}%")

    if score >= 90:
        grade = "A+"
        message = "🔥 Excellent Career Match"
    elif score >= 80:
        grade = "A"
        message = "⭐ Very Good Career Match"
    elif score >= 70:
        grade = "B"
        message = "👍 Good Career Match"
    else:
        grade = "C"
        message = "📘 Consider Improving Your Skills"

    st.write(f"🏆 Grade: {grade}")
    st.caption(message)

    st.divider()

if st.button("📄 Download Career Report"):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "<b>Career Compass AI</b>",
            styles["Title"]
        )
    )

    story.append(
        Paragraph(
            f"Interest : {interest}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"Name : {name}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"Qualification : {qualification}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"Skill Level : {skill}/10",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"Expected Salary : {salary}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"Preferred Work Style : {work_style}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            "<br/><b>Recommended Careers</b>",
            styles["Heading2"]
        )
    )

    for i, career in enumerate(recommendations[interest], start=1):

        score = max(60, base_score - (i * 5))

        if score >= 90:
            grade = "A+"
        elif score >= 80:
            grade = "A"
        elif score >= 70:
            grade = "B"
        else:
            grade = "C"

        story.append(
            Paragraph(
                f"{career} - Match Score : {score}% - Grade : {grade}",
                styles["Normal"]
            )
        )

    story.append(
        Paragraph(
            "<br/>Generated by Career Compass AI",
            styles["Italic"]
        )
    )

    doc.build(story)

    pdf = buffer.getvalue()

    st.download_button(
        "⬇ Download PDF",
        pdf,
        file_name="Career_Report.pdf",
        mime="application/pdf"
    )