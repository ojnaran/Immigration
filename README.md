# MaplePath Prototype

This repository contains a minimal prototype for the **MaplePath** immigration app.

## Features

* **Data Scraper** - `scraper/scrape_canada.py` fetches links from the official [canada.ca](https://www.canada.ca/en/services/immigration-citizenship.html) website and stores them in `data/immigration_links.json` with a timestamp.

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the scraper:

```bash
python scraper/scrape_canada.py
```

The script prints how many links were saved and stores them in the `data` directory. Each output JSON includes the source URL and a `last_updated` timestamp.

This is a starting point for syncing official immigration information into the MaplePath app.

**Note:** The scraping script requires internet access. If running in a restricted environment, it may fail to fetch the official website. Run it locally with network access to update the data.
