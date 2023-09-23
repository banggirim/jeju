import requests
from bs4 import BeautifulSoup

# 웹 페이지 URL 설정
url = 'https://www.jeju.go.kr/sobi/kind/kind.htm'

# 웹 페이지 가져오기
response = requests.get(url)

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(response.text, 'html.parser')
restaurants = soup.find_all('div', class_='shop-content')

# 파일을 열어 HTML을 저장할 준비
with open("output.html", "w", encoding="utf-8") as output_file:
    for content in restaurants:
        # 해당 요소의 HTML 구조와 내용을 저장
        output_file.write(str(content) + '\n')
        output_file.write('---------------\n')

        # 이미지 태그 찾기
        img_tags = content.find_all('img')
        for img_tag in img_tags:
            # 이미지 주소 추출
            img_url = img_tag.get('src')
            if img_url:
                print("이미지 주소:", img_url)
        print('---------------')

        # 해당 요소의 텍스트 내용만 출력
        print(content.text)
        print('---------------')
