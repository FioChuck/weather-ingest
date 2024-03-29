import os
import psycopg2
from psycopg2 import Error


def postgres_insert(df):

    db_host = os.getenv('DB_HOST')
    db_user = os.getenv('DB_USER')
    db_pass = os.getenv('DB_PASS')
    db_name = "weather"
    db_port = 5432

    try:
        connection = psycopg2.connect(
            user=db_user, password=db_pass, host=db_host, port=db_port, database=db_name)

        cursor = connection.cursor()
        item_tuple = (df['processing_time'], df['lon'], df['lat'], df['sunset'], df['timezone'], df['temp'], df['feels_like'], df['temp_min'], df['temp_max'], df['pressure'],
                      df['humidity'], df['visibility'], df['wind_speed'], df['wind_deg'], df['clouds'], df['dt'], df['sunrise'], df['desc_short'], df['desc_long'], df['city'])

        insert_query = """ INSERT INTO open_weather_api (processing_time, lon, lat, sunset, timezone, temp, feels_like, temp_min, temp_max, pressure, humidity, visibility, wind_speed, wind_deg, clouds, dt, sunrise, desc_short, desc_long, city) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(insert_query, item_tuple)
        connection.commit()

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
