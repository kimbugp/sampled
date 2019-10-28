FROM python:3.7-alpine
WORKDIR /app

COPY cacher/node ./node
COPY cacher/main.py .
COPY requirements.txt .

ENV FLASK_APP main.py
ENV FLASK_ENV production
ENV PYTHONUNBUFFERED 1
RUN pip install -r requirements.txt
CMD ["python", "main.py"]