from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from ..models import Patient, db

patients_bp = Blueprint('patients', __name__)

@patients_bp.route('/patients', methods=['POST'])
@jwt_required()
def add_patient():
    data = request.json
    new_patient = Patient(
        name=data['name'],
        age=data['age'],
        gender=data['gender'],
        contact=data['contact']
    )
    db.session.add(new_patient)
    db.session.commit()
    return jsonify({"message": "Patient added successfully"}), 201

@patients_bp.route('/patients/<int:patient_id>', methods=['GET'])
@jwt_required()
def get_patient(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    return jsonify({
        "id": patient.id,
        "name": patient.name,
        "age": patient.age,
        "gender": patient.gender,
        "contact": patient.contact
    })
