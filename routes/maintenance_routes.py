from flask import Blueprint, request, jsonify
from models.maintenance import Maintenance
from models.aircraft import Aircraft
from models import db
from services.predictive_maintenance import predict_maintenance
from utils.authentication import token_required
from utils.logging import log_request
from utils.error_handling import handle_error

maintenance_bp = Blueprint('maintenance', __name__)

@maintenance_bp.route('/predict_maintenance/<int:aircraft_id>', methods=['GET'])
@token_required
@log_request
@handle_error
def predict_maintenance_route(current_user, aircraft_id):
    # Route to predict maintenance date for a given aircraft
    prediction = predict_maintenance(aircraft_id)
    if prediction:
        return jsonify({'predicted_maintenance_date': str(prediction)}), 200
    return jsonify({'message': 'No maintenance records found'}), 404
