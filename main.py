from flask import Flask, render_template, jsonify
import subprocess
import pymongo
import datetime
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-script')
def run_script():
    # Run the script
    subprocess.call(["python", "app.py"])
    
    # Connect to MongoDB and retrieve the latest record
    client = pymongo.MongoClient("mongodb+srv://daberaoakshay1:6ufKPdL0R1iXg9dv@cluster0.7lpipcb.mongodb.net/")
    db = client.trending_data
    collection = db.trending_topics
    # latest_record = collection.find().sort([('_id', pymongo.DESCENDING)]).limit(1)[0]
    # print(latest_record)
    latest_record = collection.find_one(sort=[('date_and_time', pymongo.DESCENDING)])
    # print(latest_record)
    
    # Convert the record to a JSON string with indentation for readability
    json_data = json.dumps([latest_record], indent=4, default=str)
    
    return render_template('results.html', record=latest_record)

@app.route('/api/data')
def api_data():
    # Connect to MongoDB and retrieve the latest record
    client = pymongo.MongoClient("mongodb+srv://daberaoakshay1:6ufKPdL0R1iXg9dv@cluster0.7lpipcb.mongodb.net/")
    db = client.trending_data
    collection = db.trending_topics
    # latest_record = collection.find().sort([('_id', pymongo.DESCENDING)]).limit(1)[0]
    
    latest_record = collection.find_one(sort=[('date_and_time', pymongo.DESCENDING)])
    
    return jsonify(latest_record)

if __name__ == '__main__':
    app.run(debug=True)
