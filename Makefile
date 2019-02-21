CONTAINER_NAMESPACE=docker-hosts

build-dev-image:
	docker build --rm \
		-t $(CONTAINER_NAMESPACE):dev-base \
		-f .docker/dev.Dockerfile . 

build-pyinstaller:
	docker build --rm \
		-t $(CONTAINER_NAMESPACE):pyinstaller \
		-f .docker/pyinstaller.debian.dockerfile . 

local-dev:
	docker run --rm \
		-ti \
		-v /etc/hosts:/etc/hosts \
		-v /var/run/docker.sock:/var/run/docker.sock \
		-v `pwd`/src/cli:/usr/local/lib/python3.7/site-packages/cli \
		$(CONTAINER_NAMESPACE):dev-base \
		bash

test:
	-docker rm -f docker-hosts-test-container
	-docker run -d \
		--name docker-hosts-test-container \
		hashicorp/http-echo \
		-text="9x3s8ff"
	
	docker run --rm \
		-ti \
		-v /etc/hosts:/etc/hosts \
		-v /var/run/docker.sock:/var/run/docker.sock \
		-v `pwd`/src/cli:/usr/local/lib/python3.7/site-packages/cli \
		$(CONTAINER_NAMESPACE):dev-base \
		bash -c 'docker-local-hosts map -c docker-hosts-test-container -l docker-hosts-test-container'
	
	curl http://docker-hosts-test-container.local:5678

	-docker rm -f docker-hosts-test-container	

compile-binary:
	docker run --rm \
		-t \
		-v `pwd`/src:/src \
		-w /src \
		$(CONTAINER_NAMESPACE):pyinstaller \
		sh .buildtools/build_exe.sh

local-test:
	-docker rm -f docker-hosts-test-container
	-docker run -d \
		--name docker-hosts-test-container \
		hashicorp/http-echo \
		-text="9x3s8ff"
	
	sudo src/.dist/docker-local-hosts map -c docker-hosts-test-container -l docker-hosts-test-container
	
	curl http://docker-hosts-test-container.local:5678

	-docker rm -f docker-hosts-test-container	
