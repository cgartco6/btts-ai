from scraper.browser import get_page
from bs4 import BeautifulSoup
from database import conn

def scrape_live_odds(bookmaker_url, bookmaker_name):
    page = get_page()
    page.goto(bookmaker_url, timeout=60000)
    soup = BeautifulSoup(page.content(), "lxml")

    matches = soup.select("div.match")

    for m in matches:
        try:
            teams = m.select_one(".teams").text.strip()
            odds_yes = float(m.select_one(".btts-yes").text)
            odds_no = float(m.select_one(".btts-no").text)

            match_id = teams.replace(" ", "_").lower()

            conn.execute("""
            INSERT INTO odds (match_id, bookmaker, btts_yes, btts_no)
            VALUES (?, ?, ?, ?)
            """, (match_id, bookmaker_name, odds_yes, odds_no))

        except Exception:
            continue

    conn.commit()
