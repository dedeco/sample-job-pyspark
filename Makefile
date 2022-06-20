MYPY_OPTIONS = --ignore-missing-imports --disallow-untyped-calls --disallow-untyped-defs --disallow-incomplete-defs

.PHONY: unit-test
unit-test:
	poetry run pytest tests

requirements.txt:
	poetry export -f requirements.txt --output requirements.txt --dev

