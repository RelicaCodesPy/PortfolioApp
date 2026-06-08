import streamlit as st

st.set_page_config(
    page_title="Education",
    page_icon="🎓",
    layout="wide"
)

# ======================
# LOAD CSS
# ======================
with open("styles/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ======================
# HEADER
# ======================
st.title("🎓 Educational Journey")

st.markdown("""
<div class='card'>
My educational journey reflects dedication, perseverance,
and continuous growth from elementary to college.
</div>
""", unsafe_allow_html=True)

st.divider()

# ======================
# TIMELINE SECTION
# ======================
st.markdown("<h2 class='section-title'>📚 Academic Timeline</h2>", unsafe_allow_html=True)

education_data = [
    ("2023 - Present", "DEBESMSCAT", "BSCS"),
    ("2022 - 2023", "Federico A. Estipona Memorial High School", "Grade 12 - STEM"),
    ("2021 - 2022", "PHINMA Rizal College of Laguna", "Grade 11 - STEM"),
    ("2020 - 2021", "Eduardo Barretto Sr. National High School", "Grade 10"),
    ("2019 - 2020", "Centro De Naic National High School", "Grade 9"),
    ("2017 - 2019", "Bucal National High School", "Grades 7-8"),
    ("2011 - 2017", "Guincaiptan Elementary School", "Grades 1-6"),
]

for year, school, level in education_data:
    with st.expander(f"📅 {year} | {school}"):
        st.markdown(f"""
        <div class='card'>
        <b>Program / Level:</b> {level}
        </div>
        """, unsafe_allow_html=True)

st.divider()

# ======================
# SUMMARY METRICS
# ======================
st.markdown("<h2 class='section-title'>📈 Academic Progress</h2>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Schools Attended", "7")

with c2:
    st.metric("Current Program", "BSCS")

with c3:
    st.metric("Current Year", "3rd Year")

st.divider()

# ======================
# INTERACTIVE SECTION
# ======================
st.markdown("<h2 class='section-title'>🔍 Explore Educational Stages</h2>", unsafe_allow_html=True)

stage = st.selectbox(
    "Select a Stage",
    ["Elementary", "Junior High School", "Senior High School", "College"]
)

st.markdown("<div class='card'>", unsafe_allow_html=True)

if stage == "Elementary":
    st.success("""
Guincaiptan Elementary School (2011–2017)

Built strong academic foundation and developed early love for learning.
""")

elif stage == "Junior High School":
    st.success("""
Bucal / Centro De Naic / Eduardo Barretto Sr. High School (2017–2021)

Developed academic excellence and participated in competitions.
""")

elif stage == "Senior High School":
    st.success("""
PHINMA Rizal College / Federico A. Estipona Memorial (2021–2023)

STEM strand focusing on science, math, and technology.
""")

else:
    st.success("""
DEBESMSCAT (2023–Present)

Currently pursuing BS Computer Science with leadership and academic achievements.
""")

st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# ======================
# INTERESTS
# ======================
st.markdown("<h2 class='section-title'>📖 Academic Interests</h2>", unsafe_allow_html=True)

subjects = st.multiselect(
    "Select Academic Areas",
    [
        "Programming",
        "Web Development",
        "Cybersecurity",
        "Artificial Intelligence",
        "Graphic Design",
        "Leadership"
    ]
)

if subjects:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.info(f"You selected: {', '.join(subjects)}")
    st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# ======================
# FOOTER
# ======================
st.markdown("""
<div class='footer'>
Education is the foundation of lifelong growth and success.
</div>
""", unsafe_allow_html=True)
