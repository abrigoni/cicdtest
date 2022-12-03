# SETUP

# > Python: install
install-dependencies:
	pip install -r requirements.txt	
# > update requirements file
update-dependencies:
	pip freeze > requirements.txt

# > Docker: build image

# > Docker-compose build container

# RUN CONFIGS

# > run with uvicorn 
run-server-dev:
	uvicorn app.main:app --reload

# > run with Docker in dev mode