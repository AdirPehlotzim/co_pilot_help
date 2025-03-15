from datetime import datetime
import pytz
def current_time():
    jerusalem_tz = pytz.timezone("Asia/Jerusalem")
    jerusalem_time = datetime.now(jerusalem_tz)
    return("Jerusalem Time:" +  jerusalem_time.strftime("%Y-%m-%d %H:%M:%S"))