import streamlit as st

st.set_page_config(
    page_title="Projects",
    page_icon="🎨",
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
st.title("🎨 Graphic Arts Projects")

st.markdown("""
<div class='card'>
### Role: Graphic Artist

This collection showcases my graphic design and digital art projects
developed through competitions, advocacy campaigns, and creative exploration.
</div>
""", unsafe_allow_html=True)

st.divider()

# ======================
# FILTER (UI ONLY)
# ======================
category = st.selectbox(
    "Filter Projects",
    [
        "All",
        "Digital Illustration",
        "Advocacy Poster",
        "Typography",
        "Photo Manipulation",
        "Abstract Art"
    ]
)

st.divider()

# ======================
# PROJECT CARDS (UPGRADED LAYOUT STYLE)
# ======================

def project(title, img, content):
    with st.expander(title):
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.image(img, use_container_width=True)
        st.markdown(content, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

project(
    "🧚 Enchanted Whispers",
    "assets/artwork7.jpg",
    """
### Digital Illustration

A fantasy-inspired artwork portraying a fairy surrounded by butterflies and flowers.

**Skills:** Illustration, Composition, Color Harmony  
**Tools:** Canva
"""
)

project(
    "❤️ One Chance",
    "assets/artwork6.jpg",
    """
### Typography Poster

A motivational design emphasizing the importance of opportunities.

**Skills:** Typography, Layout, Visual Communication  
**Tools:** Canva
"""
)

project(
    "🌍 A Fading World: Our Last Chance",
    "assets/artwork5.jpg",
    """
### Advocacy Poster

An environmental awareness design about climate change and responsibility.

**Skills:** Photo Manipulation, Campaign Design  
**Tools:** Canva
"""
)

project(
    "🌲 Trees for the Future",
    "assets/artwork4.jpg",
    """
### Environmental Design

A conservation artwork promoting reforestation and sustainability.

**Skills:** Poster Design, Visual Messaging  
**Tools:** Canva
"""
)

project(
    "🎨 Fragments of Imagination",
    "assets/artwork3.jpg",
    """
### Abstract Art

A creative abstract piece representing imagination and freedom.

**Skills:** Abstract Design, Composition  
**Tools:** Canva
"""
)

project(
    "🌌 Beyond Reality",
    "assets/artwork2.jpg",
    """
### Photo Manipulation

A surreal double exposure artwork blending nature and portrait.

**Skills:** Photo Manipulation, Digital Compositing  
**Tools:** Canva
"""
)

project(
    "🌸 Neon Serenity",
    "assets/artwork1.jpg",
    """
### Digital Illustration

An anime-inspired digital artwork celebrating individuality.

**Skills:** Illustration, Color Theory  
**Tools:** Canva
"""
)

st.divider()

# ======================
# STATS
# ======================
st.markdown("<h2 class='section-title'>📊 Portfolio Highlights</h2>", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Artworks", "7")

with c2:
    st.metric("Role", "Graphic Artist")

with c3:
    st.metric("Awards", "10+")

with c4:
    st.metric("Recognition", "Multiple")

st.divider()

# ======================
# ACHIEVEMENTS
# ======================
st.markdown("<h2 class='section-title'>🏆 Graphic Design Achievements</h2>", unsafe_allow_html=True)

st.success("""
🎨 Graphic Design Festival (GDF 2024)

• 1st Runner Up  
• Best in Photo Manipulation  
• Best Abstract Art  
• Most Popular Graphic Design  
• Nitezen’s Choice  
• Top Performing Speed Art  
""")

st.divider()

# ======================
# FOOTER
# ======================
st.markdown("""
<div class='footer'>
Creativity turns imagination into visual impact.
</div>
""", unsafe_allow_html=True)
