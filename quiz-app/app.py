from flask import Flask, request, jsonify, render_template

import boto3

import json

from pymongo import MongoClient

from flask_cors import CORS



app = Flask(_name_)

CORS(app)



# Connect to MongoDB Atlas

client = MongoClient("your-mongodb-connection-string")

db = client["quizdb"]

results_collection = db["results"]



# S3

s3 = boto3.client('s3',

    aws_access_key_id="YOUR_AWS_ACCESS_KEY",

    aws_secret_access_key="YOUR_SECRET_KEY"

)

bucket_name = "your-s3-bucket-name"



@app.route('/')

def home():

    return render_template("index.html")



@app.route('/questions', methods=['GET'])

def get_questions():

    obj = s3.get_object(Bucket=bucket_name, Key='questions.json')

    questions = json.loads(obj['Body'].read())

    return jsonify(questions)



@app.route('/submit', methods=['POST'])

def submit_answers():

    data = request.json

    results_collection.insert_one(data)

    return jsonify({"message": "Results saved!"})



if _name_ == '_main_':

    app.run(host='0.0.0.0', port=80)

from flask import Flask, request, jsonify, render_template
import boto3
import json
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(_name_)
CORS(app)

# Connect to MongoDB Atlas
client = MongoClient("your-mongodb-connection-string")
db = client["quizdb"]
results_collection = db["results"]

# S3
s3 = boto3.client('s3',
    aws_access_key_id="YOUR_AWS_ACCESS_KEY",
    aws_secret_access_key="YOUR_SECRET_KEY"
)
bucket_name = "your-s3-bucket-name"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/questions', methods=['GET'])
def get_questions():
    obj = s3.get_object(Bucket=bucket_name, Key='questions.json')
    questions = json.loads(obj['Body'].read())
    return jsonify(questions)

@app.route('/submit', methods=['POST'])
def submit_answers():
    data = request.json
    results_collection.insert_one(data)
    return jsonify({"message": "Results saved!"})

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=80)