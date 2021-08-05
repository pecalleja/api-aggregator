from abc import ABC
from abc import abstractmethod


class Strategy(ABC):
    @abstractmethod
    def compute(self, elements: list[dict]):
        raise NotImplementedError


class AverageStrategy(Strategy):
    def compute(self, elements: list[dict]) -> dict:
        result = {}
        for element in elements:
            for key, value in element.items():
                result[key] = result.get(key, 0) + value / len(elements)

        return result
