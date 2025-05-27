import cloudscraper
import requests
from bs4 import BeautifulSoup

from Selector import Selector


class Main:
    def run(self):
        self.clf = cloudscraper.create_scraper()
        soup = BeautifulSoup(self.get_content().text, 'html.parser')
        selector = Selector(soup)

        print(selector.get_average_price())

    def get_content(self):
        response = self.clf.get("https://www.nepremicnine.net/oglasi-prodaja/ljubljana-mesto/lj-siska/stanovanje/")
        if response.status_code != 200:
            raise Exception(f"The request failed with an error {response.status_code}")
        else:
            return response


if __name__ == "__main__":
    Main().run()