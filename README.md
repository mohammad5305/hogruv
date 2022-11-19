# hogruv
![image](https://user-images.githubusercontent.com/71145952/202860623-26c6545c-5bf6-4932-b82f-8bf35835e95e.png)

a simple and minimal home page for browsers with gruvbox and Its useful for people like me that can't manage their TODO and updated every day.

## Usage
I would recommend using the docker image because its easier
```docker
docker build -t hogruv:latest
docker container run -d -p 8080:8080 hugrv:latest
```
Also you can run it without docker:
```
pip install -r requirements.txt
FLASK_APP=app flask --host 0.0.0.0 --port 8080 run
```
and change your default home page to `localhost:8080`
