# Variables
PYTHON := python3
PIP := pip3

# Targets and Rules
.PHONY: install test clean

install:
	$(PIP) install -r requirements.txt

test:
	$(PYTHON) -m pytest src/tests/*.py -v

clean:
	rm -rf __pycache__ .pytest_cache

# Default target when running 'make' without any specific target
all: install test clean up


up:
	docker-compose -f docker-compose.yml up -d

down:
	docker-compose -f docker-compose.yml down