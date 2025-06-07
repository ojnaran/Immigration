import json
from datetime import datetime
from pathlib import Path

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.canada.ca/en/services/immigration-citizenship.html"


def fetch_links():
    response = requests.get(BASE_URL, timeout=15)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    links = []
    # Example: collect navigation links from the page
    for link in soup.select("a[href]"):
        href = link.get("href")
        text = link.get_text(strip=True)
        if href and text:
            if href.startswith("https://www.canada.ca") and len(text.split()) > 1:
                links.append({"title": text, "url": href})
    return links


def main():
    links = fetch_links()
    out = {
        "last_updated": datetime.utcnow().isoformat() + "Z",
        "source": BASE_URL,
        "links": links,
    }
    Path("data").mkdir(exist_ok=True)
    outfile = Path("data/immigration_links.json")
    outfile.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"Saved {len(links)} links to {outfile}")


if __name__ == "__main__":
    main()
