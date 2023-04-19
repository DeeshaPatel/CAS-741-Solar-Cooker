PIP = pip3
PYTHON = $(VENV_NAME)/bin/python3
SOURCE_DIR = src
MAIN = main.py
SEP=/
TEST = testing
REQUIREMENTS = requirements.txt
VENV_NAME := venv

.PHONY: venv install run test flake

venv:
	@echo "Creating virtual environment..."
	python3 -m venv $(VENV_NAME)
	$(PYTHON) -m pip install --upgrade pip

install: venv
	@echo "Installing dependencies..."
	$(PYTHON) -m pip install -r $(REQUIREMENTS)

run: venv install
	@echo "Running Python code..."
	PYTHONPATH=$$PYTHONPATH:src $(PYTHON) src/main.py

test:
	@echo "Running test case..."
	PYTHONPATH=$$PYTHONPATH:testing $(PYTHON) -m pytest $(TEST)
	#$(PYTHON) src/ -m pytest $(TEST)

flake:
	@echo "Flake 8 testing..."
	$(PYTHON) -m flake8 src/*.py