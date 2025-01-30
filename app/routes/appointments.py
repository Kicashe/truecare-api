from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from ..models import Appointment, db
from datetime import datetime

appointments_bp = Blueprint('appointments', __name__)

@appointments_bp.route('/appointments', methods=['POST'])
@jwt_required()
def schedule_appointment():
    data = request.json
    new_appointment = Appointment(
        patient_id=data['patient_id'],
        date=datetime.strptime(data['date'], '%Y-%m-%d %H:%M:%S'),
        description=data['description']
    )
    db.session.add(new_appointment)
    db.session.commit()
    return jsonify({"message": "Appointment scheduled successfully"}), 201

@appointments_bp.route('/appointments/<int:appointment_id>', methods=['GET'])
@jwt_required()
def get_appointment(appointment_id):
    appointment = Appointment.query.get_or_404(appointment_id)
    return jsonify({
        "id": appointment.id,
        "patient_id": appointment.patient_id,
        "date": appointment.date,
        "description": appointment.description
    })
