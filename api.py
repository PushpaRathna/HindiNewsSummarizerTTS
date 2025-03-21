from fastapi import FastAPI
from news_scraper import fetch_news
from summarizer import summarize_text
from sentiment_analysis import analyze_sentiment
from tts import generate_tts

app = FastAPI()

@app.post("/fetch_news")
async def get_news(company: dict):
    company_name = company["company"]
    news_articles = fetch_news(company_name)

    results = []
    for article in news_articles:
        summary = summarize_text(article["content"])
        sentiment = analyze_sentiment(article["content"])
        topics = extract_topics(article["content"])
        tts_audio = generate_tts(summary)

        results.append({
            "title": article["title"],
            "summary": summary,
            "sentiment": sentiment,
            "topics": topics,
            "audio": tts_audio
        })

    return {"company": company_name, "articles": results}
