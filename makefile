PROJECT_NAME ?= SchedulePlannerBackend
PROJECT_NAMESPACE ?= oleggr
REGISTRY_IMAGE ?= $(PROJECT_NAMESPACE)/$(PROJECT_NAME)

all:
	@echo "make run   - Run all docker containers"
	@echo "make down  - Run all docker containers"
	@exit 0

run:
	docker-compose up -d --build

down:
	docker-compose down

ssh:
	ssh oleggr@coolpoisk.ru