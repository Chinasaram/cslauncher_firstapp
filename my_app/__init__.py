import os
from flask import Flask
from . import db

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)     # create and configure the app
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'my_app.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)      # load the instance config, if it exists, when not testing
    else:
        app.config.from_mapping(test_config)    # load the test config if passed in

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def hello():
        return "Hello World!"

    db.init_app(app)

    return app
