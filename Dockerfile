# python runtime as a base image
FROM python:3.10.6-buster

WORKDIR /prod
COPY requirements.txt /prod/requirements.txt
RUN pip install -r requirements.txt

COPY app /prod/app
COPY models /prod/models

CMD uvicorn app.main:app --host 0.0.0.0 --port $PORT
