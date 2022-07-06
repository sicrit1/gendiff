install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 gendiff

uninstall-code:
	python3 -m pip uninstall hexlet-code

pytest:
	poetry run pytest

coverage:
	poetry run pytest --cov

