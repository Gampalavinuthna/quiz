from flask import Flask, render_template, request, jsonify
import json
from pymongo import MongoClient

app = Flask(_name_)

# MongoDB Atlas setup
client = MongoClient("mongodb+srv://vinuthnagampala:Vinuthna07072005@cluster0.024tdsc.mongodb.net/quizdb?retryWrites=true&w=majority&appName=Cluster0")
db = client['quizdb']
results = db['results']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/questions')
def get_questions():
    with open('questions.json') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data.get('name')
    score = data.get('score')
    results.insert_one({'name': name, 'score': score})
    return jsonify({'message': 'Score saved successfully!'})

@app.route('/leaderboard')
def leaderboard():
    top_scores = list(results.find().sort('score', -1).limit(10))
    for s in top_scores:
        s['_id'] = str(s['_id'])  # Remove ObjectId for JSON
    return jsonify(top_scores)

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=3000)
