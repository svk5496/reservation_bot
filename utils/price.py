from info import season, weekday_day_time_price, weekday_night_time_price, weekend_day_time_price, weekend_night_time_price
import datetime

today = datetime.date.today()


def get_price(time):
    getTime = get_time_info(time)
    # 평일 낮
    if today.weekday() < 5 and getTime == "day":
        return str(weekday_day_time_price)
    # 평일 밤
    if today.weekday() < 5 and getTime == "night":
        return str(weekday_night_time_price)
    # 주말 낮
    if today.weekday() >= 5 and getTime == "day":
        return str(weekend_day_time_price)
    # 주말 밤
    if today.weekday() >= 5 and getTime == "night":
        return str(weekend_night_time_price)


def get_time_info(time):
    # 여름 & 18시 까지 = 낮
    if season == "여름" and time < 19:
        return "day"
    # 여름 & 19시 부터 = 밤
    if season == "여름" and time >= 19:
        return "night"
    # 겨울 & 17시 까지 = 낮
    if season == "겨울" and time < 18:
        return "day"
    # 겨울 & 18시 부터 = 밤
    if season == "겨울" and time >= 18:
        return "night"
