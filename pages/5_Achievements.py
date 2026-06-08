import streamlit as st

st.set_page_config(
    page_title="Achievements",
    page_icon="🏆",
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
st.title("🏆 Achievements & Recognition")

st.markdown("""
<div class='card'>
This page showcases my academic achievements, competition awards,
leadership recognitions, and participation in various activities
throughout my academic journey.
</div>
""", unsafe_allow_html=True)

st.divider()

# ======================
# METRICS DASHBOARD
# ======================
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Academic Honors", "15+")

with c2:
    st.metric("Competition Awards", "20+")

with c3:
    st.metric("Hackathons", "5+")

with c4:
    st.metric("Leadership Awards", "8+")

st.divider()

# ======================
# TABS (MODERN STRUCTURE)
# ======================
tab1, tab2, tab3, tab4 = st.tabs([
    "🎓 Elementary",
    "🏫 Junior High",
    "📚 Senior High",
    "💻 College"
])

# ======================
# ELEMENTARY
# ======================
with tab1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("Guincaiptan Elementary School")

    st.markdown("""
- Grade 1–2: 2nd Honors  
- Grade 3: 2nd Honors, Best in English, MTAP Participant  
- Grade 5: 1st Honors, Best in Filipino  
- Grade 6: With Honors  
""")

    st.markdown("</div>", unsafe_allow_html=True)

# ======================
# JUNIOR HIGH
# ======================
with tab2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("Junior High School")

    st.markdown("""
- With Honors (Grades 7–10)  
- Math Quiz Bee 2nd Placer  
""")

    st.markdown("</div>", unsafe_allow_html=True)

# ======================
# SENIOR HIGH
# ======================
with tab3:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("Senior High School")

    st.markdown("""
- With Honors (Grade 12)  
""")

    st.markdown("</div>", unsafe_allow_html=True)

# ======================
# COLLEGE (NESTED TABS)
# ======================
with tab4:
    year1, year2, year3 = st.tabs(["1st Year", "2nd Year", "3rd Year"])

    with year1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("""
- Silver Medal Athletics (4x100 Relay)  
- TechFusion Facilitator  
""")
        st.markdown("</div>", unsafe_allow_html=True)

    with year2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("""
- Dean’s Lister  
- Vice President’s Lister  
- GDF 2024 Multiple Awards  
- Hackathon Participant  
- Student of the Year Top 3 Awardee  
""")
        st.markdown("</div>", unsafe_allow_html=True)

    with year3:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("""
- Dean’s Lister  
- AI & Tech Exchange Programs  
- Hackathon Awards (Best Backend, UI/UX, Crypto MVP)  
""")
        st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# ======================
# FEATURED ACHIEVEMENTS
# ======================
st.markdown("<h2 class='section-title'>🌟 Featured Achievements</h2>", unsafe_allow_html=True)

feature = st.selectbox(
    "Select Category",
    ["Academic Excellence", "Graphic Design", "Hackathons", "Leadership"]
)

st.markdown("<div class='card'>", unsafe_allow_html=True)

if feature == "Academic Excellence":
    st.success("""
🎓 Dean’s Lister  
🎓 Vice President’s Lister  
🎓 Student of the Year Top 3  
""")

elif feature == "Graphic Design":
    st.success("""
🎨 GDF 2024 Winner Awards  
🎨 Best in Photo Manipulation  
🎨 Best Abstract Art  
🎨 UI/UX Recognition  
""")

elif feature == "Hackathons":
    st.success("""
💻 Web Dev Hackathon Awards  
🔐 Cryptography MVP  
🔐 Backend Excellence Award  
""")

else:
    st.success("""
👑 DISCSS President  
👑 CASCSC Representative  
👑 Class President  
""")

st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# ======================
# SUMMARY
# ======================
st.markdown("<h2 class='section-title'>📈 Journey Summary</h2>", unsafe_allow_html=True)

st.progress(100)

st.markdown("""
<div class='card'>
From elementary achievements to college leadership,
hackathons, and design competitions — this journey
represents growth, discipline, and excellence.
</div>
""", unsafe_allow_html=True)

st.divider()

# ======================
# FOOTER
# ======================
st.markdown("""
<div class='footer'>
Success is built through consistency, passion, and leadership.
</div>
""", unsafe_allow_html=True)
