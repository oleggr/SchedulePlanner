from abc import abstractmethod
from typing import List

from scheduler.models import Strategy1Model


class BasicPlanner:
    @abstractmethod
    def get_schedule(self) -> List[List[int]]: pass


class Strategy1Planner(BasicPlanner):

    field: List[List[int]]
    completion_time: int

    def __init__(self, strategy_data: Strategy1Model):
        self.field = strategy_data.field
        self.completion_time = strategy_data.completion_time

    def __repr__(self):
        return f'<Strategy1Planner> field: {self.field}'

    def get_schedule(self):
        best_schedule_rate = len(self.field[0]) * len(self.field)
        best_schedule = []

        for i in range(len(self.field)):
            for j in range(len(self.field[i]) - self.completion_time):
                start_index = (i, j)
                end_index = (i, j + self.completion_time)
                curr_schedule, curr_rate = self.find_path(start_index, end_index)
                if curr_rate < best_schedule_rate:
                    best_schedule = curr_schedule

        return best_schedule

    def find_path(self, start, end):
        schedule, curr_rate = [
            [0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0]
        ], 2

        return schedule, curr_rate
