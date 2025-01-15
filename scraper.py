from llm_helper import get_pagination_info
from playwright.sync_api import sync_playwright

def scrape_reviews(url):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(url)

        with open('page_content.html', 'w') as f:
            f.write(page.content())
            
        #get the content of the page
        pagination_info = get_pagination_info(page.content())
        browser.close()
    return pagination_info
