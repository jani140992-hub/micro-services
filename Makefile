.PHONY: help install lint test up down clean docker-build

help:
	@echo "CloudMart Microservices CLI commands:"
	@echo "  make install       Install dependencies in virtualenv"
	@echo "  make lint          Run code linters (ruff, mypy)"
	@echo "  make test          Execute automated test suites"
	@echo "  make up            Start entire microservices mesh with Docker Compose"
	@echo "  make down          Tear down Docker Compose containers and volumes"
	@echo "  make docker-build  Build Docker images for all 10 microservices"
	@echo "  make clean         Clean bytecode and test caches"

install:
	pip install -e ".[dev]"

lint:
	ruff check .
	ruff format --check .

test:
	pytest tests/ -v

up:
	docker-compose up -d

down:
	docker-compose down -v

docker-build:
	docker-compose build

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
