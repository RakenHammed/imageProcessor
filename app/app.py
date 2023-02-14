from flask import Flask

from app.config import config
from app.controllers import image_processor_controller


def create_app(test_config: dict[str, any] = None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)
    if test_config:
        app.config.from_object(config)
    else:
        app.config.from_mapping(test_config)
    app.register_blueprint(image_processor_controller.bp)
    return app
