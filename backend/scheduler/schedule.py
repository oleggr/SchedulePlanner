from abc import abstractmethod
from typing import List

from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

from scheduler.models import Strategy1Model


class BasicPlanner:
    @abstractmethod
    def get_schedule(self) -> List[List[int]]: pass


class Strategy1Planner(BasicPlanner):

    field: List[List[int]]
    end_x: int
    finder = AStarFinder

    def __init__(self, strategy_data: Strategy1Model):
        self.field = strategy_data.field
        self.end_x = strategy_data.end_x

    def get_schedule(self):
        best_schedule_rate = len(self.field[0]) * len(self.field)
        best_schedule = []

        for i in range(len(self.field)):
            for j in range(len(self.field[i]) - self.end_x):
                start_index = (i, j)
                end_index = (i, j + self.end_x)
                curr_schedule, curr_rate = self.find_path(start_index, end_index)
                if curr_rate < best_schedule_rate:
                    best_schedule = curr_schedule

        return best_schedule

    def find_path(self, start, end):
        grid = Grid(matrix=self.field)
        start = grid.node(start[1], start[0])
        end = grid.node(end[1], end[0])

        route = self.finder(
            diagonal_movement=DiagonalMovement.always,
            time_limit=10
        )
        path, runs = route.find_path(start, end, grid)
        # print('operations:', runs, 'path length:', len(path))
        # print(grid.grid_str(path=path, start=start, end=end))

        schedule, curr_rate = [
            [0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ], 2
        return schedule, curr_rate
