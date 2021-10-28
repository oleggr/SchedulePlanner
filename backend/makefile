PROJECT_NAME ?= SchedulePlannerBackend
PROJECT_NAMESPACE ?= oleggr
REGISTRY_IMAGE ?= $(PROJECT_NAMESPACE)/$(PROJECT_NAME)

all:
	@echo "make local	- Run app locally"
#	@echo "make docker	- Run app and db docker containers"
#	@echo "make db		- Run only db container"
	@exit 0

local:
	uvicorn scheduler.app:app --reload

#docker:
#	docker-compose up -d --build

#db:
#	docker-compose run -d --service-ports db
