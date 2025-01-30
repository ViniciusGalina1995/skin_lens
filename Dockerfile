# python runtime as a base image
FROM python:3.10.6-buster

#WORKDIR /app

COPY app /app
COPY models /models
COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
