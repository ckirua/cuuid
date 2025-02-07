PYTHON := python
PIP := pip
PACKAGE_NAME := cuuid
CURR_DIR := $(shell pwd)

.DEFAULT_GOAL := help

.PHONY: help
help:
	@echo "Makefile for $(PACKAGE_NAME)"
	@echo "Available commands:"
	@echo " make push		- Run reqs, build and install"
	@echo " make reqs		- Install requirements"
	@echo " make build		- Build package"
	@echo " make install		- Install package"
	@echo " make clean		- Clean up"
	@echo " make test		- Run tests"
	@echo " make lint		- Run lint"
	@echo ""
	@echo "Arguments:"
	@echo " dev=true/false	- Whether to install in development mode (default: false)"
	@echo "                   Development mode (-e) installs package in editable mode"
	@echo "                   for live code changes without reinstalling"

.PHONY: push
push:
	$(MAKE) reqs
	$(MAKE) build dev=$(dev)
	$(MAKE) install dev=$(dev)
	$(MAKE) test


.PHONY: reqs
reqs:
	$(PIP) install -r requirements.txt


.PHONY: install
install:
	@if [ "$(dev)" = "true" ]; then \
		$(PIP) install -e .; \
	else \
		$(PIP) install .; \
	fi

.PHONY: build
build:
	$(PIP) list 2>/dev/null | grep -q wheel || $(PIP) install wheel
	$(PIP) list 2>/dev/null | grep -q build || $(PIP) install build
	@if [ "$(dev)" = "true" ]; then \
		$(PYTHON) -m build --wheel --no-isolation; \
	else \
		$(PYTHON) -m build; \
	fi

.PHONY: clean
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name "*.egg" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".coverage" -exec rm -rf {} +
	find . -type d -name "build" -exec rm -rf {} +
	find . -type d -name "dist" -exec rm -rf {} +
	find . -type d -name "src" -exec rm -rf {} +
	find cedk -type f -name "*.cpython-*.so" -exec rm -f {} + 2>/dev/null || true
	find cedk -type f -name "*.cpython-*.pyd" -exec rm -f {} + 2>/dev/null || true

.PHONY: test
test:
	@$(PYTHON) -m unittest discover -s tests -p 'test_*.py' || true

.PHONY: lint
lint:
	$(PIP) list 2>/dev/null | grep -q black || $(PIP) install black
	$(PIP) list 2>/dev/null | grep -q isort || $(PIP) install isort
	black --check --exclude docs/ .
	isort --check-only --skip docs/ .


