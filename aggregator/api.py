from abc import ABC


class AbstractApi(ABC):
    url: str

    def __init__(self, url):
        self.url = url


class Api(AbstractApi):
    pass
