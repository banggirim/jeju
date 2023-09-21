import requests
from bs4 import BeautifulSoup
# 웹 페이지 URL 설정
url = 'https://www.jeju.go.kr/sobi/kind/kind.htm'

# 웹 페이지 가져오기
response = requests.get(url)



# XPath를 사용하여 원하는 요소 선택
# sub_contents = ('span')
soup = BeautifulSoup(response.text, 'html.parser')
restaurants = soup.find_all('div', class_='shop-content')
content = []
# f = open("../제주도해커톤/test.txt", "w+")
# 선택한 요소의 내용을 출력
for content in restaurants:
    print(content.text)

    print('---------------')
    # f.write(content.text)

# f.close()
