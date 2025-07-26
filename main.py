from typing import Dict, List, Optional

import uvicorn
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from config import api_url, g_sheet_url
from src.get_weather import get_weather_api

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/templates/static", StaticFiles(directory="templates/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get('/get_weather')
def get_weather_data(state_1:str,state_2:Optional[str] = None,
                     state_3:Optional[str] = None):
  
  weather_url:str = api_url

  states:List[str] = [state_1, state_2, state_3]
  
  # check for empty state names
  state_values:List = [value for value in states if value.strip()]

  if len(state_values) == 0:
    return {
      "message": "No state was given",
      "status": 200
    }
  ## fetch data from API
  weather_for_states:List[dict] = get_weather_api(weather_url, state_values)
  
  return {
     "state": state_values,
     "status": 200
  }


# if __name__ == "__main__":
#   uvicorn.run(app, host="127.0.0.1", port=8000)
