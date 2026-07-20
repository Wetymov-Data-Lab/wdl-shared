.PHONY: sync lint typecheck test check

# Development
sync:
	uv sync --all-extras --group dev
lint:
	uv run ruff check .
typecheck:
	uv run mypy src
test:
	uv run pytest
check: sync lint typecheck test