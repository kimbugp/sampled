import json
from collections import namedtuple
from random import randint
from threading import Thread
from typing import List

import requests

from .locator import Locator

ip_loc = namedtuple("Node", "ip lat log")


class Client():
    nodes: List[ip_loc] = []

    def __init__(self, nodes: List):
        self.locator = Locator()
        [self._attach_node(node) for node in nodes]

    def set(self, key, value, ip=None):
        node = self._node_location(ip)
        response = requests.post(
            f'http://{node.ip}/set',
            data=json.dumps({"key": key, "value": value}),
            headers={'Content-Type': 'application/json', })
        self.replicate(key, value)
        return response.json()

    def get(self, key, ip=None):
        response = requests.get(
            f'http://{self._node_location(ip).ip}/get/{key}')
        return response.json()

    def delete(self, key, ip=None):
        node = self._node_location(ip)
        response = requests.delete(f'http://{node.ip}/delete/{key}')
        return response.json()

    def _node_location(self, ip):
        if not ip:
            return self.nodes[0]
        lat, log = self.locator.locate(ip)
        location = ip_loc(ip, lat, log)
        return self.locator.closest(location, self.nodes)

    def _attach_node(self, node):
        self.nodes.append(ip_loc(node, *self.locator.locate(node)))

    def _detach_node(self, node):
        self.nodes.remove(node)

    def replicate(self, key, value):
        for item in self.nodes:
            response = requests.post(
                f'http://{item.ip}/set',
                data=json.dumps({"key": key, "value": value}),
                headers={'Content-Type': 'application/json', })

    def __getitem__(self, key): return self.get(key)

    def __setitem__(self, key, value): return self.set(key, value)
