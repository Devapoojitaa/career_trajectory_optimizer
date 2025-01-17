from flask import Flask, request, jsonify, render_template
import pandas as pd
import os

app = Flask(__name__)

# Load the CSV file
data = pd.read_csv(os.path.join(os.path.dirname(__file__), 'roles_skills.csv'))

# Home route
@app.route('/')
def home():
    return "Career Trajectory Optimizer API is running!"

# Serve the frontend
@app.route('/ui')
def ui():
    return render_template('index.html')

# Recommendation endpoint
@app.route('/recommend', methods=['POST', 'GET'])
def recommend():
    if request.method == 'POST':
        user_skills = request.json.get('skills', [])
        matching_roles = data[data['Top Skills'].str.contains('|'.join(user_skills), na=False, case=False)]
        return jsonify(matching_roles.to_dict(orient='records'))
    return "Use POST with JSON data to get recommendations."

if __name__ == '__main__':
    app.run(debug=True)
