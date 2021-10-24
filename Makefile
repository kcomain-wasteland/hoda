
.PHONY: all package docs docs-serve check

all: dependencies package

dependencies:
	poetry install

package: dependencies
	poetry build

check: dependencies
	coverage --version
	coverage run -m pytest .

docs: dependencies
	make html --directory=docs

docs-serve: dependencies
	make serve --directory=docs

clean:
	rm -vfr dist/
	coverage erase || true
	rm -vfr htmlcov
	find -type d -name __pycache__ -exec rm -vr {} \; || true

distclean: clean
	rm -vfr *cache *_cache *.cache .*cache

lint:
	black . || true
	mypy hwa
