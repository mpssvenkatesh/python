import datetime
import pytz

def current_time_in_lagos():
    lagos_tz = pytz.timezone('Africa/Lagos')
    current_time = datetime.datetime.now(lagos_tz)
    return current_time.strftime('%Y-%m-%d %H:%M:%S %Z')

print("Current time in Lagos:", current_time_in_lagos())
