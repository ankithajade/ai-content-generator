from utils.api_helpers import fetch_random_quote, fetch_random_joke, fetch_random_fact
import streamlit as st
from utils.api_helpers import fetch_random_quote
# Cache the quote for 2 minutes to reduce API calls
# Cache quotes for 2 minutes
@st.cache_data(ttl=120)
def get_quote():
    return fetch_random_quote()

# Cache jokes for 2 minutes
@st.cache_data(ttl=120)
def get_joke():
    return fetch_random_joke()

# Cache facts for 2 minutes
@st.cache_data(ttl=120)
def get_fact():
    return fetch_random_fact()


st.title("✨ Fun & Motivation Generator ✨")
st.write("Press any of the buttons below to brighten your day!")

if st.button("Get Quote"):
    quote = get_quote()
    st.success(f"💡 {quote['content']} — *{quote['author']}*")

if st.button("Get Joke"):
    joke = get_joke()
    st.info(f"😂 {joke['setup']} ... {joke['punchline']}")

if st.button("Get Fact"):
    fact = get_fact()
    st.warning(f"📚 {fact['text']}")

