IMAGE_NAME=fin_data_project_001
CONTAINER_NAME=fin_data_project_001_container

.PHONY: build run shell stop logs

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run --rm -it --name $(CONTAINER_NAME) -v $(PWD):/app $(IMAGE_NAME)

build-run: build run

shell:
	docker run --rm -it --name $(CONTAINER_NAME) -v $(PWD):/app $(IMAGE_NAME) /bin/bash

stop:
	-docker stop $(CONTAINER_NAME)

logs:
	docker logs $(CONTAINER_NAME)