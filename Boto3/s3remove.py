import boto3

s3_resource = boto3.resource('s3')
my_bucket = s3_resource.Bucket("my_bucket_name")

response = my_bucket.delete_objects(
    Delete={
        'Objects': [
            {
                'Key': "AWS_Lamda API gateway_.pdf"   # the name of your file
            }
        ]
    }
)
