import json

import pytest


@pytest.fixture
def fake_request():
    import httpretty

    httpretty.enable()
    yield httpretty
    httpretty.disable()
    httpretty.reset()


@pytest.fixture
def mock_request(fake_request):
    def _mock_request(url, answer, status=200, req_type=fake_request.GET):
        fake_request.register_uri(
            req_type,
            url,
            json.dumps(answer),
            content_type="application/json",
            status=status,
        )
        return fake_request

    return _mock_request
