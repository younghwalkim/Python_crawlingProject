# dynamic_crawling\\crawling_run.py
# 동적 웹크롤링 구동하는 파이썬 스크립트

# 동적 웹 크롤링 : selenium 모듈 사용함 => 외부패키지 설치
'''
selenium 모듈은 웹브라우저 연동, 브라우저에 입력된 웹 사이트와
이 사이트의 검색필드의 검색 키워드를 파이썬을 통해 입력받아서,
해당 사이트로 전송해서 검색필드태그의 값으로 적용시켜서 
검색을 실행하게 함 :  원격 검색

검색결과 페이지가 브라우저에 출력되면, 파이썬에서 읽어와서 분석함.

동적 웹 크롤링의 동작 :
브라우저 구동 => 사이트 접속 => 검색필드 태그 찾음 => 검색키워드 전송
=> 브라우저 웹페이지에서 검색 적용 => 검색실행 => 잠시대기 
=> 브라우저에 검색 결과가 출력 => 파이썬에서 읽어옴. => 분석
'''

## import 방법 ##
# import 모듈명[as 줄임말] => 모듈이 가진 전체 내용이 임포트 됨.
# 모듈이 가진 일부 항목만 선택해서 임포트 할 수 있음.
# from 모듈명 import 선택항목[, 선택항목, 하위모듈명, 함수명, 클래스명, ...]

from selenium import webdriver as wd # 하위모듈
from selenium.webdriver.chrome.service import Service  # 클래스
from bs4 import BeautifulSoup as bs # 하위모듈
from selenium.webdriver.common.by import By # 클래스

# 명시적 대기를 위해 (waiting 을 명시함)
from selenium.webdriver.support.ui import WebDriverWait # 클래스
from selenium.webdriver.support import  expected_conditions as EC

import time

# selenium 과 연결할 브라우저 선택 : 크롬.(chrome)
# 현재설치사용중인 크롬브라우저의 버전을 확인함.  - 버전 124.0.6367.119(공식 빌드) (64비트)
# 웹에서 '크롬 드라이버' 검색 > 확인된 버전과 같은 드라이버 zip 을 다운받음
# https://googlechromelabs.github.io/chrome-for-testing/#stable  : chromedriver	win64
# https://storage.googleapis.com/chrome-for-testing-public/124.0.6367.91/win64/chromedriver-win64.zip
# 압축풀어서 압축푼 폴더 안의 exe 파일을 현재 프로젝트 폴더로 복사함.

import common.dbConnectTemplate as dbtemp

# DB 저장 처리용 모듈
from model.tour_model import TourModel
from model.tour import TourInfo

