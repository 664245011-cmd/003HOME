
import base64
from pathlib import Path
from textwrap import dedent

import streamlit as st

st.set_page_config(
    page_title="ผู้พัฒนา | ML Hub",
    page_icon="🧑‍💻",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ==================== CSS ====================
st.markdown(dedent("""
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
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* HEADER */
.hero {
    text-align: center;
    padding: 35px 20px 15px;
}

.hero h1 {
    font-family: 'Inter', 'Prompt', sans-serif;
    font-size: 3rem;
    font-weight: 800;
    color: #111;
    letter-spacing: -1px;
    margin-bottom: 10px;
}

.hero p {
    color: #737373;
    font-size: 1rem;
}

/* PHOTO */
.profile-photo-wrap {
    display: flex;
    justify-content: center;
    margin-top: 20px;
}

.profile-photo-wrap img,
.profile-placeholder {
    width: 200px;
    height: 200px;
    border-radius: 50%;
    border: 4px solid white;
    outline: 1px solid #d4d4d4;
    box-shadow: 0 12px 35px rgba(0, 0, 0, 0.12);
}

.profile-photo-wrap img {
    object-fit: cover;
    filter: grayscale(100%);
    transition: 0.3s ease;
}

.profile-photo-wrap img:hover {
    transform: scale(1.04);
    filter: grayscale(0%);
}

.profile-placeholder {
    background: #171717;
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 4rem;
}

/* PROFILE CARD */
.profile-card {
    box-sizing: border-box;
    width: 100%;
    max-width: 550px;
    margin: 30px auto 0;
    padding: 32px 36px;
    background: #fff;
    border: 1px solid #e5e5e5;
    border-radius: 22px;
    box-shadow: 0 10px 35px rgba(0, 0, 0, 0.04);
}

.profile-tag-wrap {
    text-align: center;
    margin-bottom: 24px;
}

.profile-tag {
    display: inline-block;
    background: #171717;
    color: #fff;
    padding: 7px 16px;
    border-radius: 30px;
    font-size: 0.78rem;
    letter-spacing: 1px;
}

/* NAME AND ID */
.name-id-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
    padding-bottom: 22px;
    border-bottom: 1px solid #e5e5e5;
}

.name-id-row h2 {
    margin: 0;
    color: #111;
    font-family: 'Prompt', sans-serif;
    font-size: 1.35rem;
    font-weight: 700;
}

.student-id {
    display: inline-block;
    background: #171717;
    color: #fff;
    padding: 8px 12px;
    border-radius: 8px;
    font-size: 0.9rem;
    font-weight: 600;
    white-space: nowrap;
}

/* INFORMATION */
.info-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 12px;
    padding: 17px 4px;
    border-bottom: 1px solid #e5e5e5;
    font-size: 0.95rem;
}

.info-row:last-child {
    border-bottom: none;
    padding-bottom: 0;
}

.info-row .label {
    color: #737373;
}

.info-row .value {
    color: #171717;
    font-weight: 600;
    text-align: right;
}

/* SIDEBAR */
[data-testid="stSidebar"] {
    background: #fff !important;
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
    font-family: 'Prompt', sans-serif;
}

[data-testid="stSidebarNav"] a:hover {
    background: #f0f0f0 !important;
    color: #111 !important;
}

[data-testid="stSidebarNav"] a[aria-current="page"] {
    background: #171717 !important;
    color: #fff !important;
    font-weight: 600;
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

    .profile-photo-wrap img,
    .profile-placeholder {
        width: 175px;
        height: 175px;
    }

    .name-id-row {
        flex-direction: column;
        align-items: flex-start;
    }

    .name-id-row h2 {
        font-size: 1.2rem;
    }
}
</style>
"""), unsafe_allow_html=True)


# ==================== HEADER ====================
st.markdown(dedent("""
<div class="hero">
    <h1>ผู้พัฒนา</h1>
    <p>ข้อมูลผู้จัดทำโปรเจกต์ Machine Learning Hub</p>
</div>
"""), unsafe_allow_html=True)


# ==================== PROFILE PHOTO ====================
photo_path = (
    Path(__file__).resolve().parent.parent
    / "assets"
    / "1.jpg"
)

try:
    photo_b64 = base64.b64encode(
        photo_path.read_bytes()
    ).decode("utf-8")

    st.markdown(dedent(f"""
    <div class="profile-photo-wrap">
        <img
            src="data:image/jpeg;base64,{photo_b64}"
            alt="Profile Photo"
        >
    </div>
    """), unsafe_allow_html=True)

except (FileNotFoundError, OSError):
    st.markdown(dedent("""
    <div class="profile-photo-wrap">
        <div class="profile-placeholder">🧑‍💻</div>
    </div>
    """), unsafe_allow_html=True)


# ==================== PROFILE INFORMATION ====================
st.markdown(dedent("""
<div class="profile-card">

    <div class="profile-tag-wrap">
        <span class="profile-tag">THE DEVELOPER</span>
    </div>

    <div class="name-id-row">
        <h2>จิรศักดิ์ โมกกงจักร</h2>
        <span class="student-id">664245003</span>
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
"""), unsafe_allow_html=True)


# ==================== FOOTER ====================
st.markdown(dedent("""
<div class="custom-footer">
    <strong>ML HUB</strong><br>
    Made with ♥ using Streamlit · 2026
</div>
"""), unsafe_allow_html=True)
