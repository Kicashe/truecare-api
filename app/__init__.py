from 
import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///truecare.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'truecare-secret-key'  # Change this in production

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)

    # Register blueprints
    from .routes.auth import auth_bp
    from .routes.patients import patients_bp
    from .routes.appointments import appointments_bp
    from .routes.medical_history import medical_history_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(patients_bp)
    app.register_blueprint(appointments_bp)
    app.register_blueprint(medical_history_bp)

    # Create database tables
    with app.app_context():
        db.create_all()

    return app