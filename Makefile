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
	@rm -rf __pycache__ .mypy_cache .pytest_cache build dist
	@find src -type d -name "__pycache__" -exec rm -rf {} +

lint:
	uv run python3 -m flake8 . --exclude $(VENV)
	uv run python3 -m mypy . $(MYPY_FLAGS) --exclude $(VENV)

lint-strict:
	uv run python3 -m flake8 . --exclude $(VENV)
	uv run python3 -m mypy . $(MYPY_FLAGS) --strict --exclude $(VENV)

.PHONY: install run debug clean lint lint-strict