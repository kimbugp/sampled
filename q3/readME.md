# Distributed LRU Cache
Distributed Least Recently Used cache


## Build Cache Node Image
To build a single node image

```bash
rake build
```

## Running Tests 
```
make test 
```


## Running Cache Node Containers
Run

```
make start NODES=(number of node you need)
```
Pick up the ip address from the started nodes which are to be latter used in the cache distributor

## Cache Gateway
- Start the nodes gateway client can be integrated into any  work flow by using the module
- It can be started for testing by running 

```
make gateway&&make up
```

```
from cacher.gateway import Client
```
Instantiate the object with the ip addresses of the nodes created in the step above 
Use the docker container name for this. Docker will resolve then using the internal DNS

```
client = Client([ip address list])
```

The client can perform the following operations:

set

```
client.set("name","simon") # or 
client["name"]= "simon"
```

get
```
client.get("name") # OR 
client["name"]
```
delete
```
client.delete("name")
```
## Communication
The nodes and the gateway communicate via HTTP

## TODO
- Add data node auto discovery and configuration update 
- Add node health checks and data redundancy using replicas
