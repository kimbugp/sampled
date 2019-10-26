from .node_hasher import Hasher
import requests
import json
nodes = ['127.0.0.1:8000', '127.0.0.1:80']


class Client():
    def __init__(self, nodes=nodes):
        self.hasher = Hasher(nodes)

    def set(self, key, value):
        response = requests.post(
            f'{self.node(key)}/set', data=json.dumps({key: value}))
        return response.json()

    def get(self, key):
        response = requests.get(f'{self.node(key)}/get/{key}')
        return response.json()

    def delete(self, key):
        response = requests.delete(f'{self.node(key)}/delete/{key}')
        return response.json()

    def node(self, key):
        return self.hasher.get_node(key)

    def __getitem__(self, key): return self.get(key)

    def __setitem__(self, key, value): return self.set(key, value)
