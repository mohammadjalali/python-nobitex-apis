check:
	ruff check
	ruff check --select I
	mypy src/nobitex
