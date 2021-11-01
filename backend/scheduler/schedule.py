from abc import abstractmethod
from typing import List

from scheduler.models import Strategy1Model

from scheduler.utils import print_arr, copy_2d_array_structure, get_min


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
        # best_schedule_rate = len(self.field[0]) * len(self.field)
        _cpus = len(self.field[0])
        _time = len(self.field)
        best_schedule = []

        heat_map = self.build_heat_map()
        print_arr(heat_map)

        return best_schedule

    def build_heat_map(self):
        _cpus = len(self.field)
        _time = len(self.field[0])
        heat_map = copy_2d_array_structure(self.field)
        prev_min = 0

        for t in range(_time):
            curr_heat_by_t = []
            for c in range(_cpus):
                if t == 0 and self.field[c][t] == 0:
                    heat_map[c][t] = 1
                elif self.field[c][t] == self.field[c][t - 1] == 0:
                    heat_map[c][t] = heat_map[c][t - 1] + 1
                elif self.field[c][t] == 0 and self.field[c][t - 1] == 1:
                    heat_map[c][t] = prev_min + 1
                curr_heat_by_t.append(heat_map[c][t])
            prev_min = get_min(curr_heat_by_t)

        return heat_map

    def find_path(self, start, end):
        schedule, curr_rate = [
            [0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0]
        ], 2

        return schedule, curr_rate
