MAIN = pac-man.py
MYPY_FLAGS = --warn-return-any --warn-unused-ignores --ignore-missing-imports \
--disallow-untyped-defs --check-untyped-defs
VENV = .venv
CONFIG = src/config.json

install:
	uv sync

run:
	uv run python3 $(MAIN) $(CONFIG)

debug:
	uv run python3 -m pdb $(MAIN) $(CONFIG)

clean:
	@rm -rf $$(find . -type d -name "__pycache__") $$(find . -type d -name ".mypy_cache")
	@rm -rf build dist

lint:
	uv run python3 -m flake8 . --exclude $(VENV)
	uv run python3 -m mypy . $(MYPY_FLAGS)

lint-strict:
	uv run python3 -m flake8 . --exclude $(VENV)
	uv run python3 -m mypy . $(MYPY_FLAGS) --strict

.PHONY: install run debug clean lint lint-strict
