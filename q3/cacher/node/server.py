from flask import Flask, request, Response
from .lrucache import LRUCache
import json


def create_app(config):

    app = Flask(__name__)
    client = LRUCache(**config)

    @app.route('/set', methods=['POST'])
    def set_data():
        data = request.json
        key = data['key']
        value = data['value']
        client.set(key, value)
        return Response(json.dumps({'value': value}))

    @app.route('/get/<string:key>', methods=['GET'])
    def get_key(key):
        try:
            value = client.get(key)
            return Response(json.dumps({'value': value}))
        except KeyError as error:
            return Response(json.dumps({'error': str(error)}))

    @app.route('/delete/<string:key>', methods=['DELETE'])
    def delete_key(key):
        try:
            value = client.delete(key)
            return Response(None)
        except KeyError as error:
            return Response(json.dumps({'error': str(error)}))
    return app
