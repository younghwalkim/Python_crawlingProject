# path : crawling/crawling1_bs4.py
# bs4 (BeautifulSoup4) 를 이용한 웹크롤링 테스트1

#패키지 설치 : pip install beautifulsoup4
# import bs4      # 웹 페이지의 웹문서를 html 로 분석하는 모듈임.
# import urllib.request      # 웹상의 데이터를 가져오는 모듈
import urllib.request, bs4

# 1. url로 웹페이지에 접속
web_page = urllib.request.urlopen('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%ED%98%84%EC%9E%AC%EC%83%81%EC%98%81%EC%98%81%ED%99%94')

# 2. 접속한 페이지 소스를 읽어옴 >  출력확인. '(인코딩된 상태임)
# html_code = web_page.read()
# print(html_code)

# 3. 읽어온 인코딩된 소스를 html 태그 구문으로 변경.
decoding_code = bs4.BeautifulSoup(web_page, 'html.parser')
# print(decoding_code)

# 3-1. 1번째 영화 정보 가져오기
title = decoding_code.select_one('#main_pack > div.sc_new.cs_common_module.case_list.color_5._au_movie_list_content_wrap > div.cm_content_wrap > div > div > div > div.card_content._result_area > div.card_area._panel > div:nth-child(1) > div.data_area > div > div.title.multi_line._ellipsis > div > a')
print('첫번째 영화 제목 : ', title.get_text())

star_point = decoding_code.select_one('#main_pack > div.sc_new.cs_common_module.case_list.color_5._au_movie_list_content_wrap > div.cm_content_wrap > div > div > div > div.card_content._result_area > div.card_area._panel > div:nth-child(1) > div.data_area > div > div.info > dl.info_group.type_visible > dd:nth-child(4) > span')
print(star_point.get_text())

release_date = decoding_code.select_one('#main_pack > div.sc_new.cs_common_module.case_list.color_5._au_movie_list_content_wrap > div.cm_content_wrap > div > div > div > div.card_content._result_area > div.card_area._panel > div:nth-child(1) > div.data_area > div > div.info > dl.info_group.type_visible > dd:nth-child(2)')
print(release_date.get_text())

genre = decoding_code.select_one('#main_pack > div.sc_new.cs_common_module.case_list.color_5._au_movie_list_content_wrap > div.cm_content_wrap > div > div > div > div.card_content._result_area > div.card_area._panel > div:nth-child(1) > div.data_area > div > div.info > dl:nth-child(1) > dd:nth-child(2)')
print(genre.get_text())

print('=================================')
# 3-2. 2번째 영화 정보 가져오기
title = decoding_code.select_one('#main_pack > div.sc_new.cs_common_module.case_list.color_5._au_movie_list_content_wrap > div.cm_content_wrap > div > div > div > div.card_content._result_area > div.card_area._panel > div:nth-child(2) > div.data_area > div > div.title.multi_line._ellipsis > div > a')
print('두번째 영화 제목 : ',title.get_text())

star_point = decoding_code.select_one('#main_pack > div.sc_new.cs_common_module.case_list.color_5._au_movie_list_content_wrap > div.cm_content_wrap > div > div > div > div.card_content._result_area > div.card_area._panel > div:nth-child(2) > div.data_area > div > div.info > dl.info_group.type_visible > dd:nth-child(4) > span')
print(star_point.get_text())

release_date = decoding_code.select_one('#main_pack > div.sc_new.cs_common_module.case_list.color_5._au_movie_list_content_wrap > div.cm_content_wrap > div > div > div > div.card_content._result_area > div.card_area._panel > div:nth-child(2) > div.data_area > div > div.info > dl.info_group.type_visible > dd:nth-child(2)')
print(release_date.get_text())

genre = decoding_code.select_one('#main_pack > div.sc_new.cs_common_module.case_list.color_5._au_movie_list_content_wrap > div.cm_content_wrap > div > div > div > div.card_content._result_area > div.card_area._panel > div:nth-child(2) > div.data_area > div > div.info > dl:nth-child(1) > dd:nth-child(2)')
print(genre.get_text())
