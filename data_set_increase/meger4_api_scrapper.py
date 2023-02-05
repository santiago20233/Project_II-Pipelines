import pandas as pd
from site_scrapper import process_championships
from api_extractor import consult_api
from utils import clean_directory

def merge_content(api_results, data_championships):
    
    
    for api_item_info in api_results:

        for race_info in api_item_info:
            race_date = race_info["date"]
            if(race_date in data_championships):
                champion_name = data_championships[race_date]
                race_info["champion name"]=champion_name
            else:
                race_info["champion name"]="unavailable"
            

    return api_results



