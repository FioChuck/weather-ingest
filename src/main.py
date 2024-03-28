
from functions.postgres import *
from functions.weather import *
from functions.pubsub import *


from dotenv import load_dotenv
load_dotenv()


def main(request):

    df = import_weather()

    # postgres_insert(df)

    publish(df)

    return 'finish'


# main('none')
