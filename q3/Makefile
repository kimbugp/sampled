IMAGE := node_image
PREFIX := 172.10.0.0/16
.PHONY: test
test:
	python3 -m pytest

clean:
	rm -rf *.pyc */*.pyc */*/*.pyc

NODE :=`docker run --net node_network -d ${IMAGE}`
start:
	NODES=$$NODES
	docker network create --subnet=${PREFIX} node_network||true
	number=1
	while [[ $$number -le $$NODES ]] ; do \
        ((number = number + 1)) ; \
		echo "${NODE}";\
		docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' ${NODE};\
    done

build:
	docker build -t ${IMAGE} .

IMAGES := `docker ps -q`

kill:
	echo "${IMAGES}";\
	docker kill ${IMAGES}