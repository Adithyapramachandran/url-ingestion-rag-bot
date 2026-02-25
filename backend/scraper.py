#Add recursive website scraping module
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def scrape_page(url):
    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")

        text = soup.get_text(separator=" ", strip=True)
        links = [urljoin(url, a["href"]) for a in soup.find_all("a", href=True)]

        return text, links

    except Exception as e:
        print("Scrape error:", e)
        return "", []


def scrape_recursive(start_url, depth=1):
    visited = set()
    texts = []

    def crawl(url, d):
        if url in visited or d > depth:
            return

        visited.add(url)

        text, links = scrape_page(url)

        if text:
            texts.append(text)

        for link in links[:5]:  # limit links
            crawl(link, d + 1)

    crawl(start_url, 0)

    return texts
