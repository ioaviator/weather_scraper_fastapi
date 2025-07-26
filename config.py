import os

from dotenv import load_dotenv

load_dotenv()

g_sheet_url = os.getenv("G_SHEET_URL")
api_url = os.getenv("WEATHER_URL")

