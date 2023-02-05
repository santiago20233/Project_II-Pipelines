import requests

def consult_api():
    all_seasons = []
    for year in range(1950,2020):

        url = f"http://ergast.com/api/f1/{year}.json"


        response = requests.request("GET", url).json()
        year_data = response["MRData"]["RaceTable"]["Races"]
        
        all_seasons.append(year_data)


   
    return all_seasons