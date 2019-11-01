IMAGE := node_image
PREFIX := 172.10.0.0/16
.PHONY: test
test:
	python3 -m pytest

clean:
	rm -rf *.pyc */*.pyc */*/*.pyc
	
start:
	NODES=$$NODES
	docker network create --subnet=${PREFIX} node_network||true
	number=1
	while [[ $$number -lt $$NODES ]] ; do \
        ((number = number + 1)) ; \
		docker run --net node_network -d ${IMAGE};\
    done

build:
	docker build -t ${IMAGE} .


IMAGES := `docker ps -q`

kill:
	echo "${IMAGES}";\
	docker kill ${IMAGES}

names:
	docker inspect -f "{{range .Containers}}{{.Name}}{{end}}" node_network

gateway:
	docker build -f Dockerfile.gateway -t cache-gateway .

up:
	docker run --net node_network -it cache-gateway;


