import boto3
import json


def receive_message():
    sqs_client = boto3.client("sqs", region_name="us-east-1")
    response = sqs_client.receive_message(
        QueueUrl="https://sqs.us-east-1.amazonaws.com/875405486540/queue2023",
        MaxNumberOfMessages=1,
        WaitTimeSeconds=10,
    )
    

    print(response)
    print(f"Number of messages received: {len(response.get('Messages', []))}")

    for message in response.get("Messages", []):
        message_body = message["Body"]
        print(f"Message body: {json.loads(message_body)}")
        print(f"Receipt Handle: {message['ReceiptHandle']}")
        receipt_handle=message['ReceiptHandle']

        response = sqs_client.delete_message(
          QueueUrl="https://sqs.us-east-1.amazonaws.com/875405486540/queue2023",
          ReceiptHandle=receipt_handle,
        )
        print(response)


print("Reciviendo mensaje...")
receive_message()
