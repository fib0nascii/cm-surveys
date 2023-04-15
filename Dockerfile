FROM python:3.10.6-alpine
MAINTAINER Reagan Kirby and Haroon Khan

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D surveyuser
USER surveyuser

