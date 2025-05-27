import re

from bs4 import BeautifulSoup


class Selector:
    value_selector = "#vsebina200 .grey.tac"

    def __init__(self, soup: BeautifulSoup):
        self.soup = soup

    def get_average_price_text(self):
        return self.soup.select(self.value_selector)[0].text

    def get_average_price(self):
        txt = self.get_average_price_text()
        title_search = re.search(':\\s(.*)EUR', txt, re.IGNORECASE)

        title = None
        if title_search:
            title = title_search.group(1)
        return title

