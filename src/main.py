
from functions.postgres import *
from functions.weather import *
import sqlalchemy


def main(request):

    var = os.getenv('TEST_VAR')

    print(var)
    return

# df = import_weather()

# db = connect_tcp_socket()


# stmt = sqlalchemy.text(
#     "INSERT INTO open_weather_api (lon,lat,desc_short,desc_long,temp,feels_like,temp_min,temp_max,pressure,humidity,visibility,wind_speed,wind_deg,clouds,dt,sunrise,sunset,timezone,city)"
#     "VALUES(:lon,:lat,:desc_short,:desc_long,:temp,:feels_like,:temp_min,:temp_max,:pressure,:humidity,:visibility,:wind_speed,:wind_deg,:clouds,:dt,:sunrise,:sunset,:timezone,:city)")


# with db.connect() as conn:
#     conn.execute(stmt,
#                  lon=df['lon'],
#                  lat=df['lat'],
#                  desc_short=df['desc_short'],
#                  desc_long=df['desc_long'],
#                  temp=df['temp'],
#                  feels_like=df['feels_like'],
#                  temp_min=df['temp_min'],
#                  temp_max=df['temp_max'],
#                  pressure=df['pressure'],
#                  humidity=df['humidity'],
#                  visibility=df['visibility'],
#                  wind_speed=df['wind_speed'],
#                  wind_deg=df['wind_deg'],
#                  clouds=df['clouds'],
#                  dt=df['dt'],
#                  sunrise=df['sunrise'],
#                  sunset=df['sunset'],
#                  timezone=df['timezone'],
#                  city=df['city']
#                  )
