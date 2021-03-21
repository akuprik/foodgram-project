FROM python:3.8.5
WORKDIR /foodgram

COPY . .
RUN pip install -r /foodgram/requirements.txt
CMD gunicorn foodgram.wsgi:application --bind 0.0.0.0:8000
