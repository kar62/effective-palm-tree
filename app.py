from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='static')
CORS(app)

# Simulated user data
users = [
    {
        "id": 1,
        "firstName": "John",
        "lastName": "Doe",
        "address": "123 Main St, Seattle, WA 98101",
        "email": "john.doe@example.com"
    },
    {
        "id": 2,
        "firstName": "Jane",
        "lastName": "Smith",
        "address": "456 Oak Ave, Portland, OR 97201",
        "email": "jane.smith@example.com"
    },
    {
        "id": 3,
        "firstName": "Michael",
        "lastName": "Johnson",
        "address": "789 Pine Rd, San Francisco, CA 94102",
        "email": "michael.johnson@example.com"
    },
    {
        "id": 4,
        "firstName": "Emily",
        "lastName": "Williams",
        "address": "321 Elm Blvd, Los Angeles, CA 90001",
        "email": "emily.williams@example.com"
    },
    {
        "id": 5,
        "firstName": "David",
        "lastName": "Brown",
        "address": "654 Maple Dr, Austin, TX 78701",
        "email": "david.brown@example.com"
    },
    {
        "id": 6,
        "firstName": "Sarah",
        "lastName": "Davis",
        "address": "987 Cedar Ln, Boston, MA 02101",
        "email": "sarah.davis@example.com"
    }
]

@app.route('/')
def index():
    """Serve the main SPA page"""
    return send_from_directory('static', 'index.html')

@app.route('/api/users', methods=['GET'])
def get_users():
    """API endpoint to retrieve all users"""
    return jsonify({
        "success": True,
        "users": users,
        "count": len(users)
    })

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """API endpoint to retrieve a specific user by ID"""
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        return jsonify({
            "success": True,
            "user": user
        })
    else:
        return jsonify({
            "success": False,
            "message": "User not found"
        }), 404

if __name__ == '__main__':
    # Create static directory if it doesn't exist
    if not os.path.exists('static'):
        os.makedirs('static')
    
    # Use debug mode only in development (set DEBUG=False for production)
    debug_mode = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)
