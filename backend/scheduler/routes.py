from starlette import status
from fastapi import APIRouter, Request, status, HTTPException

from scheduler.models import Strategy1Model, Strategy1ResponseModel
from scheduler.schedule import Strategy1Planner


router = APIRouter()


@router.get(
    "/hello",
    name='dev:test-basic-get',
    status_code=status.HTTP_200_OK
)
async def hello():
    return "Hello, world!"


@router.post(
    "/strategy/1",
    name='dev:find-schedule-by-strategy-1',
    status_code=status.HTTP_200_OK,
    response_model=Strategy1ResponseModel
)
async def find_schedule_by_strategy_1(data: Strategy1Model):
    planner = Strategy1Planner(data)
    return {'result': planner.get_schedule()}


@router.post(
    "/strategy/2",
    name='dev:find-schedule-by-strategy-2',
    status_code=status.HTTP_200_OK
)
async def find_schedule_by_strategy_2():
    return "strategy 2!"


@router.post(
    "/strategy/3",
    name='dev:find-schedule-by-mode-3',
    status_code=status.HTTP_200_OK
)
async def find_schedule_by_strategy_3():
    return "strategy 3!"
