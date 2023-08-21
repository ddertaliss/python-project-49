install:
	poetry install
brain-games:
	poetry run brain-games
build:
	poetry build
done:
	poetry install
	poetry build
	poetry publish --dry-run
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
lint:
	poetry run flake8 brain_games
brain-even:
	poetry run brain-eve
brain-calc:
	poetry run brain-calc
brain-gcd:
	poetry run brain-gcd
brain-progression:
	poetry run brain-progression

