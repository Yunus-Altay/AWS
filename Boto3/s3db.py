import boto3

# client=boto3.client("s3")
# bucket_name="my_bucket_name"
# response = client.delete_bucket(Bucket=bucket_name)

s3 = boto3.resource('s3')
bucket = s3.Bucket('my_bucket_name')
bucket.delete()

# s3 = boto3.resource('s3')

# Print out all bucket names
for bucket in s3.buckets.all():
    print(bucket.name)