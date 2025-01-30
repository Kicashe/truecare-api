from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from ..models import MedicalHistory, db

medical_history_bp = Blueprint('medical_history', __name__)

@medical_history_bp.route('/medical-history', methods=['POST'])
@jwt_required()
def add_medical_history():
    data = request.json
    new_record = MedicalHistory(
        patient_id=data['patient_id'],
        diagnosis=data['diagnosis'],
        treatment=data['treatment']
    )
    db.session.add(new_record)
    db.session.commit()
    return jsonify({"message": "Medical history added successfully"}), 201

@medical_history_bp.route('/medical-history/<int:patient_id>', methods=['GET'])
@jwt_required()
def get_medical_history(patient_id):
    records = MedicalHistory.query.filter_by(patient_id=patient_id).all()
    return jsonify([{
        "id": record.id,
        "diagnosis": record.diagnosis,
        "treatment": record.treatment,
        "date": record.date
    } for record in records])
