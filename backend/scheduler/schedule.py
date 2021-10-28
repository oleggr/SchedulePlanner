from abc import abstractmethod
from typing import List

from scheduler.models import Strategy1


class BasicPlanner:
    @abstractmethod
    def path_find(self) -> List[List[int]]: pass


class Strategy1Planner(BasicPlanner):

    field: List[List[int]]
    start_x: int
    end_x: int

    def __init__(self, strategy_data: Strategy1):
        field = strategy_data.field
        start_x = strategy_data.start_x
        end_x = strategy_data.end_x

    def path_find(self):
        # TODO: implement Lee algorithm
        pass
