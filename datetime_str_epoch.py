from datetime import datetime

user_time = "2019-06-11 18:06:23"

def get_epoch_time(str_time=None):
    if not str_time:
        str_time = "%s" % datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    utc_time = datetime.strptime(str_time, "%Y-%m-%d %H:%M:%S")
    print(utc_time)
    epoch_time = int((utc_time - datetime(1970, 1, 1)).total_seconds())

    print(epoch_time)
    return epoch_time

get_epoch_time(user_time)   # if time is given
get_epoch_time()            # if time not given then it will take current time