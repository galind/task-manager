from flask import Flask

from config import Config
from app.extensions import db


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    with app.app_context():
        db.init_app(app)

        db.create_all()

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app
