import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the webpage you want to scrape
url = "http://eng.koreabaseball.com/Stats/BattingLeaders.aspx"

# Send a GET request to the webpage
response = requests.get(url)

# Parse the HTML content of the webpage
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table
table = soup.find_all('table')[0] 

# Create an empty list to store the rows
data = []

# Find all 'tr' tags (table rows)
tr_tags = table.find_all('tr')

# Create a list for column headers
column_headers = ['Player', 'TEAM', 'AVG', 'G', 'PA', 'AB', 'R', 'H', '2B', '3B', 'HR', 'TB', 'RBI', 'SB', 'CS', 'SAC', 'SF']

# Loop through each 'tr' tag
for tr in tr_tags:
    # Find all 'td' tags in this row
    td_tags = tr.find_all('td')
    # Create an empty list for this row
    row = {}
    # Loop through each 'td' tag
    for td in td_tags:
        # Get the title and text (value)
        title = td.get('title')
        if title in column_headers:
            # If the title exists, add the cell data to the row dictionary
            row[title] = td.text
    # If the row is not empty, add it to the main data list
    if row:
        data.append(row)

# Create a pandas DataFrame from the data
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel('scraped_data.xlsx', index=False)
