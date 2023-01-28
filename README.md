# hogruv
![image](https://user-images.githubusercontent.com/71145952/215286684-9fe2a3b3-e128-4c6d-99c9-8388dd70a831.png)



A simple and minimal TODO list for browsers and Its useful for people like me that can't manage their TODO and updated every day.

## Installation
I recommend using the docker compose because its easier
```docker
docker compose up -d
```
Also you can run it without docker:
```
pip install -r requirements.txt
FLASK_APP=app flask --host 0.0.0.0 --port 8080 run
```

## Usage 
In most browsers for changing new page you need to install a plugin

Chrome: [New Tab Redirect](https://chrome.google.com/webstore/detail/new-tab-redirect/icpgjfneehieebagbmdbhnlpiopdcmna?hl=en)

Firefox: [New Tab Override](https://addons.mozilla.org/en-US/firefox/addon/new-tab-override/)

Then change your new page to `localhost:8080`

### Prioritizing Tasks
Use a hyphen followed by a alphabet like:
```
-A hello world
```

### Date
Use Today, Tomorrow, Yesterday or a date with following format m/d like:
```
buying gorcriess today
```

The place of date doesn't matter It the end or start.
### Other color schemes
You can change color scheme by editing `/static/css/style.css` and changing colors variables

