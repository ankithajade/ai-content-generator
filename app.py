import streamlit as st
from utils.api_helpers import fetch_random_quote, fetch_random_joke, fetch_random_fact

st.set_page_config(
    page_title="Elevate Daily",
    page_icon="✨",
    layout="centered",
)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# ----- MAIN CARD -----
st.markdown("""
<div class="main-card">
    <div class="hero-title">✨ Elevate Daily</div>
    <div class="hero-sub">Boost your mood, one click at a time! </div>
</div>
""", unsafe_allow_html=True)

# ----- BUTTON BAR -----
st.markdown('<div class="button-bar">', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    quote_btn = st.button("💬 Get Quote")
with col2:
    joke_btn = st.button("😂 Get Joke")
with col3:
    fact_btn = st.button("🧠 Get Fact")
st.markdown('</div>', unsafe_allow_html=True)

# ----- DISPLAY RESULTS -----
if quote_btn:
    quote = fetch_random_quote()
    st.markdown(f"<div class='quote-card'>💡 {quote['content']} — <em>{quote['author']}</em></div>", unsafe_allow_html=True)
elif joke_btn:
    joke = fetch_random_joke()
    st.markdown(f"<div class='quote-card'>😂 {joke['setup']} ... {joke['punchline']}</div>", unsafe_allow_html=True)
elif fact_btn:
    fact = fetch_random_fact()
    st.markdown(f"<div class='quote-card'>📚 {fact['text']}</div>", unsafe_allow_html=True)