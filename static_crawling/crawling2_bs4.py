# path : crawling/crawling2_bs4.py
# url 을 키보드로 입력받아서 크롤링 테스트

import urllib.request, bs4

url = input('접속할 url 입력 : ')
# 프로토콜://도메인명/폴더명..../파일명?이름=값&이름=값....
# queryString : 서버측의 대상 파일로 전달되는 값들을 표현한 것. ?이후 값 = ?이름=값&이름=값....
# https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=%EC%98%81%ED%99%94

# 1. url로 웹페이지에 접속
web_page = urllib.request.urlopen(url)

# 2. 읽어온 인코딩된 소스를 html 태그 구문으로 변경.
result_code = bs4.BeautifulSoup(web_page, 'html.parser')
print(result_code)
