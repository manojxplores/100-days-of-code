import requests
from bs4 import BeautifulSoup


class ScrapeData:
    def __init__(self):
        self.date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
        self.scraper = None

    def get_date(self):
        content = requests.get(f"https://www.billboard.com/charts/hot-100/{self.date}/#", headers=self.headers).text
        self.scraper = BeautifulSoup(content, "html.parser")
        all_divs = self.scraper.find_all("div", class_="o-chart-results-list-row-container")

        songs_list = []
        for idx, div in enumerate(all_divs):
            song = div.find_all("h3", id="title-of-a-story")[0].getText().strip()
            songs_list.append(song)

        return songs_list







