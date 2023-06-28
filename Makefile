# Application: prefect
server_start:
	prefect server start

config_set_local_api:
	prefect config set PREFECT_API_URL="http://localhost:4200/api"
	prefect config set PREFECT_API_DATABASE_CONNECTION_URL="postgresql+asyncpg://postgres:yourTopSecretPassword@prefect-postgres:5432/prefect"

# Developing
update_packages:
	poetry update
	poetry export --without-hashes -f requirements.txt --output requirements.txt
	poetry export --without-hashes --with dev -f requirements.txt --output requirements-dev.txt
