from flask import Flask, request, send_file
import boto3
from botocore.exceptions import NoCredentialsError
import os

app = Flask(__name__)

# Configuration AWS
s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('AWS_REGION')
)

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    bucket_name = 'tp5bucket'
    try:
        s3.download_file(bucket_name, filename, filename)
        return send_file(filename, as_attachment=True)
    except NoCredentialsError:
        return "Credentials not available", 403
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)

