
from flask import request, jsonify
from flask_restful import Resource
from ..models import Patient
from .. import db

class PatientResource(Resource):
    def get(self, patient_id):
        patient = Patient.query.get_or_404(patient_id)
        return jsonify({
            "id": patient.id,
            "name": patient.name,
            "age": patient.age,
            "condition": patient.condition
        })

    def put(self, patient_id):
        patient = Patient.query.get_or_404(patient_id)
        data = request.get_json()
        patient.name = data.get('name', patient.name)
        patient.age = data.get('age', patient.age)
        patient.condition = data.get('condition', patient.condition)
        db.session.commit()
        return jsonify({"message": "Patient updated successfully"})

    def delete(self, patient_id):
        patient = Patient.query.get_or_404(patient_id)
        db.session.delete(patient)
        db.session.commit()
        return jsonify({"message": "Patient deleted successfully"})

class PatientListResource(Resource):
    def get(self):
        patients = Patient.query.all()
        return jsonify([{
            "id": patient.id,
            "name": patient.name,
            "age": patient.age,
            "condition": patient.condition
        } for patient in patients])

    def post(self):
        data = request.get_json()
        new_patient = Patient(
            name=data['name'],
            age=data['age'],
            condition=data.get('condition', '')
        )
        db.session.add(new_patient)
        db.session.commit()
        return jsonify({"message": "Patient created successfully", "id": new_patient.id}), 201
