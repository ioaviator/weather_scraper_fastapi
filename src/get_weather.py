from typing import List

import requests

from .scrape_data import scrape_data


def get_weather_api(url:str, states:List)->List[dict]:
  
  weather_data:List = []

  for state in states:
    
    state:str = state.lower().replace(" ", "-")
    
    BASE_URL:str = f"{url}/{state}"
    
    try:
      response = requests.get(BASE_URL)
      if response.status_code != 200:
        print(f'Invalid state value -- {state}')
        continue
    except Exception as e:
      print(f"Error fetching {state}: {e}")
      raise e

    data = scrape_data(response, state)

    weather_data.append(data)
  
  return weather_data
