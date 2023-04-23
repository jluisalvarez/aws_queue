import boto3


def list_topics():
    """
    Lists topics for the current account.

    :return: An iterator that yields the topics.
    """
    sns = boto3.resource("sns")
    topics_iter = sns.topics.all()
    return topics_iter

topics = list_topics()
for topic in topics:
  print(topic)



