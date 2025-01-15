from llm_helper import get_pagination_info, get_reviews
from playwright.sync_api import sync_playwright
import time, json

def scrape_reviews(url):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)

        with open('page_content.html', 'w') as f:
            f.write(page.content())

        reviews = get_reviews(page.content())

        browser.close()

    lines = reviews.splitlines()
    reviews = "\n".join(lines[1:-1])

    # Log the response for debugging
    with open('reviews.txt', 'w') as f:
        f.write(time.strftime("%Y-%m-%d %H:%M:%S") + "\n\n" + reviews)

    try:
        reviews_data = json.loads(reviews)
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse reviews JSON: {e}")

    return reviews_data
