test:
	python -m pytest

lint:
	flake8

up:
	docker-compose up -d

down:
	docker-compose down
