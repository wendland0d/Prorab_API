FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /api

COPY /prorab_api/. /api
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt