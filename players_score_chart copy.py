import requests
from bs4 import BeautifulSoup
import pandas as pd

team_codes = ["sk", "wo", "lg", "ht","nc", "ss","hh","lt","kt","ob"]
for team_code in team_codes:
    url = f"http://eng.koreabaseball.com/Stats/BattingByTeams.aspx?codeTeam={team_code}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find_all('table')[0]
    data = []
    tr_tags = table.find_all('tr')
    for tr in tr_tags:
        td_tags = tr.find_all('td')
        row = {}
        for td in td_tags:
            title = td.get('title')
            if title:
                row[title] = td.text
            elif 'stats_player' in td.get('class', []):
                row['Player'] = td.text
        if row:
            data.append(row)


    df = pd.DataFrame(data)

    df.to_excel(f'scraped_batters_{team_code}.xlsx', index=False)


