import boto3


def publish_message(topic, message):
    """
    Publishes a message to a topic.

    :param topic: The topic to publish to.
    :param message: The message to publish.
    :return: The ID of the message.
    """
    response = topic.publish(Message=message)
    message_id = response['MessageId']
    return message_id


sns = boto3.resource("sns")
topic = sns.Topic(arn='arn:aws:sns:us-east-1:875405486540:temperatura')
publish_message(topic, "Probando SNS: Temperatura: 27")

