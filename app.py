import os
from flask import Flask

import env


app = Flask(__name__)


@app.route('/')
def index():
    return "Hello world ... again!"


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)