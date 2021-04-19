from flask import Flask
import config
from application import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=str(config.Config.FLASK_DEBUG))