from flask import Flask
import os
from flask_bootstrap import Bootstrap4
from config import config

bootstrap = Bootstrap4()

def create_app() -> Flask:
    environment = os.getenv('APP_ENV', 'test')

    print(environment, '✅')

    app = Flask(__name__)

    app.config.from_object(config[environment])
    config[environment].init_app(app)

    from .controllers import viewsBP as viewAPI

    app.register_blueprint(viewAPI)
    bootstrap.init_app(app)
    

    return app
