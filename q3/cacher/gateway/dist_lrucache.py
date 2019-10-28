from .locator import Locator
import json
import requests
from random import randint
from collections import namedtuple
from threading import Thread

ip_loc = namedtuple("Node", "ip lat log")
nodes = ['127.0.0.1:3000', '127.0.0.1:8000']


class Client():
    def __init__(self, nodes=nodes):
        self.locator = Locator()
        self.nodes = [ip_loc(node, *self.locator.locate(node))
                      for node in nodes]

    def set(self, key, value, ip=None):
        node = self.node(ip)
        response = requests.post(
            f'http://{node.ip}/set',
            data=json.dumps({"key": key, "value": value}),
            headers={'Content-Type': 'application/json', })
        self.copy(key, value)
        return response.json()

    def get(self, key, ip=None):
        response = requests.get(
            f'http://{self.node(ip).ip}/get/{key}')
        return response.json()

    def delete(self, key, ip=None):
        node = self.node(ip)
        response = requests.delete(f'http://{node.ip}/delete/{key}')
        return response.json()

    def node(self, ip):
        if not ip:
            return self.nodes[0]
        lat, log = self.locator.locate(ip)
        location = ip_loc(ip, lat, log)
        return self.locator.closest(location, self.nodes)

    def copy(self, key, value):
        for node in self.nodes:
            response = requests.post(
                f'http://{node.ip}/set',
                data=json.dumps({"key": key, "value": value}),
                headers={'Content-Type': 'application/json', })

    def __getitem__(self, key): return self.get(key)

    def __setitem__(self, key, value): return self.set(key, value)
