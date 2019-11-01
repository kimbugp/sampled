from node.server import create_app
import os

config = {
    "duration": os.environ.get('duration', 30),
    "max_size": os.environ.get('max_size', 30),
    "can_expire": os.environ.get('can_expire', True)
}

app = create_app(config)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
