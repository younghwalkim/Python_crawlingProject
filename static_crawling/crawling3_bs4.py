# path : crawling/crawling3_bs4.py
# 네이버 개봉 영화 정보 페이지 크롤링 분석 테스트

import urllib.request, bs4, random as rs

# 1. url로 웹페이지에 접속 및 소스 가져오기
web_page = urllib.request.urlopen('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%ED%98%84%EC%9E%AC%EC%83%81%EC%98%81%EC%98%81%ED%99%94')
result_code = bs4.BeautifulSoup(web_page, 'html.parser')
#print(result_code)

# 개봉영화  정보가 기록된 태그 앨리먼트 찾기
# 찾아진 태그 앨리먼트 안의 값을 추출 : find() 함수 사용 => 찾은 첫번째 앤리먼트만 리턴함.
# find(찾을 텍스트가 기록된 태그명, 태그속성_ = '속성값')
# find(태그속성_='속성값')
# find(찾을태그명)

# 1. find() - 첫번째 항목 추출 및 a 태그 앨리먼트 1개 추출
data_box = result_code.find("div", {"class":"data_box"})
#print(data_box)
movie_title = data_box.find("a", {"class":"this_text"})
#print(movie_title)


# 2.1 find_all() - a 태그 앨리먼트 여러개 추출 : find_all() 사용
movie_title_list = result_code.find_all("a", {"class":"this_text"})
#print(movie_title_list)

# 2.2 영화 제목 추출
for idx in range(len(movie_title_list)):
     title = movie_title_list[idx].text
     #print(title)


### 영화제목, 개봉일, 장르, 별점, 링크 추출 #####################
# 영화정보 div 영역 갯수 확인
movie_div = result_code.find_all("div", {"class": "data_box"})
#print(len(movie_div))

# 결과 list에 담기
movie_list = list()

# 갯수만큼 for 처리
for idx in range(len(movie_div)):
    # 영화 제목 추출 - this_text class 내 a 태그 기준 추출 > text 추출
    movie_title = movie_div[idx].find("a", {"class": "this_text"}).get_text()
    #movie_title = movie_div[idx].find("a", {"class": "this_text"}).text
    #print(movie_title)

    # 상세 주소 추출 - this_text class 내 a 태그 기준 추출 > href 값 추출
    movie_link = movie_div[idx].find("a", {"class": "this_text"}).attrs['href']
    #movie_link = movie_div[idx].find("a", {"class": "this_text"})['href']
    #print(movie_link)

    # 장르 추출 - info_group class 내 dl 태그 기준 추출 > dd 태그 기준 추출 > text 추출
    genre = movie_div[idx].find("dl", {"class": "info_group"}).find("dd").text
    #print(genre)

    # 별점 추출 - num class 내 span 가준 추출 > float 처리
    star_point = float(movie_div[idx].find("span", {"class": "num"}).text)
    #print(star_point)

    # 개봉일 추출 - div class=info > dl 2번째 > dd 태그 추출 > 택스트 추출
    release_date = movie_div[idx].find("div", class_="info").find_all("dl")[1].find("dd").get_text()
    #print(release_date)

    movie = dict()  # 결과 딕셔너리에 저장
    movie["title"] = movie_title
    movie["link"] = "https://search.naver.com/search.naver" + movie_link
    movie["genre"] = genre
    movie["star_point"] = star_point
    movie["release_date"] = release_date

    movie_list.append(movie)

# 리스트 담긴 내용 확인
for movie in movie_list:
    print(movie)

# 등수 처리 : 벌점 이용 , 4번째 기록돔 =>[3]
sort_list = sorted(movie_list, key=lambda x: x["star_point"], reverse=True)
print('sorted after ---------------------------------')
print(sort_list)
print('----------------------------------------------')

# 정렬 후 등수 추가 확인
for idx in range(len(sort_list)):
    movie = sort_list[idx]
    print(movie)
    movie['rank'] = idx + 1

# 오라클 db movie 테이블에 기록 처리
import cx_Oracle
import common.dbConnectTemplate as dbtemp

# 오라클 드라이버 설정 - 애플리케이션 전체에서 딱 한번 실행함.
dbtemp.oracle_init()
conn = dbtemp.connect()

# 크롤링한 결과 db 에 기록 처리 : insert 문 사용
query = "insert into movie values (:1, :2, :3, :4, :5, :6) "

# rank = 0  # 순위
# title = ''  # 제목
# star_point = 0.0  # 평점
# release_date = ''  # 개봉일
# genre = ''  # 장르
# link = ''  # 상세페이지 url

# 리스트에 저장된 딕셔너리를 튜플로 변환해서 쿼리문에 적용해서 실행.
for movie in movie_list :
    tp_value = (movie['rank'], movie['title'], movie["star_point"], movie['release_date'], movie['genre'], movie['link'])
    cursor = conn.cursor()

    try :
        cursor.execute(query, tp_value)
        dbtemp.commit(conn)
    except :
        dbtemp.rollback(conn)
    finally:
        cursor.close()

dbtemp.close(conn)