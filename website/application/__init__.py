from flask import Flask

def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    
    with app.app_context():
        # Imports
        from .views import view
        from .database import DataBase

        # Register Routes
        app.register_blueprint(view, url_prefix="/")


        return app