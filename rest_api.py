#!/usr/bin/env python3
"""
Simple REST API program to display "Hello World!"
"""

from flask import Flask, jsonify

# Create a Flask application instance
app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    """Return a simple greeting"""

    return jsonify({
        "message": "Hello World!",
        "status": "success"
    })


@app.route('/hello', methods=['GET'])
def hello_endpoint():
    """Alternative hello endpoint"""
    return jsonify({
        "greeting": "Hello World!",
        "method": "GET"
    })


@app.route('/api/greet/<name>', methods=['GET'])
def greet_person(name):
    """Greet a specific person"""
    return jsonify({
        "message": f"Hello {name}!",
        "status": "success"
    })


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "message": "API is running"
    })


if __name__ == '__main__':
    print("Starting REST API Server...")
    print("Visit http://localhost:5002 to see 'Hello World!'")
    app.run(debug=True, host='0.0.0.0', port=5002)

