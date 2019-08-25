FROM python:3.6-alpine
WORKDIR .
COPY requirements.txt .
RUN apk add python3-dev  build-base gcc
RUN python3 -m pip install -r requirements.txt
COPY . .
EXPOSE 8080
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app"]