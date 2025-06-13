import boto3

# Connect to AWS
s3 = boto3.client('s3', aws_access_key_id='YOUR_ACCESS_KEY', aws_secret_access_key='YOUR_SECRET_KEY')

# Upload file to S3
filename = 'demo_file.txt'
bucket_name = 'your-bucket-name'

with open(filename, 'rb') as file_data:
    s3.upload_fileobj(file_data, bucket_name, filename)

print("File uploaded to S3!")
