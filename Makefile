install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

lint:
	poetry run flake8 gendiff

build:
	poetry build #собираем пакет

publish:
	poetry publish --dry-run #отладка публикации

package-install:
	python3.10 -m pip install --user dist/*.whl