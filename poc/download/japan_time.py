# Set the timezone to Japan
from datetime import datetime

import pytz


def get_japan_time():
    japan_timezone = pytz.timezone('Asia/Tokyo')
    japan_time = datetime.now(japan_timezone)
    formatted = japan_time.strftime("%b %d %H %M %S")
    return formatted


formatted = get_japan_time()
print(formatted)
