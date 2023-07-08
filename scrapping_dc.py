import requests
from bs4 import BeautifulSoup

url = 'https://gall.dcinside.com/board/lists/?id=doosanbears_new1'

# HTTP GET 요청을 보냅니다.
response = requests.get(url)

# 상태 코드를 확인합니다.
if response.status_code == 200:
    # 응답의 내용을 BeautifulSoup을 사용해 파싱합니다.
    soup = BeautifulSoup(response.text, 'html.parser')

    # 게시물 리스트를 찾습니다.
    post_list = soup.find_all('tr', class_='ub-content')

    # 각 게시물에 대한 정보를 추출합니다.
    for post in post_list:
        # 제목 추출
        title = post.find('td', class_='gall_tit').text.strip()

        # 글쓴이 추출
        author = post.find('td', class_='gall_writer ub-writer').text.strip()

        # 내용 추출
        content = post.find('td', class_='gall_tit ub-word').text.strip()

        # 업로드 시간 추출
        upload_time = post.find('td', class_='gall_date').text.strip()

        # 결과 출력
        print('제목:', title)
        print('글쓴이:', author)
        print('내용:', content)
        print('업로드 시간:', upload_time)
        print('---')
else:
    # 보안 검증 실패 시 에러 문구 출력
    print("스크래핑에 실패했습니다. 보안 검증이 필요한 상태입니다.")
