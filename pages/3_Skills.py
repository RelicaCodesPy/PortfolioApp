import streamlit as st

st.set_page_config(
    page_title="Skills",
    page_icon="💡",
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
st.title("💡 Skills & Competencies")

st.markdown("""
<div class='card'>
My skills continue to grow through academics, leadership,
hackathons, workshops, and personal projects.
</div>
""", unsafe_allow_html=True)

st.divider()

# ======================
# TABS SECTION
# ======================
tab1, tab2, tab3, tab4 = st.tabs([
    "💻 Programming",
    "🌐 Web Development",
    "🎨 Design",
    "👑 Leadership"
])

# ======================
# PROGRAMMING
# ======================
with tab1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("Programming Skills")
    st.progress(70, text="Python")
    st.progress(65, text="Java")
    st.progress(60, text="C++")
    st.progress(60, text="C")

    st.info("Basic to Intermediate programming level with continuous improvement.")

    st.markdown("</div>", unsafe_allow_html=True)

# ======================
# WEB DEVELOPMENT
# ======================
with tab2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("Web Development Skills")
    st.progress(70, text="HTML")
    st.progress(65, text="CSS")

    st.info("Foundational web development knowledge with UI/UX awareness.")

    st.markdown("</div>", unsafe_allow_html=True)

# ======================
# DESIGN
# ======================
with tab3:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("Graphic Design Skills")
    st.progress(95, text="Canva")
    st.progress(90, text="Photo Manipulation")
    st.progress(90, text="Poster Design")
    st.progress(88, text="Digital Illustration")
    st.progress(85, text="UI/UX Design")

    st.success("""
🏆 Graphic Design Festival Awards  
🏆 Best Photo Manipulation  
🏆 Best Abstract Art  
🏆 Most Popular Design  
🏆 Nitezen’s Choice
""")

    st.markdown("</div>", unsafe_allow_html=True)

# ======================
# LEADERSHIP
# ======================
with tab4:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("Leadership & Soft Skills")
    st.progress(98, text="Leadership")
    st.progress(95, text="Communication")
    st.progress(95, text="Teamwork")
    st.progress(90, text="Event Management")
    st.progress(90, text="Public Speaking")
    st.progress(95, text="Problem Solving")

    st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# ======================
# TECH STACK
# ======================
st.markdown("<h2 class='section-title'>🛠 Technology Stack</h2>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
<div class='card'>
<b>Programming</b>

- Python  
- Java  
- C++  
- C  
</div>
""", unsafe_allow_html=True)

with c2:
    st.markdown("""
<div class='card'>
<b>Web Technologies</b>

- HTML  
- CSS  
- Streamlit  
</div>
""", unsafe_allow_html=True)

with c3:
    st.markdown("""
<div class='card'>
<b>Design Tools</b>

- Canva  
- Photo Editing  
- Digital Art Tools  
</div>
""", unsafe_allow_html=True)

st.divider()

# ======================
# INTERACTIVE SECTION
# ======================
st.markdown("<h2 class='section-title'>📊 Skill Confidence</h2>", unsafe_allow_html=True)

skill = st.selectbox(
    "Choose a Skill",
    ["Python", "Java", "C++", "C", "HTML", "CSS", "Graphic Design", "Leadership"]
)

confidence = st.slider("Confidence Level", 0, 100, 80)

st.markdown("<div class='card'>", unsafe_allow_html=True)
st.success(f"{skill}: {confidence}% Confidence Level")
st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# ======================
# LEARNING JOURNEY
# ======================
st.markdown("<h2 class='section-title'>🚀 Currently Learning</h2>", unsafe_allow_html=True)

st.markdown("""
<div class='card'>

- Advanced Python Programming  
- Web Application Development  
- Cybersecurity Concepts  
- UI/UX Design Principles  
- Artificial Intelligence Fundamentals  
- Software Development Best Practices  

</div>
""", unsafe_allow_html=True)

st.divider()

# ======================
# CAREER INTERESTS
# ======================
st.markdown("<h2 class='section-title'>🎯 Career Interests</h2>", unsafe_allow_html=True)

interests = st.multiselect(
    "Select Career Areas",
    [
        "Software Development",
        "Web Development",
        "Cybersecurity",
        "Artificial Intelligence",
        "Graphic Design",
        "UI/UX Design",
        "Project Management"
    ]
)

if interests:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.info(f"Selected: {', '.join(interests)}")
    st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# ======================
# FOOTER
# ======================
st.markdown("""
<div class='footer'>
Learning never stops — every experience is growth.
</div>
""", unsafe_allow_html=True)
