from flask import Flask, render_template, request, redirect, abort
import jinja2
import re
import json
from datetime import datetime, timedelta

app = Flask(__name__)


# Custom filter method
def regex_replace(s, find, replace):
    """A non-optimal implementation of a regex filter"""
    return re.sub(find, replace, s)


def is_persian(string):
    pattern = r"[\u0600-\u06FF\u0750-\u077F\u0590-\u05FF\uFE70-\uFEFF]"

    return re.search(pattern, string) != None


def make_para(task, class_attr):
    class_attr = str(class_attr)
    if is_persian(task):
        class_attr = " fa"

    return f'<span class="{class_attr}">{regex_replace(task, "-[A-Za-z]", "")}</span>'


jinja2.filters.FILTERS['resub'] = regex_replace


@app.route('/')
def home():
    with open('./todo.json', 'r') as todo_file:
        todo_list = json.load(todo_file)

    todo_list = dict(sorted(todo_list.items()))

    for day in todo_list.values():
        day.sort(key=lambda x: x[1].lower() if x[0] == '-' else 'z')

    return render_template('index.html', todo_list=todo_list, make_para=make_para, today=datetime.today(), timedelta=timedelta)


@app.route('/add', methods=["GET"])
def add():
    with open('./todo.json', 'r+') as todo:
        todo_list = json.load(todo)
        new_task = request.args.get('todo_box')
        date_pattern = r"\d+\/\d+"
        today = datetime.today().strftime("%m/%d")

        if re.search(date_pattern, new_task):
            date = re.search(date_pattern, new_task).group()
            new_task = re.sub(date_pattern, "", new_task)
        elif re.search("today", new_task.lower()):
            date = today
            new_task = re.sub("today", "", new_task.lower())
        else:
            date = "long-term"

        if todo_list.get(date):
            todo_list[date] += [new_task]
        else:
            todo_list.update({date: [new_task]})

        todo.write(json.dumps(todo_list))

    return redirect('/')


@ app.route('/del', methods=["GET"])
def delete():
    if not request.args.get('task'):
        abort(400)

    else:
        date = request.args.get("date")
        task = request.args.get("task")
        with open("./todo.json", 'r+') as todo:
            todo_list = json.load(todo)
            field = todo_list[date]
            if len(field) == 1:
                todo_list.pop(date)
            else:
                field.remove(task)
            todo.write(json.dumps(todo_list))

    return redirect('/')
