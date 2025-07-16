.PHONY: help
.DEFAULT_GOAL := help

IMAGE_TAG := flask-structure
PORT := 5000

help:
	@grep -h -E '^[a-zA-Z0-9_-]+:.*?# .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?# "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

# .PHONY: build
build: # Build the docker image
	docker build -t $(IMAGE_TAG) .

# .PHONY: run
run: # Run the docker image
	docker run -d -v $(PWD):/app -p $(PORT):5000 $(IMAGE_TAG)

# .PHONY: stop
stop: # Stop the docker container
	docker stop $$(docker ps -q --filter ancestor=$(IMAGE_TAG))

# .PHONY: clean
clean: # Remove all related docker images and containers
	docker rm $$(docker ps -a -q --filter ancestor=$(IMAGE_TAG))
	docker rmi $(IMAGE_TAG)

# .PHONY: format-check
format-check: # Run the format in container
	docker run $(IMAGE_TAG) bash -c "python -m black --check ."

# .PHONY: lint
lint: # Run linting in container
	docker run $(IMAGE_TAG) bash -c "python -m ruff check ."

# .PHONY: git-hook
git-hook: # Set the git hook path
	git config core.hooksPath .git_hooks

# .PHONY: tree
tree: # Show project structure
	tree -I "venv|.venv|__pycache__"

# .PHONY: test
test: # Test endpoints with curl
	curl -X POST http://127.0.0.1:5000/numbers/42
	curl -X POST http://127.0.0.1:5000/numbers/43
	curl -X POST http://127.0.0.1:5000/letters/word
	curl -X POST http://127.0.0.1:5000/letters/42
	curl -X GET http://127.0.0.1:5000/unique/
