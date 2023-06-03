import requests
from bs4 import BeautifulSoup
import pandas as pd  # pandas import 확인

# 웹 페이지 URL
url = "http://eng.koreabaseball.com/Teams/PlayerSearch.aspx"

# GET 요청으로 HTML 가져오기
response = requests.get(url)
html = response.text

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(html, "html.parser")

# 선수 정보를 저장할 리스트 생성
player_info_list = []

# 모든 팀에 대한 정보를 가져옵니다.
for team in soup.select('.sub_tab.team_select ul li'):
    # 팀 이름을 가져옵니다.
    team_name = team.find('h4').text

    # 이 팀의 모든 선수 정보를 가져옵니다.
    for player_row in soup.select('tbody tr'):
        player_info = {"팀 이름": team_name}

        # 선수 이름을 가져옵니다.
        player_info["이름"] = player_row.th.a.text.strip()

        # 선수 번호, 포지션, 생년월일, 신장/체중 정보를 가져옵니다.
        for td in player_row.find_all("td"):
            title = td.get("title")
            if title:
                player_info[title] = td.text.strip()

        # 가져온 선수 정보를 리스트에 추가
        player_info_list.append(player_info)

# 리스트를 데이터프레임으로 변환
df = pd.DataFrame(player_info_list)

# 엑셀 파일로 저장
df.to_excel("players.xlsx", index=False)
