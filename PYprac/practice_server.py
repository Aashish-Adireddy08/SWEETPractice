print("Hello World!")


""" 
from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# 1. Simple text route (Home page)
@app.route('/')
def home():
    return "<h1>Hello, World!</h1><p>Welcome to your Flask web server.</p>"

# 2. Dynamic route that reads a variable from the URL path
@app.route('/user/<username>')
def show_user_profile(username):
    return f"User page for: <b>{username}</b>"

# 3. API route that returns JSON data
@app.route('/api/data', methods=['GET'])
def get_data():
    sample_data = {
        "status": "success",
        "message": "Data retrieved perfectly!",
        "items": [1, 2, 3, 4, 5]
    }
    return jsonify(sample_data)

# Run the local development server when this script is executed directly
if __name__ == '__main__':
    # debug=True allows automatic reloading when you make changes to the code
    app.run(debug=True, host='127.0.0.1', port=5000)
"""
