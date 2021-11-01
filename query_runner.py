#!/Users/o.gritchin/dev/github/SchedulePlanner/venv/bin/python3

import json
import requests
from argparse import ArgumentParser

from pathfinding.core.grid import Grid


API_HOST = 'http://localhost:8000/api'
STRATEGY_1_PATH = '/strategy/1'
STRATEGY_2_PATH = '/strategy/2'


def callback_strategy_1(arguments):
    print('strategy1 callback')
    data = {
        'field': [
            [0, 0, 0, 0, 0, 1],
            [0, 0, 1, 1, 1, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
        ],
        'end_x': 5
    }
    r = requests.post(API_HOST + STRATEGY_1_PATH, json=data)
    res = r.json()
    grid = Grid(matrix=res['result'])
    print(grid.grid_str())


def callback_strategy_2(arguments):
    print('strategy2 callback')
    requests.post(API_HOST + STRATEGY_2_PATH)


def callback_strategy_3(arguments):
    print('strategy3 callback')


def setup_parser(parser):
    """Setup parser method"""

    subparsers = parser.add_subparsers(help="choose strategy")

    # Parser for strategy1 command
    strategy_1_parser = subparsers.add_parser(
        "strategy1", help="build plan by strategy 1"
    )
    strategy_1_parser.set_defaults(callback=callback_strategy_1)

    # Parser for strategy2 command
    strategy_2_parser = subparsers.add_parser(
        "strategy2", help="build plan by strategy 2"
    )
    strategy_2_parser.set_defaults(callback=callback_strategy_2)

    # Parser for strategy3 command
    strategy_3_parser = subparsers.add_parser(
        "strategy3", help="build plan by strategy 3"
    )
    strategy_3_parser.set_defaults(callback=callback_strategy_3)


def main():
    """Main method"""
    parser = ArgumentParser(
        description="CLI Interface for schedule planner."
    )
    setup_parser(parser)
    arguments = parser.parse_args()
    arguments.callback(arguments)


if __name__ == "__main__":
    main()
