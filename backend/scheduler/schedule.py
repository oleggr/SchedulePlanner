from abc import abstractmethod
from typing import List

from scheduler.models import Strategy1Model, Strategy1ResponseModel


class BasicPlanner:
    @abstractmethod
    def path_find(self) -> List[List[int]]: pass


class Strategy1Planner(BasicPlanner):

    field: List[List[int]]
    start_x: int
    end_x: int

    def __init__(self, strategy_data: Strategy1Model):
        field = strategy_data.field
        start_x = strategy_data.start_x
        end_x = strategy_data.end_x

    def path_find(self) -> Strategy1ResponseModel:
        # TODO: implement Lee algorithm
        return Strategy1ResponseModel(result="strategy 1!")
