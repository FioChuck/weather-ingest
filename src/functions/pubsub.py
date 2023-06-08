from google.cloud import pubsub_v1
import json
from datetime import datetime


def publish(data_df):

    publisher = pubsub_v1.PublisherClient()

    GCP_PROJECT_ID = "cf-data-analytics"
    TOPIC_NAME = "weather-data"

    topic_path = publisher.topic_path(GCP_PROJECT_ID, TOPIC_NAME)

    data_df.pop('processing_time')
    data_df.pop('desc_short')
    data_df.pop('desc_long')

    data_df['processing_time'] = str(datetime.now())

    message_json = json.dumps(data_df)
    message_bytes = message_json.encode('utf-8')

    try:
        publish_future = publisher.publish(topic_path, data=message_bytes)
        publish_future.result()
        return 'message published'
    except Exception as e:
        print(e)
        return (e, 500)
