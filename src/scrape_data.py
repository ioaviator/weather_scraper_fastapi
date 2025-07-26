import re
from typing import Dict

from bs4 import BeautifulSoup


def scrape_data(response, state:str)-> Dict:

  soup = BeautifulSoup(response.text, 'html.parser')

  # --- Extraction from <div id="qlook"> ---
  qlook_div = soup.find('div', id='qlook')

  # Extract temperature from <div class="h2">
  temperature = qlook_div.find('div', class_='h2').get_text(strip=True)

  # Extract weather condition from the first <p> tag
  weather_condition = qlook_div.find('p').get_text(strip=True)

  # Extract only the first text node from the second <p> tag (the "Feels Like" value)
  feels_like_p = qlook_div.find_all('p')[1]

  # Using .contents[0] gives the direct text before the <br> tag
  # e.g., "Feels Like: 39 °C"
  feels_like_text = feels_like_p.contents[0].strip()  

  # Remove the "Feels Like:" part from the string
  feels_like = feels_like_text.replace("Feels Like:", "").strip()

  
  table = soup.find('table', class_='table table--left table--inner-borders-rows')

  humidity_th = table.find('th', string=lambda text: text and 'Humidity:' in text)
  humidity = humidity_th.find_parent('tr').find('td').get_text(strip=True)

  dew_point_th = table.find('th', string=lambda text: text and 'Dew Point:' in text)
  dew_point = dew_point_th.find_parent('tr').find('td').get_text(strip=True)

  ## clean data
  dew_point = re.sub(r"[^\d]", "", dew_point)
  temperature = re.sub(r"[^\d]", "", temperature)
  feels_like = re.sub(r"[^\d]", "", feels_like)

  data:dict = {
    "State": state,
    "Temperature": temperature,
    "Weather_Condition": weather_condition,
    "Feels_Like": feels_like,
    "Humidity": humidity,
    "Dew_Point": dew_point
  }

  return data