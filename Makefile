
.PHONY: all package docs docs-serve check

all: dependencies package

dependencies:
	poetry install

package: dependencies
	poetry build

check: dependencies
	coverage --version
	coverage run -m pytest .

coverage: check
	coverage report -m
	coverage html --show-contexts

docs: dependencies
	make html --directory=docs

docs-serve: dependencies
	make serve --directory=docs

docs-i18n-update: dependencies
	$(MAKE) gettext --directory=docs
	# To generate new languages, append -l <LANG> to the following command,
	sphinx-intl update -p docs/build/gettext -d docs/source/locale

clean:
	rm -vfr dist/
	coverage erase || true
	rm -vfr htmlcov
	find -type d -name __pycache__ -exec rm -vr {} \; || true

distclean: clean
	rm -vfr *cache *_cache *.cache .*cache

lint:
	black . || true
	mypy hoda
