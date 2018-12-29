.PHONY: clean clean-test clean-pyc clean-build docs up down wipe help mypy lint pytest
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr docs/_build/*
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	rm -rf .mypy_cache

clean-test: ## remove test and coverage artifacts
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

clean: clean-build clean-pyc clean-test ## runs all cleas


lint: ## check style with pylint
	pylint pyarchops_dnsmasq tests

mypy: ## check types with mypy
	mypy pyarchops_dnsmasq tests

pytest: ## run tests quickly with the default Python
	py.test

coverage: ## check code coverage quickly with the default Python
	coverage run --source pyarchops_dnsmasq -m pytest
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/pyarchops_dnsmasq.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ pyarchops_dnsmasq
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	echo 'to see the docs execute: $(BROWSER) docs/_build/html/index.html'


servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

release: dist ## package and upload a release
	twine upload dist/*

dist: clean ## builds source and wheel package
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

install: clean ## install the package to the active Python's site-packages
	python setup.py install

up: down ## starts development tmuxp mode
	./.bootstrap.sh && tmuxp load .tmuxp.yaml

down: ## stops development tmuxp mode
	tmux kill-session -t python-project || true

wipe: clean ## cleans .venv and other files
	rm -rf .venv
	rm -rf .npm-packages
	rm -rf .pyenv
	find . -name __pycache__ | xargs -i rm -rf {}
	rm -rf .eggs
	rm -rf .mpypy_cache
	rm -rf *.egg-info
	rm -rf .eggs
	rm -rf .pytest_cache


