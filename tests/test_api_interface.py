def test_api_interface_create_object():
    from aggregator.api import Api

    assert Api("https://api1.com")
