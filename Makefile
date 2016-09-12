test:
	cd tests;PYTHONPATH=.. pytest --tb=short

install:
	pip install -r requirements.txt

lint:
	pylint --disable=R,C sensible

clean:
	find . -name '*.pyc' -delete
