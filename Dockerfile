FROM python:3.8-slim-buster

WORKDIR /code

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080
ENV FLASK_APP=app

EXPOSE 8080

CMD ["flask", "run"]
