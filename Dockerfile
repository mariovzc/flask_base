# Use an official Python runtime as an image
FROM python:alpine3.16

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

RUN apk add make

WORKDIR /app
COPY . /app