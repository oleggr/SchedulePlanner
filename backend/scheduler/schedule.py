from abc import abstractmethod
from typing import List

from scheduler.models import Strategy1Model
from scheduler.utils import print_arr, copy_2d_array, get_min


class BasicPlanner:
    @abstractmethod
    def get_schedule(self) -> List[List[int]]: pass


class Strategy1Planner(BasicPlanner):

    field: List[List[int]]
    task_workload: int
    heat_map: List[List[int]]
    best_schedule: List[List[int]]

    def __init__(self, strategy_data: Strategy1Model):
        self.field = strategy_data.field
        self.task_workload = strategy_data.task_workload

    def __repr__(self):
        return f'<Strategy1Planner> field: {self.field}'

    def get_schedule(self):
        self.build_heat_map()
        self.build_path()
        print(self.best_schedule)
        return self.best_schedule

    def build_path(self):
        best_path = copy_2d_array(self.field, only_structure=True, default_value=0)

        self.best_schedule = copy_2d_array(self.field, only_structure=True, default_value=0)

    def build_heat_map(self):
        _cpus = len(self.field)
        _time = len(self.field[0])
        heat_map = copy_2d_array(self.field, only_structure=True, default_value=None)
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

        self.heat_map = heat_map
