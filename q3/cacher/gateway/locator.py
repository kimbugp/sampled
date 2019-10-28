from math import cos, asin, sqrt


class Locator:
    def locate(self, ip):
        # TODO: find the location of the node
        return (32.1, 0.5)

    def closest(self, node, nodes):
        """Gets location of the closest node to ip using Haversine method"""
        def distance(node1, node2):
            r = 12742
            p = 0.017453292519943295
            d = 0.5 - cos((node2.lat-node1.lat)*p)/2 + cos(node1.lat*p) * \
                cos(node2.lat*p) * (1-cos((node2.log-node1.lat)*p)) / 2
            return r * asin(sqrt(d))
        return min(nodes, key=lambda test_node: distance(node, test_node))
