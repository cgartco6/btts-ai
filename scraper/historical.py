from bs4 import BeautifulSoup
from scraper.browser import get_page
from database import conn

def scrape_team_history(team_url):
    page = get_page()
    page.goto(team_url, timeout=60000)
    soup = BeautifulSoup(page.content(), "lxml")

    rows = soup.select("table.matches tbody tr")
    data = []

    for r in rows:
        goals = r.select_one(".score")
        if not goals: continue
        hg, ag = map(int, goals.text.split("-"))
        data.append((hg, ag, int(hg>0 and ag>0)))

    return data
