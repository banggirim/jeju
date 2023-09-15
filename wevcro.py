import requests
from bs4 import BeautifulSoup

# 웹 페이지 URL 설정
url = 'https://www.jeju.go.kr/sobi/kind/kind.htm'

# 웹 페이지 가져오기
response = requests.get(url)

# BeautifulSoup을 사용하여 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 식당 정보가 있는 요소 선택
restaurants = soup.find_all('div', class_='shop-content')

# 결과 저장할 리스트 초기화
restaurant_data = []

# 각 식당 정보를 크롤링하여 리스트에 저장
for restaurant in restaurants:
    # 식당 이름
    name = restaurant.find('div', class_='shop-title').text.strip()

    # 전화번호를 가져오기 위해 'a' 태그를 찾고 'href' 속성 값을 추출
    phone_href = restaurant.find('a', href=True)['href']

    # "tel:" 접두사를 제외한 부분이 전화번호입니다.
    phone = phone_href.replace('tel:', '').strip()

    # 주소 정보를 직접 추출
    address = restaurant.find('span', class_='shop-info-text').get_text(strip=True, separator='\n')

    # 결과를 딕셔너리로 저장
    restaurant_data.append({
        '이름': name,
        '전화번호': phone,
        '주소': address
    })

# 결과 출력
for data in restaurant_data:
    print(f"식당: {data['이름']}")
    print(f"전화번호: {data['전화번호']}")
    print(f"주소: {data['주소']}")
    print('-' * 50)
