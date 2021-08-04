from .api import Api
from .strategy import Strategy


class ApiAggregator:
    apis: list[Api]
    strategy: Strategy

    def __init__(self, apis, aggregator_strategy):
        self.apis = apis
        self.strategy = aggregator_strategy

    def coalesce(self, member_id) -> dict:
        result = []
        for api_element in self.apis:
            result.append(api_element.request(member_id=member_id))

        return self.strategy.compute(result)
