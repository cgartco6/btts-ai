from playwright.sync_api import sync_playwright

def get_page():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=True)
    return browser.new_page()
