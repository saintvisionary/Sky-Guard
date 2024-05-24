from flask import Flask
from models import db
from routes.maintenance_routes import maintenance_bp
from routes.user_routes import user_bp
from routes.dashboard_routes import dashboard_bp
from config import Config
from flask_migrate import Migrate
from utils.logging import logger

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database
db.init_app(app)
migrate = Migrate(app, db)

# Register blueprints for different routes
app.register_blueprint(maintenance_bp, url_prefix='/maintenance')
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(dashboard_bp, url_prefix='/dashboard')

@app.route('/')
def index():
    # Home route
    return "Sky Guard Aviation SaaS Platform API"

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
