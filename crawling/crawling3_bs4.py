# path : crawling/crawling3_bs4.py
# 네이버 개봉 영화 정보 페이지 크롤링 분석 테스트

import urllib.request, bs4

# 1. url로 웹페이지에 접속
web_page = urllib.request.urlopen('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%ED%98%84%EC%9E%AC%EC%83%81%EC%98%81%EC%98%81%ED%99%94')
result_code = bs4.BeautifulSoup(web_page, 'html.parser')
# print(result_code)

# 개봉영화  정보가 기록된 태그 앨리먼트 찾기
# 찾아진 태그 앨리먼트 안의 값을 추출 : find() 함수 사용 => 찾은 첫번째 앤리먼트만 리턴함.
# find(찾을 텍스트가 기록된 태그명, 태그속성_ = '속성값')
# find(태그속성_='속성값')
# find(찾을태그명)

movie_titles = result_code.select("a.this_text")

# title
for i in movie_titles:
    title = i.get_text()
    print(title)

# link
for i in movie_titles:
    href = i.attrs['href']
    print(href)

# star_point
star_points  = result_code.select("span.num")

for i in star_points:
    star_point = i.get_text()
    print(star_point)

# genre
genres  = result_code.select("div.info dl.info_group dd")

for i in genres:
    genre = i.get_text()
    print(genre)
