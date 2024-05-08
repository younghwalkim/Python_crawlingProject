# path : entity/Movie.py
# module : entity.Movie
# 크롤링해서 추출한 영화 정보 저장용 클래스 정의 스크립트.

class Movie:

    # filed (attribute) : private (이름 앞에 __ 2개 붙임)

    rank = 0                # 순위
    title = ''                 # 제목
    star_point = 0.0    # 평점
    release_date = ''   # 개봉일
    genre = ''             # 장르
    link = ''                # 상세페이지 url

    # 생성자
    def __init__(self, rank, title, star_point, release_date, genre, link ):
        self.rank = rank
        self.title = title
        self.star_point = star_point
        self.release_date = release_date
        self.genre = genre
        self.link = link

    # method
    # 연산자 오버로딩
    # java 의 toString() == 파이썬 __str__(self)
    # 객체가 가진 필드값들을 하나의 문장(str)로 만들어서 리턴함.
    def __str__(self):
        return f'{ self.rank }위 : {self.title }, { self.genre }, 평점 : { self.star_point }, 개봉일: { self.release_date }, 상세페이지 : { self.link } '
