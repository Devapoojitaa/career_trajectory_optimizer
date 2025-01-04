from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# Load the static dataset
data = pd.DataFrame({
    "Role": ["Data Scientist", "AI Engineer", "Product Manager"],
    "Top Skills": ["Python, Machine Learning", "Python, TensorFlow", "Leadership, Communication"],
    "Learning Resources": [
        "https://example.com/ds", 
        "https://example.com/ai", 
        "https://example.com/pm"
    ]
})

# Home route
@app.route('/')
def home():
    return "Career Trajectory Optimizer API is running!"

# Recommendation endpoint
@app.route('/recommend', methods=['POST'])
def recommend():
    user_skills = request.json.get('skills', [])
    matching_roles = data[data['Top Skills'].str.contains('|'.join(user_skills), na=False)]
    return matching_roles.to_dict(orient='records')

# Serve frontend
@app.route('/ui')
def ui():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
