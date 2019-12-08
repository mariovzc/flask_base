# Use an official Python runtime as an image
FROM python:3.7-alpine3.9

WORKDIR /app-run

COPY requirements.txt /app-run/requirements.txt
RUN pip install -r /app-run/requirements.txt

WORKDIR /app-run
COPY . /app-run

ENTRYPOINT ["gunicorn", "-w 4", "--bind", "0.0.0.0:8000", "--access-logfile", "-", "--error-logfile", "-", "server:app"]