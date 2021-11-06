PROJECT_NAME ?= SchedulePlannerBackend
PROJECT_NAMESPACE ?= oleggr
REGISTRY_IMAGE ?= $(PROJECT_NAMESPACE)/$(PROJECT_NAME)

all:
	@echo "make dododo   - Deploy nginx configuration"
	@exit 0

dododo:
	ansible-playbook -i hosts.ini --user=oleggr deploy.yml
