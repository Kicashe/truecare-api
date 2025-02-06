# app/__init__.py
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
    print("Patients Blueprint:", patients_bp)  # Debugging line

    from .resources.doctors import doctors_bp
    print("Doctors Blueprint:", doctors_bp)  # Debugging line

    from .resources.appointments import appointments_bp
    print("Appointments Blueprint:", appointments_bp)  # Debugging line

    from .resources.auth import auth_bp
    print("Auth Blueprint:", auth_bp)  # Debugging line

    app.register_blueprint(patients_bp)
    app.register_blueprint(doctors_bp)
    app.register_blueprint(appointments_bp)
    app.register_blueprint(auth_bp)

    return app
