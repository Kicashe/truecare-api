# app/resources/auth.py
from flask import Blueprint, request, jsonify
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from ..models import Patient, Doctor
from .. import db

# Define the Blueprint
auth_bp = Blueprint('auth', __name__)

# Define the AuthResource class
class AuthResource(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        # Check if the user is a patient
        patient = Patient.query.filter_by(name=username).first()
        if patient and patient.password == password:
            access_token = create_access_token(identity=patient.id)
            return jsonify(access_token=access_token)

        # Check if the user is a doctor
        doctor = Doctor.query.filter_by(name=username).first()
        if doctor and doctor.password == password:
            access_token = create_access_token(identity=doctor.id)
            return jsonify(access_token=access_token)

        return jsonify({"message": "Invalid credentials"}), 401

# Export the Blueprint
__all__ = ['auth_bp']
