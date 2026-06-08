import streamlit as st

st.set_page_config(
    page_title="Achievements",
    page_icon="🏆",
    layout="wide"
)

# LOAD CSS
with open("styles/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.title("🏆 Achievements & Recognition")

st.markdown("""
This page showcases my academic achievements, competition awards,
leadership recognitions, and participation in various educational,
creative, and technology-related activities throughout my journey.
""")

st.divider()

# OVERVIEW

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Academic Honors", "15+")

with col2:
    st.metric("Competition Awards", "20+")

with col3:
    st.metric("Hackathons", "5+")

with col4:
    st.metric("Leadership Awards", "8+")

st.divider()

# TABS

tab1, tab2, tab3, tab4 = st.tabs([
    "🎓 Elementary",
    "🏫 Junior High",
    "📚 Senior High",
    "💻 College"
])

# ELEMENTARY

with tab1:

    st.subheader("Guincaiptan Elementary School")

    st.markdown("""
### Grade 1
- 2nd Honors

### Grade 2
- 2nd Honors

### Grade 3
- 2nd Honors
- Best in English
- MTAP Contestant

### Grade 4
- 2nd Honors

### Grade 5
- 1st Honors
- Best in Filipino

### Grade 6
- With Honors
""")

# JUNIOR HIGH

with tab2:

    st.subheader("Junior High School Achievements")

    st.markdown("""
### Grade 7
- With Honors

### Grade 8
- With Honors

### Grade 9
- With Honors
- 2nd Placer Math Quiz Bee Competition

### Grade 10
- With Honors
""")

# SENIOR HIGH

with tab3:

    st.subheader("Senior High School Achievements")

    st.markdown("""
### Grade 12
- With Honors
""")

# COLLEGE

with tab4:

    year1, year2, year3 = st.tabs([
        "1st Year",
        "2nd Year",
        "3rd Year"
    ])

    # 1ST YEAR

    with year1:

        st.markdown("""
### Academic Year 2023–2024

- Silver in Athletics Women (4x100 Relay)
- Facilitator (TechFusion 2024)
""")

    # 2ND YEAR

    with year2:

        st.markdown("""
### Academic Year 2024–2025

#### Academic Recognition
- Vice President’s Lister (1st Sem. A.Y. 2024–2025)
- Dean’s Lister (2nd Sem. A.Y. 2024–2025)

#### Graphic Design Festival (GDF 2024)
- Idiosyncratic Graphic Design (Semi Finals)
- Best in Photo Manipulation (Semi Finals)
- Facilitator (GDF 2024)
- 1st Runner Up
- Rank 2 (Art Exhibit)
- Rank 2 (Semi Finals)
- Top Performing Speed Art (Grand Finals)
- Nitezen’s Choice (Grand Finals)
- Best in One Color Shade Art (Grand Finals)
- Best Abstract Art (Grand Finals)
- Top Performing Finalist in Fixing a Broken Art Challenge (Grand Finals)
- Most Popular Graphic Design (Grand Finals)

#### Cybersecurity & Technology
- PicoCTF Activity Workshop 2025: From Zero to Hero
- Participation in Hackathon: Cyber Challenge (TechFusion 2025)

#### Special Recognition
- Student of the Year Top 3 Awardee (TechFusion 2025)

#### Web Development Hackathon 2025
- Guest Participant
- Guest Top 7 (Preliminary)
- Guest Team Top 5 (Semi-Finals)
- Web Guardian Award (PicoCTF Cyber Challenge Semi-Finals)
""")

    # 3RD YEAR

    with year3:

        st.markdown("""
### Academic Year 2025–2026

#### Academic Recognition
- Dean’s Lister (1st Sem. A.Y. 2025–2026)

#### Academic & Professional Development
- Participation in FILKOM UB Academic and Cultural Exchange on Information Technology (FACE-IT)
- AI+X: Understanding and Applying Artificial Intelligence

#### Web Development Hackathon 2025
- Top 5 Defender in SQL Injection Challenge
- Top 4 in Web Development Hackathon (Semi-Finals Cross-over)
- Cryptography MVP (Semi-Finals Cross-over)
- Best in Backend Development
- Best in UI/UX Design
- 3rd Runner Up
- Host Team Participant
- Crypto Alchemist Award
- Top 3 Attacker in SQL Injection Challenge

#### Graphic Design Festival
- Board of Adjudicator (GDF 2025)
""")

st.divider()

# FEATURED ACHIEVEMENTS

st.subheader("🌟 Featured Achievements")

featured = st.selectbox(
    "Select Achievement Category",
    [
        "Academic Excellence",
        "Graphic Design",
        "Hackathons",
        "Leadership"
    ]
)

if featured == "Academic Excellence":

    st.success("""
🎓 Vice President's Lister

🎓 Dean's Lister

🎓 Student of the Year Top 3 Awardee

🎓 Multiple Honors Recipient
""")

elif featured == "Graphic Design":

    st.success("""
🎨 1st Runner Up (GDF 2024)

🎨 Best in Photo Manipulation

🎨 Best Abstract Art

🎨 Most Popular Graphic Design

🎨 Nitezen's Choice

🎨 Best in UI/UX Design
""")

elif featured == "Hackathons":

    st.success("""
💻 Web Development Hackathon 2025

🔐 Cryptography MVP

🔐 Crypto Alchemist Award

🔐 Top SQL Injection Defender

🔐 Top SQL Injection Attacker
""")

else:

    st.success("""
👑 DISCSS President

👑 CASCSC Representative

👑 Class President

👑 Class Vice President

👑 Youth Organization Leader
""")

st.divider()

# TIMELINE SUMMARY

st.subheader("📈 Achievement Journey")

st.progress(100)

st.info("""
From elementary honors to university-level leadership,
graphic design competitions, hackathons, and academic excellence,
my journey reflects continuous growth, perseverance, and dedication.
""")

st.divider()

st.markdown("""
<div class='footer'>

Success is built through continuous learning,
hard work, creativity, and leadership.

</div>
""", unsafe_allow_html=True)
