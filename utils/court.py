from info import place_name

# 시청, 종합, 자유, 중앙, 호계


def get_place_number():
    # Get today's date
    if place_name == "시청":
        return 1
    elif place_name == "종합":
        return 2
    elif place_name == "자유":
        return 3
    elif place_name == "중앙":
        return 4
    elif place_name == "호계":
        return 5


def get_court_number(courtNumber, placeName):
    if (placeName == "시청"):
        return courtNumber
    if (placeName == "종합"):
        return courtNumber+4
    if (placeName == "자유"):
        return courtNumber+11
    if (placeName == "중앙"):
        return courtNumber+15
    if (placeName == "호계"):
        return courtNumber+19
