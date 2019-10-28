IMAGE := node_image
PREFIX := 172.10.0.
.PHONY: test
test:
	python3 -m pytest

clean:
	rm -rf *.pyc */*.pyc */*/*.pyc

start:
	NODES=$$NODES
	docker network create --subnet=172.10.0.0/16 node_network||true
	number=1
	while [[ $$number -le $$NODES ]] ; do \
        ((number = number + 1)) ; \
		echo $(PREFIX)$$number ; \
		docker run --net node_network -d --ip $(PREFIX)$$number $(IMAGE);\
    done

build:
	docker build -t $(IMAGE) .