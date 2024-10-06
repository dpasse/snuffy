import requests
from bs4 import BeautifulSoup

from selenium import webdriver


def make_request(url: str) -> BeautifulSoup:
    response = requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    })

    assert response.status_code == 200
    return BeautifulSoup(response.content, 'html.parser')


class Browser:
    def make_request(self, url: str) -> BeautifulSoup:
        self._browser.get(url)
        return BeautifulSoup(self._browser.page_source, 'html.parser')

    def __enter__(self):
        self._browser = webdriver.Firefox()
        return self
    
    def __exit__(self, exception_type, exception_value, exception_traceback):
        self._browser.quit()
