import streamlit as st
import random
import time

st.set_page_config(
    page_title="Tap the Heart 💖",
    page_icon="❤️",
    layout="centered"
)

# -------- SESSION STATE --------
if "score" not in st.session_state:
    st.session_state.score = 0

if "start" not in st.session_state:
    st.session_state.start = time.time()

if "game_over" not in st.session_state:
    st.session_state.game_over = False

# -------- TIMER --------
GAME_TIME = 8
elapsed = time.time() - st.session_state.start
time_left = max(0, int(GAME_TIME - elapsed))

if time_left == 0:
    st.session_state.game_over = True

# -------- STYLES (MOBILE-FIRST) --------
st.markdown("""
<style>
.big-heart {
    font-size: 120px;
    text-align: center;
    animation: beat 0.9s infinite;
}
@keyframes beat {
    0% { transform: scale(1); }
    50% { transform: scale(1.25); }
    100% { transform: scale(1); }
}
.tap-zone {
    padding: 40px;
    border-radius: 20px;
    text-align: center;
}
.info {
    font-size: 22px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# -------- UI --------
st.markdown("<h2 style='text-align:center;'>💓 Tap the Heart 💓</h2>", unsafe_allow_html=True)
st.markdown(f"<div class='info'>⏱ {time_left}s | 💖 {st.session_state.score}</div>", unsafe_allow_html=True)

# -------- GAME --------
if not st.session_state.game_over:
    heart = random.choice(["❤️", "💖", "💘", "💗", "💝"])

    if st.button("TAP 💓", use_container_width=True):
        st.session_state.score += 1
        st.rerun()

    st.markdown(
        f"<div class='tap-zone'><div class='big-heart'>{heart}</div></div>",
        unsafe_allow_html=True
    )

else:
    # -------- END SCREEN --------
    if st.session_state.score >= 6:
        st.balloons()
        st.markdown(
            "<h1 style='text-align:center; color:#ff4b4b;'>❤️ I LOVE YOU ❤️</h1>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            "<h2 style='text-align:center;'>💔 Try again</h2>",
            unsafe_allow_html=True
        )

    if st.button("Play again 🔄", use_container_width=True):
        st.session_state.score = 0
        st.session_state.start = time.time()
        st.session_state.game_over = False
        st.rerun()
