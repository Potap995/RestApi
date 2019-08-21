FROM python:3.6-alpine
RUN apk add python3-dev build-base gcc
RUN python3 -m pip install flask pymongo flask-restful
COPY . .
ENTRYPOINT ["python", "app.py"]