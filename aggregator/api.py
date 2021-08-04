import requests


class Api:
    def __init__(self, url):
        self.url = url

    def request(self, **kwargs) -> dict:
        return requests.get(self.url, params=kwargs).json()
