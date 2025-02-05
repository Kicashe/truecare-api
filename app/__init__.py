
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)

    # Register blueprints or resources
    from .resources.patients import patients_bp
    from .resources.doctors import doctors_bp
    from .resources.appointments import appointments_bp
    from .resources.auth import auth_bp

    app.register_blueprint(patients_bp)
    app.register_blueprint(doctors_bp)
    app.register_blueprint(appointments_bp)
    app.register_blueprint(auth_bp)

    return app
