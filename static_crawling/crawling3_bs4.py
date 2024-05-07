# path : crawling/crawling3_bs4.py
# 네이버 개봉 영화 정보 페이지 크롤링 분석 테스트

import urllib.request, bs4, random as rs

# 1. url로 웹페이지에 접속
web_page = urllib.request.urlopen('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%ED%98%84%EC%9E%AC%EC%83%81%EC%98%81%EC%98%81%ED%99%94')
result_code = bs4.BeautifulSoup(web_page, 'html.parser')
# print(result_code)

# 개봉영화  정보가 기록된 태그 앨리먼트 찾기
# 찾아진 태그 앨리먼트 안의 값을 추출 : find() 함수 사용 => 찾은 첫번째 앤리먼트만 리턴함.
# find(찾을 텍스트가 기록된 태그명, 태그속성_ = '속성값')
# find(태그속성_='속성값')
# find(찾을태그명)

# (방법1)
# 1.1첫번째 항목 한개만 출력
data_box = result_code.find("div", {"class":"data_box"})
# print(data_box)
movie_title = data_box.find("a", {"class":"this_text"})
# print(movie_title)

# 1.2 태그 앨리먼트 여러개 추출 : find_all() 사용
movie_list = result_code.find_all("a", {"class":"this_text"})
# print(movie_list)

# 영화 제목만 추출
for idx in range(len(movie_list)):
    title = movie_list[idx].text
    # print(title)

# 영화제목, 개봉일, 장르, 별점, 링크 추출









# (방법2)
movie_titles = result_code.select("a.this_text")

movie_list = []
for i in movie_titles:

    # title
    title = i.get_text()
    # print("title : ", title)

    # link
    href = "https://search.naver.com/search.naver" + i.attrs['href']
    # print("link : ", href)

    movie = dict()
    movie["title"] = title
    movie["link"] = href
    movie["star_point"] = rs.uniform(0, 10)
    movie["genre"] = ""
    movie["release_date"] = ""

    # # star_point
    # star_points  = result_code.select("span.num")
    # for i in star_points:
    #     star_point = i.get_text()
    #     print("star_point :  ",star_point)
    #
    # # genre
    # genres_result  = result_code.select("div.info dl.info_group")
    # for idx in range(len(genres_result)):
    #     reuslt = genres_result[idx].text
    #     print(idx, reuslt)

    movie_list.append(movie)

# 리스트에 저장된 영화정보 출력
for movie in movie_list :
    print(movie)

# 등수처리 : 별점 이용, 4번째 기록됨 => [3]
sort_list = sorted(movie_list, key=lambda  x : x["star_point"], reverse=True)

print('=====================')

# 정렬 후 등수 추가 확인
for idx in range(len(sort_list)) :
    movie = sort_list[idx]
    movie['rank'] = idx + 1
    print(movie)

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
        conn.commit()
    except :
        conn.rollback()
    finally:
        cursor.close()

dbtemp.close(conn)