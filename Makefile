
.PHONY: all package docs docs-serve

all: dependencies package

dependencies:
	poetry install

package: dependencies
	poetry build

docs: dependencies
	make html --directory=docs

docs-serve: dependencies
	make serve --directory=docs

clean:
	find -type d -name __pycache__ -exec rm -vr {} \; || true

lint:
	black . || true
	mypy .
