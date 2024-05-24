from flask import Blueprint, jsonify
from utils.authentication import token_required
from utils.logging import log_request
from utils.error_handling import handle_error
from services.data_visualization import generate_maintenance_chart
from models.maintenance import Maintenance
from datetime import datetime

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/maintenance_chart', methods=['GET'])
@token_required
@log_request
@handle_error
def maintenance_chart(current_user):
    # Generate maintenance chart data
    records = Maintenance.query.all()
    data = {
        'date': [record.date for record in records],
        'maintenance_cost': [len(record.details) for record in records]  # Dummy maintenance cost based on details length
    }
    chart = generate_maintenance_chart(data)
    return jsonify({'chart': chart}), 200
