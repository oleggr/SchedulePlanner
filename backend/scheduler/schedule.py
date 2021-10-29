from abc import abstractmethod
from typing import List

from scheduler.models import Strategy1Model


class BasicPlanner:
    @abstractmethod
    def get_schedule(self) -> List[List[int]]: pass


class Strategy1Planner(BasicPlanner):

    field: List[List[int]]
    end_x: int

    def __init__(self, strategy_data: Strategy1Model):
        self.field = strategy_data.field
        self.end_x = strategy_data.end_x

    def get_schedule(self):
        # TODO: implement Lee algorithm
        best_schedule_rate = len(self.field[0]) * len(self.field)
        best_schedule = []

        for line in self.field:
            for i in range(len(line) - self.end_x):
                start_index = i
                end_index = i + self.end_x - 1
                curr_schedule, curr_rate = self.find_path(start_index, end_index)
                if curr_rate < best_schedule_rate:
                    best_schedule = curr_schedule

        return best_schedule

    def find_path(self, start, end):
        schedule, curr_rate = [
            [0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ], 2
        return schedule, curr_rate
