TEST_COMPOSE_FILE := docker-compose-test.yml
DEV_COMPOSE_FILE := docker-compose.yml

build:
	docker build -t books-app:latest -f Dockerfile .

run-stack:
	docker compose -f $(DEV_COMPOSE_FILE) up

lint:
	ruff format

all-tests:
	docker-compose -f $(TEST_COMPOSE_FILE) exec app pytest tests

test-stack-up:
	docker-compose -f $(TEST_COMPOSE_FILE) up -d --force-recreate

dev-stack-up:
	docker compose -f $(DEV_COMPOSE_FILE) up --build