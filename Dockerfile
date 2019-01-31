FROM python:3.7

WORKDIR /usr/app

COPY /app/server.py .

EXPOSE 8011

ENTRYPOINT ["python3.7", "/usr/app/server.py"]
