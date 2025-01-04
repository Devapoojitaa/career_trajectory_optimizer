from flask import Flask, request, jsonify, render_template
import pandas as pd
import os

app = Flask(__name__)

# Load CSV data
data = pd.read_csv(os.path.join(os.path.dirname(__file__), 'roles_skills.csv'))

# Home route
@app.route('/')
def home():
    return "Career Trajectory Optimizer API is running!"

# Recommendation endpoint
@app.route('/recommend', methods=['POST'])
def recommend():
    user_skills = request.json.get('skills', [])
    matching_roles = data[data['Top Skills'].str.contains('|'.join(user_skills), na=False, case=False)]
    return jsonify(matching_roles.to_dict(orient='records'))

# Serve frontend
@app.route('/ui')
def ui():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
