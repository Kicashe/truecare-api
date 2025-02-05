
from flask import request, jsonify
from flask_restful import Resource
from ..models import Doctor
from .. import db

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
