import requests
from bs4 import BeautifulSoup

# 웹 페이지 URL
url = "http://eng.koreabaseball.com/Teams/PlayerSearch.aspx"

# 선수 이름
player_name = "BAEK Seung Geon"

# GET 요청으로 HTML 가져오기
response = requests.get(url)
html = response.text

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(html, "html.parser")

# 선수 이름에 해당하는 요소 찾기
player_element = soup.find("a", text=player_name)

# 선수 정보가 없으면 종료
if player_element is None:
    print("선수를 찾을 수 없습니다.")
    exit(0)

# 선수 정보가 있는 table row 찾기
player_row = player_element.find_parent("tr")

# 선수 정보 추출
player_info = {}
for td in player_row.find_all("td"):
    # 각 td 요소의 title 속성을 가져와서 선수 정보에 추가
    title = td.get("title")
    if title:
        player_info[title] = td.text.strip()

# 가져온 선수 정보 출력
print("선수 이름:", player_name)
for key, value in player_info.items():
    print(key + ":", value)
