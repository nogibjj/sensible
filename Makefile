test:
	cd tests;PYTHONPATH=.. pytest --cov=sensible *.py

install:
	pip install -r requirements.txt

lint:
	pylint --disable=R,C sensible

clean:
	find . -name '*.pyc' -delete

release:
	python setup.py sdist bdist_wheel upload

all: lint test
