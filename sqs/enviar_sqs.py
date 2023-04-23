import boto3
import json

sqs = boto3.client("sqs", region_name="us-east-1")

response = sqs.get_queue_url(QueueName="queue2023",)
QueueUrl = response["QueueUrl"]
print(QueueUrl)

message = {"new": "mensaje desde SQS"}
response = sqs.send_message(
	QueueUrl=QueueUrl,
	MessageBody=json.dumps(message)
)
print(response)
