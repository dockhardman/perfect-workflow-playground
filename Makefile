# Application: prefect
server_start:
	prefect server start

# Developing
update_packages:
	poetry update
	poetry export --without-hashes -f requirements.txt --output requirements.txt
	poetry export --without-hashes --with dev -f requirements.txt --output requirements-dev.txt
