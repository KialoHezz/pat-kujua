from config import config_options
from flask import Flask
from flask_bootstrap import Bootstrap

def create_app(config_name):
    app =  Flask (__name__)
    # create app configuration
    app.config.from_object(config_options[config_name])

    # register the blueprint
    from .main  import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # create the app configurations
  
    bootstrap = Bootstrap(app)

    # setting the configuration
    from .requests import configure_request
    configure_request(app)

    # will add the views

    return app


# from .main import views
# from .main import errors