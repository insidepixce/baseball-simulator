import requests
from bs4 import BeautifulSoup
import pandas as pd

# 웹 페이지에 접속하여 HTML 데이터 가져오기
url = 'https://m.sports.naver.com/game/20230602OBKT02023/record'
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)

# Response의 status code를 확인하여 요청이 정상적으로 이루어졌는지 확인
if response.status_code != 200:
    print(f"Request failed: status code {response.status_code}")
else:
    html = response.text

    # BeautifulSoup을 사용하여 HTML 파싱
    soup = BeautifulSoup(html, 'html.parser')

    # 타자 기록 테이블을 찾기 위한 선택자 확인
    table = soup.find('table', class_='record_tbl')

    if table is not None:
        # 테이블의 헤더 추출
        headers = [th.text for th in table.select('thead th')]

        # 테이블의 각 행 추출
        rows = []
        for tr in table.select('tbody tr'):
            data = [td.text.strip() for td in tr.select('td')]
            rows.append(data)

        # DataFrame 생성
        df = pd.DataFrame(rows, columns=headers)

        # DataFrame을 엑셀 파일로 저장
        df.to_excel('dosan_baseball_records.xlsx', index=False)
        print('엑셀 파일로 저장되었습니다.')
    else:
        print('타자 기록 테이블을 찾을 수 없습니다.')
