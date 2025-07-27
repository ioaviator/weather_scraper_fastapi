FROM python:3.12

WORKDIR /weather_api

RUN mkdir -p /root/.config/gspread
COPY src/creds/service_account.json /root/.config/gspread/service_account.json

COPY requirements.txt /weather_api/requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]

