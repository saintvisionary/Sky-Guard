import logging
from flask import request
from config import Config

# Configure logging
logging.basicConfig(level=Config.LOGGING_LEVEL)
logger = logging.getLogger(__name__)

def log_request(f):
    # Decorator to log the details of the request
    def wrapper(*args, **kwargs):
        logger.info(f"Request to {request.path} with args {request.args} and kwargs {kwargs}")
        return f(*args, **kwargs)
    return wrapper
