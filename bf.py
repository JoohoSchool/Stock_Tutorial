import requests
from bs4 import BeautifulSoup

# Make a request to the website with headers
url = "https://finance.yahoo.com/quote/MSFT/financials?p=MSFT"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
}
response = requests.get(url, headers=headers)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.content, "html.parser")

# Find the table containing the financial information
table = soup.find("div", {"class": "M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"})

# Find all the table rows (financial data rows)
rows = table.find_all("div", {"class": "D(tbr) fi-row Bgc($hoverBgColor):h"})

# Extract and print the financial information
for row in rows:
    cells = row.find_all("div", {"class": "D(tbc)"})
    for cell in cells:
        print(cell.text.strip())
    print()
    