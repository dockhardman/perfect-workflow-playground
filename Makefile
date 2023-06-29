# Application: prefect
server_start:
	prefect server start

config_set_local_api:
	prefect config set PREFECT_API_URL="http://localhost:4200/api"
	prefect config set PREFECT_API_DATABASE_CONNECTION_URL="postgresql+asyncpg://postgres:yourTopSecretPassword@prefect-postgres:5432/prefect"

build_deployments:
	prefect deployment build \
		-n env_info \
		-p worker-pool \
		--storage-block gcs/prefect-workflow \
		-o prefect_workflow/deployments/deploy-env-info.yaml \
		prefect_workflow/flows/env_info.py:get_env_info

apply_deployments:
	prefect deployment apply prefect_workflow/deployments/deploy-env-info.yaml

# Developing
update_packages:
	poetry update
	poetry export --without-hashes -f requirements.txt --output requirements.txt
	poetry export --without-hashes --with dev -f requirements.txt --output requirements-dev.txt
