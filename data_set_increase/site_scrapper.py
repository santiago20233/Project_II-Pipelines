import requests
from bs4 import BeautifulSoup
import requests as re


def mapper(old_date):
    
    new_dates_map = {
                     "Jan":"01",
                     "Feb": "02",
                     "Mar": "03",
                     "Apr": "04",
                     "May": "05",
                     "Jun": "06",
                     "Jul": "07",
                     "Aug": "08",
                     "Sep": "09",
                     "Oct": "10",
                     "Nov": "11",
                     "Dec": "12"
                    }
    month = new_dates_map[ old_date.split()[1]]
    day = old_date.split()[0]
    year = old_date.split()[2]

    return f"{year}-{month}-{day}"

def find_champions(page_name):
    data = {}
    with open(page_name) as fp:
        soup = BeautifulSoup(fp, "html.parser")
        #table = soup.find('table', attrs={'class':'lineItemsTable'})
        table_body = soup.find('tbody')

        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            old_date_formated = cols[2].find(text=True)
            new_formated_formated = mapper(old_date_formated)
            name_lines = cols[3].find_all("span")
            name = name_lines[0].find(text=True)
            surename = name_lines[1].find(text=True)
            data[new_formated_formated] = name + " " + surename
    return data


def download_page(year):
    page_name = f"doc_{year}.html"
    with open(page_name, "w") as fp:
        res = re.get(
            f'https://www.formula1.com/en/results.html/{year}/races.html')
        fp.write(res.text)
    return page_name


def process_champion_page(year):
    page_name = download_page(year)
    data = find_champions(page_name)
    return data


def merge(dict1, dict2):
    return(dict2.update(dict1))




def process_championships():
    response = {}
    for year in range(1950, 2022):
        data_year = process_champion_page(year)
        merge(data_year, response)

    return response

