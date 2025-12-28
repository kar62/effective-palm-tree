# User Management SPA Web Application

A Single Page Application (SPA) built with Python Flask backend and vanilla JavaScript frontend that displays user information.

## Features

- 🌐 RESTful API built with Flask
- 👥 Display user information (first name, last name, address, email)
- 🔄 Simulated user data (ready for future Azure API integration)
- 📱 Responsive design
- 🎨 Modern UI with card and table views
- 🔌 CORS-enabled for cross-origin requests

## Project Structure

```
.
├── app.py                 # Flask backend with REST API
├── requirements.txt       # Python dependencies
├── static/
│   └── index.html        # Frontend SPA
└── APP_README.md         # This file
```

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. **Clone the repository** (if not already done):
   ```bash
   git clone <repository-url>
   cd effective-palm-tree
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the Flask server**:
   ```bash
   python app.py
   ```

2. **Access the application**:
   Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

The server will run on `http://localhost:5000` by default.

## API Endpoints

### Get All Users
- **URL**: `/api/users`
- **Method**: `GET`
- **Success Response**:
  ```json
  {
    "success": true,
    "users": [
      {
        "id": 1,
        "firstName": "John",
        "lastName": "Doe",
        "address": "123 Main St, Seattle, WA 98101",
        "email": "john.doe@example.com"
      },
      ...
    ],
    "count": 6
  }
  ```

### Get Single User
- **URL**: `/api/users/<user_id>`
- **Method**: `GET`
- **Success Response**:
  ```json
  {
    "success": true,
    "user": {
      "id": 1,
      "firstName": "John",
      "lastName": "Doe",
      "address": "123 Main St, Seattle, WA 98101",
      "email": "john.doe@example.com"
    }
  }
  ```
- **Error Response**:
  ```json
  {
    "success": false,
    "message": "User not found"
  }
  ```

## User Data Structure

Each user contains the following information:
- `id`: Unique identifier (integer)
- `firstName`: User's first name (string)
- `lastName`: User's last name (string)
- `address`: User's full address (string)
- `email`: User's email address (string)

## Current Implementation

The application currently uses **simulated data** stored in the backend. The data is hardcoded in `app.py` with 6 sample users.

## Future Integration

The application is designed to be easily integrated with an external REST API (such as Azure-hosted services). To integrate with a real API:

1. Replace the `users` list in `app.py` with API calls to your external service
2. Update the `/api/users` endpoint to fetch data from the external API
3. Add any necessary authentication headers or API keys
4. Handle potential API errors and edge cases

Example modification for Azure API integration:
```python
import requests

@app.route('/api/users', methods=['GET'])
def get_users():
    try:
        # Replace with your Azure API endpoint
        response = requests.get('https://your-azure-api.azurewebsites.net/users')
        data = response.json()
        return jsonify({
            "success": True,
            "users": data,
            "count": len(data)
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500
```

## Development

- The Flask server runs in debug mode for development
- Changes to Python files will automatically reload the server
- Frontend changes require a browser refresh

## Technologies Used

- **Backend**: Python, Flask, Flask-CORS
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **API**: RESTful JSON API

## Browser Support

The application supports all modern browsers:
- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)

## License

MIT License - See LICENSE file for details
