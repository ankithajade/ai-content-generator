import requests

# ---------------- Quotes ----------------
def fetch_random_quote():
    url = "https://api.quotable.io/random"
    response = requests.get(url, verify=False)
    data = response.json()
    return data

# ---------------- Jokes ----------------
def fetch_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url, verify=False)
    data = response.json()
    return data

# ---------------- Facts ----------------
def fetch_random_fact():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    response = requests.get(url, verify=False)
    data = response.json()
    return data
