import boto3


def publish_text_message(phone_number, message):
    """
    Publishes a text message directly to a phone number without need for a
    subscription.

    :param phone_number: The phone number that receives the message.
    :param message: The message to send.
    :return: The ID of the message.
    """
    sns = boto3.resource("sns")
    response = sns.meta.client.publish(
        PhoneNumber=phone_number, Message=message)
    message_id = response['MessageId']
    return message_id


publish_text_message("+34649856166", "Testing sms 1234")
