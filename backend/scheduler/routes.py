import hashlib
from random import random

from starlette import status
from fastapi import APIRouter, Request, HTTPException

from scheduler.models import Strategy1Model, Strategy1ResponseModel
from scheduler.schedule import Strategy1Planner
from scheduler.storage.storage_factory import StorageFactory


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
async def find_schedule_by_strategy_1(request: Request):
        # data: Strategy1Model):
    request = await request.json()
    data = Strategy1Model(**request)

    field_hash = hashlib.sha224(str(data.field).encode()).hexdigest()
    StorageFactory.get_storage().put(field_hash, {'test': random()})

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
