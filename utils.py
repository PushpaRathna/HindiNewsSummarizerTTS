def extract_topics(text):
    keywords = ["business", "market", "technology", "regulations"]
    return [word for word in keywords if word in text.lower()]
