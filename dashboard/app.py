from flask import Flask, render_template, jsonify
import boto3
import pandas as pd

app = Flask(__name__)

s3 = boto3.client('s3')
bucket_name = 'your-s3-bucket-name'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    response = s3.get_object(Bucket=bucket_name, Key='sentiment_data.csv')
    df = pd.read_csv(response['Body'])
    return jsonify(df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
