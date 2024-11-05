install_deps:
	@echo "Installing dependencies"
	poetry install

reload_deps:
	@echo "Loading deps"
	poetry export --without-hashes > requirements.txt

run_app:
	@echo "Running main"
	poetry run python src/main.py

run_docker_app:
	@echo "Running docker app"