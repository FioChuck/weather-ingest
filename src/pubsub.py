from google.cloud import pubsub_v1
import json
from datetime import datetime


def publish(df, project, topic):

    data_df = df

    publisher = pubsub_v1.PublisherClient()

    # project = "cf-data-analytics"
    # topic = "weather-data"

    topic_path = publisher.topic_path(project, topic)

    data_df.pop('processing_time')
    # data_df.pop('desc_short')
    # data_df.pop('desc_long')

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


def router(df, destination):
    match destination:
        case "weather-data":
            response = publish(df, "cf-data-analytics", "weather-data")
            return response
        case "weather-data-short":
            df.pop('desc_short')
            df.pop('desc_long')
            response = publish(df, "cf-data-analytics", "weather-data-short")
            return response
