import requests
from bs4 import BeautifulSoup
import urllib3

# 경고 메시지를 무시하도록 설정
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 크롤링할 웹 페이지 URL
url = "https://www.jejusi.go.kr/field/culture/festival/list.do?currentPageNo=1"

response = requests.get(url, verify=False)

# 나머지 코드는 이전과 동일하게 유지
soup = BeautifulSoup(response.text, 'html.parser')

restaurants = soup.find_all('div', class_='text')

# 이미지 주소와 텍스트 내용을 파일로 저장
with open("../무제 폴더/output.txt", "w", encoding="utf-8") as text_file:
    for content in restaurants:
        # 이미지 주소 추출 및 저장
        img_tags = content.find_all('img')
        for img_tag in img_tags:
            img_url = img_tag.get('src')
            if img_url:
                text_file.write("이미지 주소: " + img_url + '\n')

        # 텍스트 내용 저장
        text_file.write('---------------\n')
        text_file.write(content.text + '\n')
        text_file.write('---------------\n')

# 이미지 주소와 텍스트 내용을 출력
for content in restaurants:
    img_tags = content.find_all('img')
    for img_tag in img_tags:
        img_url = img_tag.get('src')
        if img_url:
            print("이미지 주소:", img_url)

    print('---------------')
    print(content.text)
