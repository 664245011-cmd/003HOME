
import base64
from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="ผู้พัฒนา | ML Hub",
    page_icon="🧑‍💻",
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

html, body, [class*="css"] {
    font-family: 'Prompt', 'Inter', sans-serif;
}

.block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* HEADER */
.hero {
    text-align: center;
    padding: 25px 15px 35px;
}

.hero h1 {
    color: #111111;
    font-family: 'Inter', 'Prompt', sans-serif;
    font-size: clamp(2.3rem, 5vw, 3.5rem);
    font-weight: 800;
    letter-spacing: -1px;
    margin-bottom: 10px;
}

.hero p {
    color: #737373;
    font-size: 1rem;
    font-weight: 300;
}

/* PROFILE LAYOUT */
.profile-container {
    display: flex;
    align-items: center;
    gap: 45px;
    max-width: 950px;
    margin: 10px auto 35px;
    padding: 38px;
    background: #ffffff;
    border: 1px solid #e5e5e5;
    border-radius: 25px;
    box-shadow: 0 12px 35px rgba(0,0,0,0.045);
}

/* PHOTO */
.photo-column {
    flex: 0 0 300px;
    text-align: center;
}

.profile-photo {
    width: 270px;
    height: 320px;
    object-fit: cover;
    object-position: center;
    border-radius: 20px;
    border: 1px solid #dedede;
    filter: grayscale(100%);
    transition: all 0.35s ease;
    box-shadow: 0 12px 28px rgba(0,0,0,0.12);
}

.profile-photo:hover {
    filter: grayscale(0%);
    transform: translateY(-4px);
}

.photo-placeholder {
    width: 270px;
    height: 320px;
    margin: auto;
    border-radius: 20px;
    background: #171717;
    color: #ffffff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 5rem;
}

/* INFORMATION */
.info-column {
    flex: 1;
    min-width: 0;
}

.eyebrow {
    color: #737373;
    font-size: 0.78rem;
    letter-spacing: 3px;
    font-weight: 600;
    margin-bottom: 12px;
}

.profile-name {
    font-family: 'Prompt', sans-serif;
    font-size: clamp(1.6rem, 3vw, 2.3rem);
    line-height: 1.5;
    font-weight: 700;
    color: #111111;
    margin-bottom: 8px;
    overflow-wrap: anywhere;
}

.profile-role {
    color: #737373;
    font-size: 0.95rem;
    margin-bottom: 30px;
}

.info-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 15px;
    padding: 17px 0;
    border-top: 1px solid #e5e5e5;
}

.info-label {
    color: #737373;
    font-size: 0.92rem;
    white-space: nowrap;
}

.info-value {
    color: #171717;
    font-size: 0.95rem;
    font-weight: 600;
    text-align: right;
}

.profile-badge {
    display: inline-block;
    background: #171717;
    color: #ffffff;
    border-radius: 30px;
    padding: 8px 16px;
    font-size: 0.8rem;
    margin-top: 20px;
}

/* BOTTOM SECTION */
.section-title {
    text-align: center;
    font-size: 1.25rem;
    font-weight: 600;
    color: #171717;
    margin: 35px 0 18px;
}

.bottom-card {
    background: #ffffff;
    border: 1px solid #e5e5e5;
    border-radius: 16px;
    padding: 22px;
    text-align: center;
    transition: 0.25s ease;
}

.bottom-card:hover {
    background: #171717;
    color: #ffffff;
    transform: translateY(-4px);
}

.bottom-icon {
    font-size: 1.8rem;
    margin-bottom: 8px;
}

.bottom-title {
    font-size: 1rem;
    font-weight: 600;
}

.bottom-desc {
    color: #737373;
    font-size: 0.85rem;
    margin-top: 6px;
}

.bottom-card:hover .bottom-desc {
    color: #d4d4d4;
}

/* SIDEBAR */
[data-testid="stSidebar"] {
    background: #ffffff !important;
    border-right: 1px solid #e5e5e5;
}

[data-testid="stSidebarNav"] {
    padding-top: 20px;
}

