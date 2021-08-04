from aggregator import ApiAggregator
from aggregator.api import Api
from aggregator.strategy import AverageStrategy


class TestApiInterface:
    url = "https://api1.com"

    def test_create_object(self):
        assert Api(self.url)

    def test_make_a_request(self, mock_request):
        api = Api(self.url)
        mock_request(self.url, {"foo": "bar"})
        result = api.request(foo="bar")
        assert result
        assert isinstance(result, dict)


class TestAggregatorInterface:
    urls = {
        "https://api1.com": {
            "deductible": 1000,
            "stop_loss": 10000,
            "oop_max": 5000,
        },
        "https://api2.com": {
            "deductible": 1200,
            "stop_loss": 13000,
            "oop_max": 6000,
        },
        "https://api3.com": {
            "deductible": 1000,
            "stop_loss": 10000,
            "oop_max": 6000,
        },
    }

    def test_create_aggregator(self, mock_request):
        for url, response in self.urls.items():
            mock_request(url, response)
        apis = [Api(url) for url in self.urls.keys()]
        result = ApiAggregator(apis, AverageStrategy()).coalesce(1)
        assert result
        assert isinstance(result, dict)
        for key in ["deductible", "stop_loss", "oop_max"]:
            assert key in result
