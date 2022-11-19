# hogruv
a simple and minimal home page for browsers with gruvbox and Its useful for people like me that can't manage their TODO and updated every day.

## Usage
I would recommend using the docker image because its easier
```docker
docker build -t hogruv:latest
docker container run -d -p 8080:8080 hugrv:latest
```
and change you default home page to `localhost:8080`

also you can run it without docker:
```
pip install -r requirements.txt
FLASK_APP=app flask --host 0.0.0.0 --port 8080 run
```
