FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD exec gunicorn  --workers 1 --threads 8 --timeout 0 api:app