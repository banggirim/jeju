import re
import pandas as pd

# 주어진 텍스트
text = """
2023 노형동 가을밤 행복음악회
○일 시: 2023. 9. 23.(토) 18시
○장 소: 노형1근린공원(백록초 옆)
 ※ 우천 시 노형초등학교 체육관
○주최·주관: 노형동주민센터·노형동주민자치위원회
---------------
행사 개요
- 행사명 : 제2회 화북, 포구문화제 
- 행사 기간 : 2023.9.22.(금) ~9.23.(토)
- 장소 : 화북포구 일원
- 주요 프로그램
(전시) 화북 역사문화 전시, 대비모주 유래 전시
(공연) 뮤지컬 갈라쇼, 청소년 버스킹, 지역 문화예술 동아리 공연
(기타) 옛길따라 걸을락(樂), 보트타고 유적지 탐방, 깅이잡기&고망낚시
---------------
2023 하반기 거리예술제
- 기간: 2023. 9. 1. ~ 10. 27.
- 장소: 칠성로 상점가, 노웨모루 거리
- 내용: 지역 예술인 공연(음악, 댄스, 마술 등)
"""

# 정규 표현식 패턴
event_pattern = re.compile(r"(\d{4}.*?)\n(?:[○\*\s]*일 시: (.*?)\n[○\*\s]*장 소: (.*?)\n[○\*\s]*(?:.*?\n)?)", re.DOTALL)

# 패턴과 매치되는 모든 행사 정보 추출
event_matches = event_pattern.findall(text)

# 추출한 데이터를 DataFrame으로 변환
data = {
    '행사명': [event_match[0].strip() for event_match in event_matches],
    '일시': [event_match[1].strip() for event_match in event_matches],
    '장소': [event_match[2].strip() for event_match in event_matches]
}

df = pd.DataFrame(data)

# DataFrame 출력
print(df)
