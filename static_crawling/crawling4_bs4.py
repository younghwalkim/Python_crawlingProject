# crawling\\crwaling4_bs4.py
# movie 테이블에 기록된 행들을 모두 조회해와서 출력 처리함.

# 등수순 오름차순 정렬해서 모두 조회해 옴
# 조회한 한 행의 정보를 Movie 클래스 객체로 생성해서, 객체를 리스트에 저장 처리함.

import urllib.request, bs4
import cx_Oracle
import common.dbConnectTemplate as dbtemp

import entity.Movie as mv

# 0. 오라클 드라이버 설정
dbtemp.oracle_init()
conn = dbtemp.connect()

# 1. 쿼리문 준비
query = 'select * from movie order by rank asc'

# 2. 쿼리문 실행시키기 위한 객체 준비, 실행 처리
cursor = conn.cursor()
cursor.execute(query)

#3. 객체
movie_list = list()

# 커서가 가진 select 쿼리조회결과를 한 행씩 1개씩 출력
for row in cursor :

    # index 를 이용한 출력 처리
    # for i in range(len(row)):
    #     print(row[i], end=', ')
    # print()

    # 컬럼별로 데이터 하나씩 추출
    movie_list.append(mv.Movie(row[0], row[1], row[2], row[3], row[4], row[5]))

# 작업이 끝나면 받드시 닫음.
cursor.close()
conn.close()

for movie in movie_list:
    print(movie)