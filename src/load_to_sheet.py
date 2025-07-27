from typing import Dict, List

import gspread


def load_to_sheet(data, url)->Dict :
  g_sheet_cred = gspread.service_account()
  spreadsheet = g_sheet_cred.open_by_url(url)

  sheetname = spreadsheet.get_worksheet(0)

  column_headers = sheetname.row_values(1)

  expected_headers:List[str] = ["State","Temperature","Weather_Condition",
                      "Feels_Like","Humidity", "Dew_Point"]

  if column_headers is None or column_headers != expected_headers:
    sheetname.insert_row(expected_headers, index=1)

  for weather in data:
    sheetname.append_row([weather['State'], weather['Temperature'],
                         weather['Weather_Condition'], weather['Feels_Like'],
                         weather['Humidity'], weather['Dew_Point'] ])
  print('sheet loading done')
  return {
    "message": "Success: Data loaded into Google Sheets",
    "status": 200,
    # "data": data
  }