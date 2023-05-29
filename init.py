from selenium import webdriver
from info import place_name, user_id, user_password, hour, minute, second, court_number, first_start_time, second_start_time
from utils.price import get_price
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from utils.date import get_future_date
from utils.court import get_place_number, get_court_number
import pytz
import time

# 변수들
place = get_place_number()
register_court_number = get_court_number(court_number, place_name)
first_time_price = get_price(first_start_time)
second_time_price = get_price(second_start_time)

# Path to the webdriver executable. Make sure to download the appropriate driver for your browser.
webdriver_path = './webdriver'

# Create a new instance of the web driver
driver = webdriver.Chrome(webdriver_path)

# Navigate to a website
driver.get('https://www.aytennis.or.kr/Login')

# 컴포넌트 나타날때까지 걸리는 시간
wait = WebDriverWait(driver, 10)

try:
    # id 입력
    id_input = wait.until(EC.element_to_be_clickable((By.NAME, "uid")))
    id_input.send_keys(user_id)

    # password 입력
    pw_input = wait.until(EC.element_to_be_clickable((By.NAME, "pwd")))
    pw_input.send_keys(user_password)

    # button 로그인 버튼 클릭
    login_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".genric-btn.info")))
    login_button.click()

    # 정해진 시간까지 기다리는 로직
    # Set the target UTC time (22:30)
    seoul_tz = pytz.timezone("Asia/Seoul")
    target_time = seoul_tz.localize(datetime.now().replace(
        hour=hour, minute=minute, second=second, microsecond=0))

    while datetime.now(seoul_tz) < target_time:
        # Sleep for 1 second before checking the time again
        print("아직작동중")
        print(datetime.now(seoul_tz) - target_time)
        time.sleep(1)

    # 새로고침 한번 하고
    driver.refresh()

    # 종합운동장 예약 버튼
    # 버튼 나타날때까지 기다리고
    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "span.btn.btn-ms.btn-primary")))

    # element = wait.until(EC.element_to_be_clickable(
    #     (By.CSS_SELECTOR, '#navigation li.indent a[href="/daily/2"]')
    # ))
    # element.click()

    # 다른 코트들 중
    rCourt_elements = driver.find_elements(By.CSS_SELECTOR, 'li.rCourt')

    # 종합운동장(2번째)
    sports_complex_court = rCourt_elements[place-1]

    sports_complex_court_btn = sports_complex_court.find_element(
        By.CSS_SELECTOR, 'span.btn.btn-ms.btn-primary')
    sports_complex_court_btn.click()

    # # 날짜 로직
    future_date = get_future_date(7)
    formatted_future_date = f'/daily/2/{future_date}'

    anchor_element = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, f'a.fc-day-grid-event.fc-h-event.fc-event.fc-start.fc-end[href="{formatted_future_date}"]')))
    anchor_element.click()

    # 달력에서 날짜 클릭(셀렉트박스)
    checkbox1 = f'{future_date}|{place}|{register_court_number}|{first_start_time}|{get_price(first_start_time)}'
    checkbox2 = f'{future_date}|{place}|{register_court_number}|{second_start_time}|{get_price(second_start_time)}'
    print(checkbox1)
    print(checkbox2)
    submit_btn = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'a[href*="utils.confirm()"][class="btn btn-primary"]')))

    try:
        checkbox1_element = driver.find_element(
            By.CSS_SELECTOR, f'input[name="pick[]"][value="{checkbox1}"]')

        if checkbox1_element:
            checkbox1_element.click()
        else:
            print("예약하려고 하는 1번 체크박스를 찾지 못했습니다")
    except:
        print("예약하려고 하는 1번 체크박스를 찾지 못했습니다")

    try:
        checkbox2_element = driver.find_element(
            By.CSS_SELECTOR, f'input[name="pick[]"][value="{checkbox2}"]')

        if checkbox2_element:
            checkbox2_element.click()
        else:
            print("예약하려고 하는 2번 체크박스를 찾지 못했습니다")
    except:
        print("예약하려고 하는 2번 체크박스를 찾지 못했습니다")

    # 예약하기 버튼 클릭
    submit_btn.click()

    # 결제하기 버튼 클릭

    payment_btn = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'a[href*="#none"][class="btn btn-sm btn-primary"]')))
    payment_btn.click()

except Exception as e:
    print("뭔가뭔가 잘못됨", str(e))


while (True):
    pass
