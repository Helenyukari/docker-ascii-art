FROM python:3.11-slim

WORKDIR /app

COPY app.py .

RUN pip install pyfiglet

ENTRYPOINT  ["python", "app.py"]