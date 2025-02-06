# app/resources/appointments.py
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from ..models import Appointment, Patient, Doctor
from .. import db
from datetime import datetime

# Define the Blueprint
appointments_bp = Blueprint('appointments', __name__)
api = Api(appointments_bp)

# Define the AppointmentResource class
class AppointmentResource(Resource):
    def get(self, appointment_id):
        appointment = Appointment.query.get_or_404(appointment_id)
        return jsonify({
            "id": appointment.id,
            "patient_id": appointment.patient_id,
            "doctor_id": appointment.doctor_id,
            "date": appointment.date.isoformat()
        })

    def put(self, appointment_id):
        appointment = Appointment.query.get_or_404(appointment_id)
        data = request.get_json()
        appointment.patient_id = data.get('patient_id', appointment.patient_id)
        appointment.doctor_id = data.get('doctor_id', appointment.doctor_id)
        appointment.date = datetime.fromisoformat(data.get('date', appointment.date.isoformat()))
        db.session.commit()
        return jsonify({"message": "Appointment updated successfully"})

    def delete(self, appointment_id):
        appointment = Appointment.query.get_or_404(appointment_id)
        db.session.delete(appointment)
        db.session.commit()
        return jsonify({"message": "Appointment deleted successfully"})

# Define the AppointmentListResource class
class AppointmentListResource(Resource):
    def get(self):
        appointments = Appointment.query.all()
        return jsonify([{
            "id": appointment.id,
            "patient_id": appointment.patient_id,
            "doctor_id": appointment.doctor_id,
            "date": appointment.date.isoformat()
        } for appointment in appointments])

    def post(self):
        data = request.get_json()
        new_appointment = Appointment(
            patient_id=data['patient_id'],
            doctor_id=data['doctor_id'],
            date=datetime.fromisoformat(data['date'])
        )
        db.session.add(new_appointment)
        db.session.commit()
        return jsonify({"message": "Appointment created successfully", "id": new_appointment.id}), 201

# Add resources to the API
api.add_resource(AppointmentListResource, '/appointments')
api.add_resource(AppointmentResource, '/appointments/<int:appointment_id>')

# Export the Blueprint
__all__ = ['appointments_bp']
