import streamlit as st

st.set_page_config(
    page_title="About Me",
    page_icon="👩‍💻",
    layout="wide"
)

# LOAD CSS
with open("styles/styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# HEADER

st.title("👩‍💻 About Me")

st.markdown("""
### Hello, I'm Relica Malinao!

A passionate **3rd Year Bachelor of Science in Computer Science student**
at **Dr. Emilio B. Espinosa Sr. Memorial State College of Agriculture and Technology (DEBESMSCAT)**.

I am dedicated to continuously improving my knowledge in technology,
graphic design, cybersecurity, and leadership while making meaningful
contributions to both academic and community organizations.
""")

st.divider()

# PROFILE SECTION

col1, col2 = st.columns([1, 2])

with col1:

    st.image(
        "assets/profile.png",
        use_container_width=True
    )

with col2:

    st.subheader("📌 Professional Profile")

    st.write("""
    I am a Computer Science student who enjoys combining technology,
    creativity, and leadership.

    My academic journey has allowed me to explore different areas
    including:

    • Software Development

    • Web Development

    • Graphic Design

    • Cybersecurity

    • Artificial Intelligence

    • Student Leadership

    Through competitions, workshops, hackathons, and leadership
    experiences, I continue to develop both technical and interpersonal skills.
    """)

st.divider()

# CAREER GOALS

st.subheader("🎯 Career Goals")

st.write("""
My goal is to become a skilled technology professional capable of creating
innovative solutions that positively impact communities and organizations.

I aspire to strengthen my expertise in software development, web technologies,
cybersecurity, and digital design while maintaining a strong commitment to
leadership and lifelong learning.
""")

st.divider()

# INTERESTS

st.subheader("💡 Areas of Interest")

interest = st.selectbox(
    "Select an area you would like to know about:",
    [
        "Software Development",
        "Web Development",
        "Graphic Design",
        "Cybersecurity",
        "Leadership"
    ]
)

if interest == "Software Development":

    st.info("""
    I enjoy learning programming concepts and developing solutions using
    various programming languages and technologies.
    """)

elif interest == "Web Development":

    st.info("""
    I am interested in creating responsive and user-friendly web applications
    that provide meaningful experiences for users.
    """)

elif interest == "Graphic Design":

    st.info("""
    Graphic design allows me to express creativity through visual storytelling,
    digital illustrations, and promotional materials.
    """)

elif interest == "Cybersecurity":

    st.info("""
    Through workshops, hackathons, and cybersecurity challenges,
    I continue to expand my understanding of digital security.
    """)

else:

    st.info("""
    Leadership has helped me develop communication, teamwork,
    decision-making, and organizational skills.
    """)

st.divider()

# PERSONAL STRENGTHS

st.subheader("🌟 Personal Strengths")

col1, col2 = st.columns(2)

with col1:

    st.success("✔ Leadership")
    st.success("✔ Creativity")
    st.success("✔ Adaptability")
    st.success("✔ Teamwork")

with col2:

    st.success("✔ Communication")
    st.success("✔ Problem Solving")
    st.success("✔ Time Management")
    st.success("✔ Continuous Learning")

st.divider()

# QUICK FACTS

st.subheader("📊 Quick Facts")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Current Year Level",
        "3rd Year"
    )

with col2:
    st.metric(
        "Leadership Positions",
        "8"
    )

with col3:
    st.metric(
        "Major Interests",
        "5"
    )

st.divider()

# QUOTE

st.markdown("""
### 💬 Personal Motto

> "Success is achieved through continuous learning, perseverance,
> leadership, and the courage to embrace new opportunities."
""")

st.divider()

# FOOTER

st.markdown("""
<div class='footer'>

Thank you for visiting my portfolio.

Let's continue learning, creating, and leading.

</div>
""", unsafe_allow_html=True)
