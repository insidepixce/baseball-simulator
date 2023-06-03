import requests
from bs4 import BeautifulSoup
import pandas as pd

# 웹 페이지 URL
url = "http://eng.koreabaseball.com/Teams/PlayerSearch.aspx"

# GET 요청으로 HTML 가져오기
response = requests.get(url)
html = response.text

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(html, "html.parser")

# 모든 선수 요소를 찾음
player_elements = soup.select('th[title="player"]')

# 모든 선수에 대한 정보를 저장할 리스트
all_players_info = []

for player_element in player_elements:
    player_name = player_element.text.strip()

    # 선수 정보가 있는 table row 찾기
    player_row = player_element.find_parent("tr")

    # 선수 정보 추출
    player_info = {'name': player_name}
    for td in player_row.find_all("td"):
        # 각 td 요소의 title 속성을 가져와서 선수 정보에 추가
        title = td.get("title")
        if title:
            player_info[title] = td.text.strip()

    # 선수 정보를 리스트에 추가
    all_players_info.append(player_info)

# DataFrame 생성
df = pd.DataFrame(all_players_info)

# 엑셀 파일로 저장
df.to_excel('ssg_pitcher.xlsx', index=False)
