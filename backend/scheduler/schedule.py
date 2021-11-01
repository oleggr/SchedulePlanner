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
    _cpus: int
    _time: int
    heat_map: List[List[int]]
    min_heat_by_time: List
    best_schedule: List[List[int]]

    def __init__(self, strategy_data: Strategy1Model):
        self.field = strategy_data.field
        self._cpus = len(self.field)
        self._time = len(self.field[0])
        self.task_workload = strategy_data.task_workload
        self.min_heat_by_time = []

    def __repr__(self):
        return f'<Strategy1Planner> field: {self.field}'

    def get_schedule(self):
        best_rate = -1

        for start_c in range(self._cpus):
            if self.field[start_c][0] == 1:
                continue

            schedule, rate = self.build_path(start_c)

            if best_rate == -1:
                best_rate = rate
                self.best_schedule = schedule

            if rate < best_rate:
                best_rate = rate
                self.best_schedule = schedule

        return self.best_schedule

    def build_path(self, start_c):
        start_t = 1
        best_path = copy_2d_array(self.field, only_structure=True)

        best_path[start_c][0] = 1
        prev_c = start_c

        migrations_count = 0

        for t in range(start_t, self._time):
            tmp = 0
            modified = 1
            for c in range(self._cpus):
                if c == prev_c and self.field[c][t] == 0:
                    best_path[c][t] = 1
                    modified = 0
                    continue
                elif c != prev_c and self.field[c][t] == 0:
                    tmp = c  # migration++

            if modified:
                best_path[tmp][t] = 1
                prev_c = tmp
                migrations_count += 1

        return best_path, migrations_count

    def build_heat_map(self):
        """
        Currently unused method
        :return:
        """
        heat_map = copy_2d_array(self.field, only_structure=True, default_value=None)
        prev_min = 0

        for t in range(self._time):
            curr_heat_by_t = []

            for c in range(self._cpus):
                if t == 0 and self.field[c][t] == 0:
                    heat_map[c][t] = 1
                elif self.field[c][t] == self.field[c][t - 1] == 0:
                    heat_map[c][t] = heat_map[c][t - 1] + 1
                elif self.field[c][t] == 0 and self.field[c][t - 1] == 1:
                    heat_map[c][t] = prev_min + 1
                curr_heat_by_t.append(heat_map[c][t])

            prev_min = get_min(curr_heat_by_t)
            self.min_heat_by_time.append(prev_min)

        self.heat_map = heat_map
