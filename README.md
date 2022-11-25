# hogruv
![image](https://user-images.githubusercontent.com/71145952/202860623-26c6545c-5bf6-4932-b82f-8bf35835e95e.png)

a simple and minimal home page for browsers with gruvbox and Its useful for people like me that can't manage their TODO and updated every day.

## Installation
I would recommend using the docker compose because its easier
```docker
docker compose up -d
```
Also you can run it without docker:
```
pip install -r requirements.txt
FLASK_APP=app flask --host 0.0.0.0 --port 8080 run
```

## Usage 
Change your new page to `localhost:8080` and for prioritizing use '-' followed with alphabet, tasks without it will be z
like:
```
-A hello world
```
