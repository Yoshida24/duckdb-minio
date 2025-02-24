.PHONY: run
run:
	uv run python src/main.py

.PHONY: fmt
fmt:
	@uvx ruff format
	@uvx ruff check --fix --extend-select I

.PHONY: test
test:
	@echo "Define your test!"
