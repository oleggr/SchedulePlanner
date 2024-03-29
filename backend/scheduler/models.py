from typing import List
from pydantic import BaseModel, validator


class Strategy1Model(BaseModel):
    field: List[List[int]]
    task_workload: int

    @validator('task_workload')
    def check_start(cls, v, values, **kwargs):
        if 'field' in values and not (0 <= v < len(values['field'][0])):
            raise ValueError(
                f"Unacceptable border value: {v}. "
                f"Value must be 0 <= X < {len(values['field'][0])}"
            )
        return v


class Strategy1ResponseModel(BaseModel):
    result: List[List[int]]
