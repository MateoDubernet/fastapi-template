import boto3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configurer le client S3
s3_client = boto3.client('s3')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    bucket_name = 'tp5bucket'
    s3_client.upload_fileobj(file, bucket_name, file.filename)
    return jsonify({'message': 'Fichier téléchargé avec succès !'}), 200

if __name__ == '__main__':
    app.run(debug=True)

