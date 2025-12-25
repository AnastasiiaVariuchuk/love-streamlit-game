import streamlit as st
import random
import time

st.set_page_config(
    page_title="Love Slots Deluxe 🎰",
    page_icon="❤️",
    layout="centered"
)

# ---------- SESSION STATE ----------
if "reels" not in st.session_state:
    st.session_state.reels = ["❔", "❔", "❔"]

if "coins" not in st.session_state:
    st.session_state.coins = 100

if "message" not in st.session_state:
    st.session_state.message = "Tap SPIN to try your luck 💓"

# ---------- SYMBOLS ----------
symbols = ["❤️", "💖", "💘", "💗", "💝"]

# ---------- STYLES ----------
st.markdown("""
<style>
.slot {
    font-size: 90px;
    text-align: center;
}
.info {
    font-size: 22px;
    text-align: center;
    margin: 10px;
}
.message {
    font-size: 24px;
    text-align: center;
    margin-top: 15px;
}
</style>
""", unsafe_allow_html=True)

# ---------- UI ----------
st.markdown("<h2 style='text-align:center;'>🎰 Love Slots Deluxe 🎰</h2>", unsafe_allow_html=True)
st.markdown(f"<div class='info'>💰 Coins: {st.session_state.coins}</div>", unsafe_allow_html=True)

cols = st.columns(3)
slots_placeholder = []

for col in cols:
    slots_placeholder.append(col.empty())

for i in range(3):
    slots_placeholder[i].markdown(
        f"<div class='slot'>{st.session_state.reels[i]}</div>",
        unsafe_allow_html=True
    )

st.markdown(f"<div class='message'>{st.session_state.message}</div>", unsafe_allow_html=True)

# ---------- SPIN LOGIC ----------
if st.button("SPIN 🎲", use_container_width=True):

    if st.session_state.coins < 10:
        st.session_state.message = "💔 Not enough coins"
        st.rerun()

    st.session_state.coins -= 10

    # Weighted symbols: more chance for hearts
    weighted_symbols = ["❤️"] * 5 + ["💖"] * 3 + ["💘"] * 2 + ["💗"] * 2 + ["💝"]

    # ⏳ SPIN ANIMATION
    for _ in range(8):
        st.session_state.reels = [random.choice(weighted_symbols) for _ in range(3)]
        for i in range(3):
            slots_placeholder[i].markdown(
                f"<div class='slot'>{st.session_state.reels[i]}</div>",
                unsafe_allow_html=True
            )
        time.sleep(0.1)

    r = st.session_state.reels
    hearts = sum(1 for x in r if x == "❤️")

    # ---------- WIN CONDITIONS ----------
    if hearts == 3:
        st.session_state.coins += 100
        st.session_state.message = "❤️ JACKPOT! My heart is all yours ❤️"
        st.balloons()

    elif hearts == 2:
        st.session_state.coins += 20
        st.session_state.message = "💖 Two hearts! Love is in the air 💖"

    elif hearts == 1:
        st.session_state.coins += 5
        st.session_state.message = "💗 One heart… love is close 💗"

    else:
        st.session_state.message = "💔 No love this time… try again"

    st.rerun()