[data-testid="stSidebarNav"]::before {
    content: "ML HUB NAVIGATION";
    display: block;
    margin: 0 20px 20px;
    padding-bottom: 16px;
    border-bottom: 1px solid #e5e5e5;
    font-family: 'Inter', sans-serif;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 2px;
    color: #737373;
}

[data-testid="stSidebarNav"] a {
    margin: 4px 12px !important;
    padding: 12px 16px !important;
    border-radius: 10px;
    color: #525252 !important;
}

[data-testid="stSidebarNav"] a:hover {
    background: #f0f0f0 !important;
    color: #111111 !important;
}

[data-testid="stSidebarNav"] a[aria-current="page"] {
    background: #171717 !important;
    color: #ffffff !important;
    font-weight: 600;
}

/* FOOTER */
.custom-footer {
    text-align: center;
    color: #737373;
    margin-top: 45px;
    padding: 25px 10px;
    font-size: 0.83rem;
    border-top: 1px solid #e5e5e5;
}

footer, #MainMenu {
    visibility: hidden;
}

/* MOBILE */
@media (max-width: 700px) {
    .profile-container {
        flex-direction: column;
        gap: 28px;
        padding: 24px 18px;
    }

    .photo-column {
        flex: none;
        width: 100%;
    }

    .profile-photo,
    .photo-placeholder {
        width: min(100%, 270px);
        height: 300px;
    }

    .info-column {
        width: 100%;
    }
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("""
<div class="hero">
    <h1>ABOUT ME.</h1>
    <p>ข้อมูลผู้พัฒนา Machine Learning Hub</p>
</div>
""", unsafe_allow_html=True)

# ---------- LOAD PHOTO ----------
photo_path = (
    Path(__file__).resolve().parent.parent
    / "assets"
    / "1.jpg"
)

photo_html = ""

try:
    photo_b64 = base64.b64encode(
        photo_path.read_bytes()
    ).decode("utf-8")

    photo_html = f"""
        <img
            class="profile-photo"
            src="data:image/jpeg;base64,{photo_b64}"
            alt="Developer Profile"
        >
    """
except (FileNotFoundError, OSError):
    photo_html = """
        <div class="photo-placeholder">🧑‍💻</div>
    """

# ---------- PROFILE ----------
st.markdown(f"""
<div class="profile-container">

    <div class="photo-column">
        {photo_html}
    </div>

    <div class="info-column">
        <div class="eyebrow">THE DEVELOPER</div>

        <div class="profile-name">
            จิรศักดิ์ โมกกงจักร
        </div>

        <div class="profile-role">
            Computer Science Student
        </div>

        <div class="info-row">
            <span class="info-label">🎓 รหัสนักศึกษา</span>
            <span class="info-value">664245003</span>
        </div>

        <div class="info-row">
            <span class="info-label">📚 หมู่เรียน</span>
            <span class="info-value">Sec. 66/43</span>
        </div>

        <div class="info-row">
            <span class="info-label">💻 สาขาวิชา</span>
            <span class="info-value">Computer Science</span>
        </div>

        <div class="profile-badge">
            ✦ MACHINE LEARNING HUB
        </div>
    </div>

</div>
""", unsafe_allow_html=True)

# ---------- SKILLS / PROJECTS ----------
st.markdown(
    '<div class="section-title">WHAT I DO</div>',
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns(3, gap="medium")

items = [
    ("💻", "Programming", "พัฒนาโปรแกรมและเว็บไซต์"),
    ("🤖", "Machine Learning", "เรียนรู้การใช้โมเดล AI"),
    ("🗄️", "Database", "จัดการข้อมูลและฐานข้อมูล"),
]

for col, (icon, title, desc) in zip(
    [col1, col2, col3], items
):
    with col:
        st.markdown(f"""
        <div class="bottom-card">
            <div class="bottom-icon">{icon}</div>
            <div class="bottom-title">{title}</div>
            <div class="bottom-desc">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("""
<div class="custom-footer">
    <strong>ML HUB</strong><br>
    Designed with simplicity · Made with ♥ using Streamlit · 2026
</div>
""", unsafe_allow_html=True)
