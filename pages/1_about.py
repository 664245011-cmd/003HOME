
import base64
from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="ผู้พัฒนา | ML Hub",
    page_icon="🧑‍💻",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Prompt:wght@300;400;500;600;700&family=Inter:wght@400;600;700;800&display=swap');

/* MAIN */
.stApp {
    background: #f5f5f5;
    color: #171717;
    font-family: 'Prompt', 'Inter', sans-serif;
}

html, body, [class*="css"] {
    font-family: 'Prompt', 'Inter', sans-serif;
}

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* HERO */
.hero {
    text-align: center;
    padding: 45px 20px 20px;
}

.hero h1 {
    font-family: 'Inter', 'Prompt', sans-serif;
    font-size: 3rem;
    font-weight: 800;
    color: #111111;
    letter-spacing: -1px;
    margin-bottom: 10px;
}

.hero p {
    color: #737373;
    font-size: 1rem;
    font-weight: 300;
}

/* PROFILE PHOTO */
.profile-photo-wrap {
    display: flex;
    justify-content: center;
    margin-top: 25px;
}

.profile-photo-wrap img {
    width: 200px;
    height: 200px;
    border-radius: 50%;
    object-fit: cover;
    border: 4px solid #ffffff;
    outline: 1px solid #d4d4d4;
    box-shadow: 0 12px 35px rgba(0, 0, 0, 0.12);
    transition: all 0.3s ease;
    filter: grayscale(100%);
}

.profile-photo-wrap img:hover {
    transform: scale(1.04);
    filter: grayscale(0%);
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.18);
}

/* PROFILE CARD */
.profile-card {
    max-width: 500px;
    margin: 30px auto 0;
    background: #ffffff;
    border: 1px solid #e5e5e5;
    border-radius: 22px;
    padding: 32px 36px;
    text-align: center;
    box-shadow: 0 10px 35px rgba(0, 0, 0, 0.04);
    transition: all 0.3s ease;
}

.profile-card:hover {
    border-color: #a3a3a3;
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.08);
}

.profile-card h2 {
    color: #111111;
    font-family: 'Prompt', sans-serif;
    font-size: 1.55rem;
    font-weight: 700;
    margin: 0 0 22px;
}

.profile-tag {
    display: inline-block;
    background: #171717;
    color: #ffffff;
    padding: 6px 15px;
    border-radius: 30px;
    font-size: 0.78rem;
    letter-spacing: 1px;
    margin-bottom: 22px;
}

.info-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 12px;
    padding: 16px 4px;
    border-top: 1px solid #e5e5e5;
    color: #171717;
    font-size: 0.95rem;
}

.info-row span.label {
    color: #737373;
    font-weight: 400;
}

.info-row span.value {
    color: #171717;
    font-weight: 600;
    letter-spacing: 0.3px;
}

/* SIDEBAR */
[data-testid="stSidebar"],
[data-testid="stSidebarCollapsedControl"] {
    visibility: visible !important;
}

[data-testid="stSidebar"] {
    background: #ffffff !important;
    border-right: 1px solid #e5e5e5 !important;
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
    font-family: 'Prompt', sans-serif;
    font-weight: 500;
    font-size: 0.95rem;
    transition: all 0.2s ease;
}

[data-testid="stSidebarNav"] a:hover {
    background: #f0f0f0 !important;
    color: #111111 !important;
}

[data-testid="stSidebarNav"] a[aria-current="page"] {
    background: #171717 !important;
    color: #ffffff !important;
    font-weight: 600;
    border-left: 3px solid #737373;
}

/* SIDEBAR LABELS */
[data-testid="stSidebarNav"] li:nth-child(1) a * {
    font-size: 0 !important;
}

[data-testid="stSidebarNav"] li:nth-child(1) a::after {
    content: "🏠 หน้าหลัก";
    font-size: 0.95rem !important;
}

[data-testid="stSidebarNav"] li:nth-child(2) a * {
    font-size: 0 !important;
}

[data-testid="stSidebarNav"] li:nth-child(2) a::after {
    content: "🧑‍💻 ผู้พัฒนา";
    font-size: 0.95rem !important;
}

/* FOOTER */
.custom-footer {
    text-align: center;
    color: #737373;
    margin-top: 45px;
    padding: 28px 20px;
    font-size: 0.85rem;
    border-top: 1px solid #e5e5e5;
}

footer, #MainMenu {
    visibility: hidden;
}

/* MOBILE */
@media (max-width: 600px) {
    .hero h1 {
        font-size: 2.3rem;
    }

    .profile-card {
        padding: 25px 20px;
    }

    .profile-photo-wrap img {
        width: 175px;
        height: 175px;
    }
}
</style>
""", unsafe_allow_html=True)

# HEADER
st.markdown("""
<div class="hero">
    <h1>ผู้พัฒนา</h1>
    <p>ข้อมูลผู้จัดทำโปรเจกต์ Machine Learning Hub</p>
</div>
""", unsafe_allow_html=True)

# PROFILE PHOTO
photo_path = (
    Path(__file__).resolve().parent.parent
    / "assets"
    / "1.jpg"
)

try:
    photo_b64 = base64.b64encode(
        photo_path.read_bytes()
    ).decode("utf-8")

    st.markdown(
        f"""
        <div class="profile-photo-wrap">
            <img
                src="data:image/jpeg;base64,{photo_b64}"
                alt="Profile Photo"
            >
        </div>
        """,
        unsafe_allow_html=True,
    )

except (FileNotFoundError, OSError):
    st.markdown("""
    <div class="profile-photo-wrap">
        <div style="
            width:200px;
            height:200px;
            border-radius:50%;
            background:#171717;
            border:4px solid #ffffff;
            outline:1px solid #d4d4d4;
            display:flex;
            align-items:center;
            justify-content:center;
            font-size:4rem;
        ">🧑‍💻</div>
    </div>
    """, unsafe_allow_html=True)

# PROFILE INFORMATION
st.markdown("""
<div class="profile-card">
    <div class="profile-tag">THE DEVELOPER</div>

    <h2>จิรศักดิ์ โมกกงจักร</h2>

    <div class="info-row">
        <span class="label">🎓 รหัสนักศึกษา</span>
        <span class="value">664245003</span>
    </div>

    <div class="info-row">
        <span class="label">📚 หมู่เรียน</span>
        <span class="value">Sec. 66/43</span>
    </div>

    <div class="info-row">
        <span class="label">💻 สาขาวิชา</span>
        <span class="value">Computer Science</span>
    </div>
</div>
""", unsafe_allow_html=True)

# FOOTER
st.markdown("""
<div class="custom-footer">
    <strong>ML HUB</strong><br>
    Made with ♥ using Streamlit · 2026
</div>
""", unsafe_allow_html=True)
