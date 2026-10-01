
import streamlit as st

st.set_page_config(
    page_title="Movie Recommendation",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------- BLACK & WHITE THEME ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700&family=Inter:wght@400;600;700;800&display=swap');

.stApp {
    background: #f5f5f5;
    color: #171717;
    font-family: 'Prompt', 'Inter', sans-serif;
}

header[data-testid="stHeader"] {
    background: transparent;
}

html, body, [class*="css"] {
    font-family: 'Prompt', 'Inter', sans-serif;
}

.block-container {
    max-width: 1250px;
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

/* HERO */
.hero {
    background: #111111;
    color: #ffffff;
    border-radius: 28px;
    padding: 65px 25px 58px;
    text-align: center;
    margin: 10px 0 35px;
    position: relative;
    overflow: hidden;
    border: 1px solid #333333;
}

.hero::before {
    content: '✦';
    position: absolute;
    top: 8px;
    left: 7%;
    color: #777777;
    font-size: 45px;
}

.hero::after {
    content: '✦';
    position: absolute;
    bottom: 5px;
    right: 8%;
    color: #777777;
    font-size: 35px;
}

.hero h1 {
    color: #ffffff;
    font-family: 'Inter', sans-serif;
    font-size: clamp(2rem, 5vw, 3.7rem);
    font-weight: 800;
    letter-spacing: -1.5px;
    line-height: 1.2;
    margin: 0 0 18px;
}

.hero p {
    color: #c4c4c4;
    font-size: 1.05rem;
    font-weight: 300;
    margin: 0;
}

.hero-tag {
    display: inline-block;
    border: 1px solid #555555;
    border-radius: 30px;
    color: #e5e5e5;
    padding: 6px 16px;
    font-size: 0.8rem;
    letter-spacing: 2px;
    margin-bottom: 22px;
}

/* SECTION */
.section-title {
    color: #171717;
    text-align: center;
    font-size: 1.35rem;
    font-weight: 600;
    margin: 20px 0 8px;
}

.section-desc {
    color: #737373;
    text-align: center;
    font-size: 0.92rem;
    margin-bottom: 30px;
}

/* PROJECT CARDS */
.card {
    background: #ffffff;
    border: 1px solid #e5e5e5;
    border-radius: 20px;
    padding: 27px;
    min-height: 275px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    margin-bottom: 22px;
    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.035);
    transition: all 0.3s ease;
}

.card:hover {
    transform: translateY(-6px);
    border-color: #737373;
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.10);
}

.card-icon {
    width: 58px;
    height: 58px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #171717;
    color: #ffffff;
    border-radius: 16px;
    font-size: 1.8rem;
    margin-bottom: 22px;
}

.card h3 {
    color: #171717;
    font-size: 1.2rem;
    font-weight: 600;
    margin: 0 0 10px;
}

.card p {
    color: #737373;
    font-size: 0.9rem;
    line-height: 1.8;
    margin: 0 0 25px;
}

.btn {
    display: block;
    text-align: center;
    text-decoration: none !important;
    padding: 13px 18px;
    border-radius: 11px;
    background: #171717;
    color: #ffffff !important;
    font-weight: 500;
    font-size: 0.93rem;
    border: 1px solid #171717;
    transition: all 0.25s ease;
}

.btn:hover {
    background: #ffffff;
    color: #171717 !important;
}

/* FOOTER */
.custom-footer {
    text-align: center;
    color: #737373;
    margin-top: 30px;
    padding: 28px 10px;
    font-size: 0.83rem;
    border-top: 1px solid #e5e5e5;
}

footer, #MainMenu {
    visibility: hidden;
}

[data-testid="stSidebar"] {
    background: #ffffff !important;
    border-right: 1px solid #e5e5e5;
}

/* MOBILE */
@media (max-width: 768px) {
    .hero {
        padding: 45px 15px;
        border-radius: 20px;
    }

    .card {
        min-height: 240px;
        padding: 22px;
    }
}
</style>

<div class="hero">
    <div class="hero-tag">CINEMA • DISCOVERY • TECHNOLOGY</div>
    <h1>🎬 MOVIE<br>RECOMMENDATION</h1>
    <p>ค้นพบภาพยนตร์ที่ใช่ ผ่านระบบแนะนำหนังอัจฉริยะ</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section-title">🎥 Movie Recommendation Projects</div>
<div class="section-desc">
    รวมระบบจัดการข้อมูล วิเคราะห์ความสัมพันธ์ และแนะนำภาพยนตร์
</div>
""", unsafe_allow_html=True)

# ---------- PROJECTS ----------
APPS = [
    (
        "🎞️",
        "Movie & User Database",
        "จัดการข้อมูลภาพยนตร์และผู้ใช้งาน ด้วยฐานข้อมูลกราฟ Neo4j",
        "https://colab.research.google.com/drive/1MxwddWvrCj21v5XOHpjoDlE4_PGM8qYk?usp=sharing",
        "เปิดโปรเจกต์ ↗",
    ),
    (
        "👥",
        "User Relationship Analysis",
        "วิเคราะห์ความสัมพันธ์ระหว่างผู้ใช้งานและประวัติการรับชมภาพยนตร์",
        "https://colab.research.google.com/drive/1Dgt5W3WGhh_yA9jzt3kpuEiooxHvS_ad?usp=sharing",
        "เปิดโปรเจกต์ ↗",
    ),
    (
        "🍿",
        "Movie Recommendation System",
        "แนะนำภาพยนตร์จากความสัมพันธ์ของผู้ใช้งานและประวัติการรับชม",
        "https://gaidptrbfndmhfnqc8fu7h.streamlit.app/",
        "เปิดเว็บไซต์ ↗",
    ),
]

cols = st.columns(3, gap="large")

for i, (icon, title, desc, url, button_text) in enumerate(APPS):
    with cols[i]:
        st.markdown(
            f"""
            <div class="card">
                <div>
                    <div class="card-icon">{icon}</div>
                    <h3>{title}</h3>
                    <p>{desc}</p>
                </div>
                <a class="btn" href="{url}" target="_blank"
                   rel="noopener noreferrer">{button_text}</a>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown("""
<div class="custom-footer">
    <strong>🎬 MOVIE RECOMMENDATION</strong><br>
    Discover your next favorite movie.<br>
    Made with ♥ using Streamlit · 2026
</div>
""", unsafe_allow_html=True)
