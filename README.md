# 웹 크롤링 

### 정적 웹 크롤링
* 크롤링 대상 주소 : [네이버 현재상영영화](https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%ED%98%84%EC%9E%AC%EC%83%81%EC%98%81%EC%98%81%ED%99%94")
* 크롤링 항목 : 제목, 평점, 개봉일, 장르, 상세주소, 랭킹 (평점 기준으로 순위 생성)
* Database 처리 및 재출력

### 동적 웹 크롤링
* 크롤링 대상 : 네이버 검색
* 네이버 > 통합검색 - 로마여행 > 가볼만한곳 클릭 > 6위 여행정보 추출
* [네이버](https://www.naver.com/")
* [네이버 통합검색 결과 - 로마여행](https://search.naver.com/search.naver?where=nexearch&sm=top_sly.hst&fbm=0&acr=1&ie=utf8&query=%EB%A1%9C%EB%A7%88%EC%97%AC%ED%96%89")
* [가볼만한곳 클릭](https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%A1%9C%EB%A7%88%EC%97%AC%ED%96%89")
* 크롤링 항목 : 랭킹, 여행장소, 여행설명, 분류
