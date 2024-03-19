from flask import Flask, jsonify
import os
from pymongo import MongoClient

app = Flask(__name__)

# Fetch MongoDB connection string from environment variables
MONGODB_CONNECTION_STRING = os.getenv("MONGODB_CONNECTION_STRING")

# Check if the connection string is available
if not MONGODB_CONNECTION_STRING:
    raise ValueError("MongoDB connection string not found in environment variables.")

# Function to test connectivity with CosmosDB MongoDB
def test_connectivity():
    try:
        # Connect to MongoDB
        client = MongoClient(MONGODB_CONNECTION_STRING)
        db = client.test_database

        # Test connection by fetching a document from a collection
        document = db.test_collection.find_one()
        return True, document
    except Exception as e:
        return False, str(e)

@app.route("/")
def index():
    """Function to test the functionality of the API"""
    return "Hello, world!"

# Endpoint to test connectivity with CosmosDB MongoDB
@app.route('/test-connectivity')
def test_connectivity_endpoint():
    success, result = test_connectivity()
    if success:
        return jsonify({'success': True, 'message': 'Successfully connected to CosmosDB MongoDB', 'data': result}), 200
    else:
        return jsonify({'success': False, 'error': 'Failed to connect to CosmosDB MongoDB', 'message': result}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)