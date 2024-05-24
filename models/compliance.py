from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class ComplianceRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aircraft_id = db.Column(db.Integer, db.ForeignKey('aircraft.id'), nullable=False)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    details = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), nullable=False)  # e.g., 'Pending', 'Approved', 'Rejected'

class IncidentReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aircraft_id = db.Column(db.Integer, db.ForeignKey('aircraft.id'), nullable=False)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    description = db.Column(db.Text, nullable=False)
    severity = db.Column(db.String(50), nullable=False)  # e.g., 'Low', 'Medium', 'High'
