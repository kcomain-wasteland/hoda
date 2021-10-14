
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