def run():
    # 1. 크롬 드라이버 실행 (크롬브라우저 실행)
    # driver = wd.Chrome(service=Service('./chromedriver.exe'))
    driver = wd.Chrome()

    # 2. 크롬 드라이버에 url 주소 넣고 실행
    main_url = 'https://www.naver.com'
    # main_url = input('연결할 사이트 url 입력 : ')
    driver.get(main_url)

    # 페이지가 완전히 로딩되도록 3초동안 기다림
    # time.sleep(3)

    keyword = '로마여행'
    # keyword = input('검색할 키워드 : ')

    # 검색결과 저장할 리스트
    tour_list = []

    # 3. 접속한 페이지의 검색입력필드 찾아서 검색 키워드 입력해서 실행되게 처리.
    # 검색필드 태그 (element)는 브라우저 '개발자도구 > Elements' 탭에서 찾음
    # 찾은 앨리먼트 태그에서 마우스 우클릭 > copy > copy selector 선택함.
    # input 태그 id명 : # query
    input_tag = driver.find_element(By.ID, value='query')
    # print(input_tag)
    input_tag.send_keys(keyword)    # 검색input 에 로마여행 자동 입력됨.

    # 4. 검색 버튼 클릭 자동
    # button 태그 선택자 복사해 옴 : # sform > fieldset > button
    driver.find_element(By.CSS_SELECTOR, '#sform > fieldset > button').click()
    
    # 잠시 대기 => 검색결과 페이지가 브라우저에 출력되고 나서 바로 데이터를 획득하는 행위는
    # 명시적으로 (코드상으로 표기) 대기시켜야 함.
    # 획득할 데이터가 발견될 때까지 대기시킴
    # 대기방법 : 명시적 대기와 암묵적 대기 2가지 임.

    # 5-1. 명시적 대기 :  요구한 엘리먼트를 찾을 때까지 대기시킴
    # 로마가볼만한 곳 글자 출력될때까지
    # #nxTsOv > div > div.MainContainer._travel_header.MainContainer-vjtko > div.content-qIit7 > div.SummaryTopPoiContainer-qpzcR > div > div.head-xMGxp > div > h3
    try:
        element = WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#nxTsOv > div > div.MainContainer._travel_header.MainContainer-vjtko > div.content-qIit7 > div.SummaryTopPoiContainer-qpzcR > div > div.head-xMGxp > div > h3')))
        # 지정한 앨리먼트 위치를 확인하면 대기 종료됨.
    except Exception as msg:
        print('대기 요청 타임 아웃 : ', msg)

    # 5-2 암묵적 대기
    # DOM (document Object Model : 태그 사용 계층 구조) 이 전부 다 브라우저에 로그될 때까지 (모두 읽어들일때까지) 대기하게 하고,
    # 먼저 로드되면 바로 태그 앨리먼트를 찾도록 진행함.
    # 앨리먼트 찾을 시간(초)를 지정하면, 지정 시간동안 DOM 풀링을 지시할 수 있음.
    driver.implicitly_wait(20)

    # 5-3. 절대적 대기 설정
    # time.sleep(10)

    # 6-1. "가볼만한 곳" 클릭.처리
    # 로마 > 가볼만한 곳 : 클릭처리 > 아래쪽에 정보가 표시됨.
    # #nxTsOv > div > div.MainContainer._travel_header.MainContainer-vjtko > div.PanelHeader-vpb6F > div.TabList-Erooo._scroll_wrapper > div.scroll-D9KKR._scroller > ul > li:nth-child(4) > a
    driver.find_element(By.CSS_SELECTOR, "#nxTsOv > div > div.MainContainer._travel_header.MainContainer-vjtko > div.PanelHeader-vpb6F > div.TabList-Erooo._scroll_wrapper > div.scroll-D9KKR._scroller > ul > li:nth-child(4) > a").click()
    # time.sleep(10)

    # 6-2. 연습 - "가볼만한곳 더보기" 클릭 처리
    # #nxTsOv > div > div.MainContainer._travel_header.MainContainer-vjtko > div.content-qIit7 > div > div > div.TopPoi-AF_rQ > div.more-y7DDV > div > a
    # driver.find_element(By.CSS_SELECTOR, "#nxTsOv > div > div.MainContainer._travel_header.MainContainer-vjtko > div.content-qIit7 > div > div > div.TopPoi-AF_rQ > div.more-y7DDV > div > a").click()
    #time.sleep(10)

    # 해당 페이지 영역에서 데이터를 가져올 때, 혹시 로그인이 필요한 경우에는 로그인 세션 관리 필요함.
    # 데이터가 많으면 세션 타임아웃에 의해서 자동 로그아웃 될 수 있으므로,
    # 특정 단위별로 로그아웃하고, 재로그인하는 처리가 필요함. => loop 문 구동, 일괄적으로 접근 처리 필요 : 메타 정보 획득

    # 7. 가볼만한 곳 항목들 추출
    item_list = driver.find_elements(By.CLASS_NAME, "TopPoiItem-MgXeO")
    # print(len(item_list))
    # print(item_list)

    # 8-1. 가볼만한 곳 항목에서 데이터 추출하기
    # 순위, 장소이름, 장소설명, 장소구분

    # 8-2. db 저장처리를 위한 객체 생성
    tm = TourModel()

    # 9. 기존 테이블에 저장된 정보 모두 지우기
    tm.delete_all()

    for item in item_list:
        rank = item.find_element(By.CSS_SELECTOR, "a > figure > span").text
        # print(rank)
        name = item.find_element(By.CSS_SELECTOR, "a > div > span.subject-G1Fz6 > b.name-icVvV").text
        # print(name)
        description = item.find_element(By.CSS_SELECTOR, "a > div > span.desc-tw973").text
        # print(description)
        category  = item.find_element(By.CSS_SELECTOR, "a > div > div > span").text
        # print(category)

        # 튜플로 저장 처리
        tp_info = (rank, name, description, category)

        # db에 저장 처리
        tm.insert_tour(tp_info)

    # 10-1. DB에 저장된 정보 조회 출력 확인
    resultset = tm.select_all()

    # 10-2. 리턴된 정보들을 한행씩 toruinfo  객체에 저장 처리하고, 리스트에 추가
    tour_list =[]
    for row in resultset:
        tourInfo = TourInfo(row[0], row[1], row[2], row[3])

        # 객체정보 출력확인
        print(tourInfo)

        tour_list.append(tourInfo)

    print(tour_list)

    # 11. 크롬 브라우저 및 드라이버 종료
    driver.close()
    driver.quit()

    # 12. main으로 리턴 : 프로세스 종료
    return










