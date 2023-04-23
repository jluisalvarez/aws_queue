import boto3

def subscribe(topic, protocol, endpoint):
    """
    Subscribes an endpoint to the topic. Some endpoint types, such as email,
    must be confirmed before their subscriptions are active. When a subscription
    is not confirmed, its Amazon Resource Number (ARN) is set to
    'PendingConfirmation'.

    :param topic: The topic to subscribe to.
    :param protocol: The protocol of the endpoint, such as 'sms' or 'email'.
    :param endpoint: The endpoint that receives messages, such as a phone number
                      or an email address.
    :return: The newly added subscription.
    """
    subscription = topic.subscribe(Protocol=protocol, Endpoint=endpoint, ReturnSubscriptionArn=True)
    return subscription

sns = boto3.resource("sns")
topic = sns.Topic(arn='arn:aws:sns:us-east-1:875405486540:temperatura')
email = 'jolualma@gmail.com'
email_sub = subscribe(topic, "email", email)

# Emails need to be manually confirmed first
print(email_sub.attributes["PendingConfirmation"])
