.PHONY: help
.DEFAULT_GOAL := help

IMAGE_TAG := pproject
PORT := 5000

help:
	@grep -h -E '^[a-zA-Z0-9_-]+:.*?# .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?# "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: build
build: # Build the docker image
	docker build -t $(IMAGE_TAG) .

.PHONY: run
run: # Run the docker image
	docker run -d -p $(PORT):5000 $(IMAGE_TAG)

.PHONY: stop
stop: # Stop the docker container
	docker stop $$(docker ps -q --filter ancestor=$(IMAGE_TAG))

.PHONY: clean
clean: # Remove all related docker images and containers
	docker rm $$(docker ps -a -q --filter ancestor=$(IMAGE_TAG))
	docker rmi $(IMAGE_TAG)

.PHONY: format-check
format-check: # Run the format in container
	docker run $(IMAGE_TAG) bash -c "python -m black --check ."

.PHONY: lint
lint: # Run linting in container
	docker run $(IMAGE_TAG) bash -c "python -m ruff check ."

.PHONY: git-hook
git-hook: # Set the git hook path
	git config core.hooksPath .git_hooks

VENV=venv
PYTHON=$(VENV)/bin/python3

.PHONY: dev-build
dev-build: # Create a virtual environment and install the dependencies
	python3.10 -m venv $(VENV)
	$(PYTHON) -m pip install -r requirements.txt

.PHONY: dev-run
dev-run: # Run the server in the virtual environment
	$(PYTHON) -m flask run --debug -p $(PORT)

.PHONY: dev-format
dev-format: # Format the code using black
	$(PYTHON) -m black .

.PHONY: dev-format-check
dev-format-check: # Check the code format using black
	$(PYTHON) -m black --check .

.PHONY: dev-lint
dev-lint: # Lint the code using ruff
	$(PYTHON) -m ruff check .

.PHONY: tree
tree: # Show project structure
	tree -I "venv|__pycache__"
