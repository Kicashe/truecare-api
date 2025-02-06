# app/resources/doctors.py
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from ..models import Doctor
from .. import db

# Define the Blueprint
doctors_bp = Blueprint('doctors', __name__)
api = Api(doctors_bp)

# Define the DoctorResource class
class DoctorResource(Resource):
    def get(self, doctor_id):
        doctor = Doctor.query.get_or_404(doctor_id)
        return jsonify({
            "id": doctor.id,
            "name": doctor.name,
            "specialization": doctor.specialization
        })

    def put(self, doctor_id):
        doctor = Doctor.query.get_or_404(doctor_id)
        data = request.get_json()
        doctor.name = data.get('name', doctor.name)
        doctor.specialization = data.get('specialization', doctor.specialization)
        db.session.commit()
        return jsonify({"message": "Doctor updated successfully"})

    def delete(self, doctor_id):
        doctor = Doctor.query.get_or_404(doctor_id)
        db.session.delete(doctor)
        db.session.commit()
        return jsonify({"message": "Doctor deleted successfully"})

# Define the DoctorListResource class
class DoctorListResource(Resource):
    def get(self):
        doctors = Doctor.query.all()
        return jsonify([{
            "id": doctor.id,
            "name": doctor.name,
            "specialization": doctor.specialization
        } for doctor in doctors])

    def post(self):
        data = request.get_json()
        new_doctor = Doctor(
            name=data['name'],
            specialization=data['specialization']
        )
        db.session.add(new_doctor)
        db.session.commit()
        return jsonify({"message": "Doctor created successfully", "id": new_doctor.id}), 201

# Add resources to the API
api.add_resource(DoctorListResource, '/doctors')
api.add_resource(DoctorResource, '/doctors/<int:doctor_id>')

# Export the Blueprint
__all__ = ['doctors_bp']
