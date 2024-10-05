import requests
from bs4 import BeautifulSoup


def make_request(url: str) -> BeautifulSoup:
    response = requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    })

    assert response.status_code == 200
    return BeautifulSoup(response.content, 'html.parser')
