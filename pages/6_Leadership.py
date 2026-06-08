import streamlit as st

st.set_page_config(
    page_title="Leadership",
    page_icon="👑",
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
st.title("👑 Leadership Journey")

st.markdown("""
<div class='card'>
Leadership has been a core part of my growth, helping me develop
communication, teamwork, decision-making, and organizational skills.
</div>
""", unsafe_allow_html=True)

st.divider()

# ======================
# METRICS DASHBOARD
# ======================
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Leadership Roles", "8")

with c2:
    st.metric("Organizations", "5")

with c3:
    st.metric("Years Experience", "8+")

with c4:
    st.metric("Current Position", "President")

st.divider()

# ======================
# TIMELINE SECTION
# ======================
st.markdown("<h2 class='section-title'>📅 Leadership Timeline</h2>", unsafe_allow_html=True)

leadership_positions = [
    ("2018–2019", "Grade 8 Representative", "KABAYANI Club"),
    ("2022–2023", "Grade 12 Representative", "YES-O"),
    ("2023–2024", "Class Vice President", "BSCS 1A"),
    ("2024–2025", "Class President", "BSCS 2A"),
    ("2024–2025", "DISCSS Representative", "DISCSS"),
    ("Present", "President", "Katipunan ng Kabataan"),
    ("2025–2026", "President", "DISCSS"),
    ("2025–2026", "Representative", "CASCSC")
]

for year, position, org in leadership_positions:
    with st.expander(f"👑 {year} | {position}"):
        st.markdown(f"""
        <div class='card'>
        <b>Organization:</b> {org}
        </div>
        """, unsafe_allow_html=True)

st.divider()

# ======================
# CURRENT POSITIONS
# ======================
st.markdown("<h2 class='section-title'>🌟 Current Leadership Roles</h2>", unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:
    st.markdown("""
    <div class='card'>
    <h3>👑 President</h3>
    DISCSS<br>
    A.Y. 2025–2026
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class='card'>
    <h3>🏛 Representative</h3>
    CASCSC<br>
    A.Y. 2025–2026
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ======================
# LEADERSHIP SKILLS
# ======================
st.markdown("<h2 class='section-title'>💡 Leadership Skills</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.progress(98, text="Leadership")
    st.progress(95, text="Communication")
    st.progress(95, text="Teamwork")
    st.progress(92, text="Decision Making")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.progress(90, text="Conflict Resolution")
    st.progress(93, text="Organization")
    st.progress(90, text="Public Speaking")
    st.progress(95, text="Event Management")
    st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# ======================
# RESPONSIBILITIES
# ======================
st.markdown("<h2 class='section-title'>📋 Key Responsibilities</h2>", unsafe_allow_html=True)

role = st.selectbox(
    "Select Leadership Position",
    [
        "DISCSS President",
        "CASCSC Representative",
        "Class President",
        "Katipunan ng Kabataan President"
    ]
)

st.markdown("<div class='card'>", unsafe_allow_html=True)

if role == "DISCSS President":
    st.info("""
• Lead organization operations  
• Represent Computer Science students  
• Coordinate programs and activities  
• Promote student development  
""")

elif role == "CASCSC Representative":
    st.info("""
• Represent DISCSS in council meetings  
• Communicate student concerns  
• Participate in planning activities  
""")

elif role == "Class President":
    st.info("""
• Lead class activities  
• Coordinate with faculty  
• Represent classmates  
""")

else:
    st.info("""
• Lead youth community programs  
• Organize outreach activities  
• Promote youth engagement  
""")

st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# ======================
# PHILOSOPHY
# ======================
st.markdown("<h2 class='section-title'>🎯 Leadership Philosophy</h2>", unsafe_allow_html=True)

st.markdown("""
<div class='card'>
<blockquote>
"Leadership is not about authority; it is about service,
responsibility, and inspiring others toward a common goal."
</blockquote>

I believe leadership requires empathy, integrity,
accountability, and continuous growth.
</div>
""", unsafe_allow_html=True)

st.divider()

# ======================
# SUMMARY
# ======================
st.markdown("<h2 class='section-title'>🏆 Leadership Highlights</h2>", unsafe_allow_html=True)

st.markdown("""
<div class='card'>
✔ Grade 8 Representative  
✔ Grade 12 Representative  
✔ Class Vice President  
✔ Class President  
✔ DISCSS President  
✔ CASCSC Representative  
✔ Youth Organization Leader  
</div>
""", unsafe_allow_html=True)

st.divider()

# ======================
# FOOTER
# ======================
st.markdown("""
<div class='footer'>
Leadership is about service, growth, and positive impact.
</div>
""", unsafe_allow_html=True)
