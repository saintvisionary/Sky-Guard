from flask import jsonify
import traceback

def handle_error(f):
    # Decorator to handle errors and provide a JSON response
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            traceback.print_exc()
            return jsonify({'message': 'An error occurred', 'error': str(e)}), 500
    return wrapper
