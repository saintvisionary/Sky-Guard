from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Aircraft(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tail_number = db.Column(db.String(10), unique=True, nullable=False)
    model = db.Column(db.String(50), nullable=False)
    manufacturer = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    maintenance_records = db.relationship('Maintenance', backref='aircraft', lazy=True)
    fleet_id = db.Column(db.Integer, db.ForeignKey('fleet.id'), nullable=True)

class Maintenance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aircraft_id = db.Column(db.Integer, db.ForeignKey('aircraft.id'), nullable=False)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    details = db.Column(db.Text, nullable=False)
    predicted_failure_date = db.Column(db.Date, nullable=True)

class Fleet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    aircrafts = db.relationship('Aircraft', backref='fleet', lazy=True)
