from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import random

# 셀레니움 브라우저 설정
options = Options()
options.add_argument('--start-maximized')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

hrefs = []


# 모두 수락한다 용(일단은)
url = 'https://www.justwatch.com/kr'
driver.get(url)
time.sleep(5)


for i in range(3): # 여기 값 수정  (현재년도 - range())
    year = 2025 - i
    url = 'https://www.justwatch.com/kr?exclude_genres=ani,eur,msc,trl,war,wsn&release_year_from={0}&release_year_until={0}'.format(year)
    driver.get(url)
    time.sleep(2)  # 페이지 로딩 대기

    # 🔻 페이지 끝까지 스크롤
    SCROLL_PAUSE_TIME = 1  # 스크롤 후 대기 시간 (초)

    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # 아래로 스크롤
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)

        # 새로운 높이 계산
        new_height = driver.execute_script("return document.body.scrollHeight")

        # 스크롤 더 이상 변화 없으면 종료
        if new_height == last_height:
            break
        last_height = new_height


    # 상위 10개 프로그램 링크 수집
    program_elements = driver.find_elements(By.CSS_SELECTOR, 'a.title-list-grid__item--link')[:300] # [:5] 이거 지우면 다 돔

    for elem in program_elements:
        href = elem.get_attribute('href')
        hrefs.append(href)

video_info = []
# 10개 프로그램 상세 정보 크롤링
for i, url in enumerate(hrefs):
    try:
        driver.get(url)
        time.sleep(random.uniform(2.5, 4.5)) # 딜레이 랜덤값으로 봇탐지 방지

        # 제목
        try:
            title = driver.find_element(By.XPATH, '//h1[contains(@class, "title-detail-hero__details__title")]').text.strip()
        except NoSuchElementException:
            title = ""

        # 시놉시스
        try:
            synopsis = driver.find_element(By.XPATH, '//p[contains(@class, "text-wrap-pre-line mt-0")]').text.strip()
        except NoSuchElementException:
            synopsis = ""

        # 장르
        try:
            genre_tags = driver.find_elements(By.XPATH, '//div[contains(@class, "poster-detail-infos__value")]//span')
            genres_list = [g.text.strip() for g in genre_tags if g.text.strip()]
            genre = genres_list[-1] if genres_list else ""
        except NoSuchElementException:
            genres_list = []

        video_info.append({
            "title": title,
            "synopsis": synopsis,
            "genre": genre
        })

        print(f"✅ {i+1}/{len(hrefs)}: {title} | {genre}")
    except Exception as e:
        print(f"❌ {i+1}/{len(hrefs)} 에러: {e}")
        continue

driver.quit()

# 결과 저장
df = pd.DataFrame(video_info, columns=["title", "synopsis", "genre"])
df.to_csv('./crawling_data/justwatch_test.csv', index=False, encoding='utf-8-sig')
print("🎉 테스트 완료! justwatch_test.csv 저장됨")
