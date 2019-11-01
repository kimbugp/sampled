FROM python:3.6-slim
WORKDIR /app

COPY cacher/node ./node
COPY cacher/wsgi.py .
COPY requirements.txt .

ENV FLASK_APP wsgi.py
ENV FLASK_ENV production
ENV PYTHONUNBUFFERED 1
RUN pip install -r requirements.txt
CMD gunicorn --bind=0.0.0.0:80 -w 2 wsgi:app