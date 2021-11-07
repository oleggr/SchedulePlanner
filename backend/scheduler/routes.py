import hashlib
from random import random

from starlette import status
from fastapi import APIRouter, Request, HTTPException

from scheduler.config import auth_token
from scheduler.schedule import Strategy1Planner
from scheduler.storage.storage_factory import StorageFactory
from scheduler.models import Strategy1Model, Strategy1ResponseModel


router = APIRouter()


async def validate_request(request: Request):
    try:
        user_token = request.headers['token']
        if not auth_token == user_token:
            raise Exception
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Token incorrect: {e}",
        )


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
    await validate_request(request)

    request = await request.json()
    data = Strategy1Model(**request)

    # TODO add hashing of useful params and move it to strategy planner
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
