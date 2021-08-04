# api-aggregator

usage
-----
```python
from aggregator import ApiAggregator
from aggregator.api import Api
from aggregator.strategy import AverageStrategy
apis = [
    Api("https://api1.com"),
    Api("https://api2.com"),
    Api("https://api3.com"),
]
result = ApiAggregator(
    apis, AverageStrategy()
).coalesce(member_id=1)
```

dependencies
-------

```bash
$ python -m pip install -r requirements.txt
```

testing
-------

```bash
$ pytest
```

todo
----
* look for corner cases requirements ( eg: different response formats, bad results, api response errors)
* round the results in average strategy
* make parallel requests
* refactor and implement factory for api creator
*
