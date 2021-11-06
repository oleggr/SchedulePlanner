PROJECT_NAME ?= SchedulePlannerBackend
PROJECT_NAMESPACE ?= oleggr
REGISTRY_IMAGE ?= $(PROJECT_NAMESPACE)/$(PROJECT_NAME)

all:
	@echo "make local	- Run app locally"
	@exit 0

local:
	uvicorn scheduler.app:app --reload
