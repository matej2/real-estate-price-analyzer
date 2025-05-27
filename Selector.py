from bs4 import BeautifulSoup


class Selector:
    value_selector = "#vsebina200 .grey.tac"

    def __init__(self, soup: BeautifulSoup):
        self.soup = soup

    def get_value(self):
        return self.soup.find(self.value_selector)

