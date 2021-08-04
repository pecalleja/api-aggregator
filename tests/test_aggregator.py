from aggregator.api import Api


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
