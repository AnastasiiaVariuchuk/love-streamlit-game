import streamlit as st
import random
import time

st.set_page_config(page_title="Love Game 💖", page_icon="❤️", layout="centered")

# --------- SESSION STATE ----------
if "score" not in st.session_state:
    st.session_state.score = 0

if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

if "game_over" not in st.session_state:
    st.session_state.game_over = False

# --------- TIMER ----------
GAME_DURATION = 10  # seconds
elapsed = time.time() - st.session_state.start_time
time_left = max(0, int(GAME_DURATION - elapsed))

if time_left == 0:
    st.session_state.game_over = True

# --------- UI ----------
st.markdown("<h1 style='text-align:center;'>💘 Catch the Love 💘</h1>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align:center;'>⏱ Time left: {time_left}s</h3>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align:center;'>Score: {st.session_state.score}</h3>", unsafe_allow_html=True)

# --------- HEART ANIMATION ----------
st.markdown(
    """
    <style>
    .heart {
        font-size: 100px;
        animation: beat 0.8s infinite;
    }
    @keyframes beat {
        0% { transform: scale(1); }
        50% { transform: scale(1.3); }
        100% { transform: scale(1); }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --------- GAME LOGIC ----------
if not st.session_state.game_over:
    cols = st.columns(3)
    position = random.randint(0, 2)

    with cols[position]:
        st.markdown("<div class='heart'>❤️</div>", unsafe_allow_html=True)
        if st.button("Catch 💖"):
            st.session_state.score += 1
            st.rerun()

else:
    # --------- GAME OVER ----------
    if st.session_state.score >= 5:
        st.balloons()
        st.markdown(
            "<h1 style='text-align:center; color:#ff4b4b;'>❤️ I LOVE YOU ❤️</h1>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            "<h2 style='text-align:center;'>💔 Try again!</h2>",
            unsafe_allow_html=True
        )

    if st.button("Play again 🔄"):
        st.session_state.score = 0
        st.session_state.start_time = time.time()
        st.session_state.game_over = False
        st.rerun()