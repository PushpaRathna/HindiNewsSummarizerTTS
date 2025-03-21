import requests
from bs4 import BeautifulSoup

def fetch_news(company_name):
    search_url = f"https://www.bbc.com/search?q={company_name}"
    response = requests.get(search_url)

    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    articles = []

    for item in soup.find_all("article")[:10]:  # Extract top 10 articles
        title = item.find("h1").text if item.find("h1") else "No Title"
        link = item.find("a")["href"] if item.find("a") else "#"
        articles.append({"title": title, "link": link, "content": fetch_article_content(link)})

    return articles

def fetch_article_content(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return "Content Not Available"
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = [p.text for p in soup.find_all("p")]
        return " ".join(paragraphs)
    except:
        return "Failed to retrieve content"
