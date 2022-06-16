PACKAGE_NAME=api
HOST_PORT=8000
PROJECT_FOLDER=.
GIT_DIR=$(shell pwd)

clean-pyc:
	rm -Rf tests/__pycache__
	find . -name '*.pyc' -delete
	find . -name '*.pyo' -delete
	find . -name '*~' -delete

clean-build:
	rm -Rf build/
	rm -Rf dist/
	rm -Rf *.egg-info
	rm -Rf .cache/

clean: clean-pyc clean-build

launch:
	FLASK_APP=server.py FLASK_DEBUG=1 python -m flask run --host=0.0.0.0 --port=8000

build: clean
	docker build -t $(PACKAGE_NAME) -f Dockerfile --build-arg module_folder=$(PROJECT_FOLDER) --build-arg package_name=$(PACKAGE_NAME) $(GIT_DIR)

shell: clean
	docker run -it --rm \
	-v $(GIT_DIR):/app \
	-p $(HOST_PORT):8000 \
	-w /app/$(PROJECT_FOLDER) \
	--entrypoint=/bin/ash $(PACKAGE_NAME)

