from flask import Flask, render_template, request, redirect, abort
import jinja2
from re import sub

app = Flask(__name__)


# Custom filter method
def regex_replace(s, find, replace):
    """A non-optimal implementation of a regex filter"""
    return sub(find, replace, s)


jinja2.filters.FILTERS['resub'] = regex_replace


@app.route('/')
def home():
    with open('./todo.txt', 'r') as todo:
        todo_txt = todo.readlines()
    todo_txt.sort(key=lambda x: x[1].lower() if x[0] == '-' else 'z')
    return render_template('index.html', todo_txt=todo_txt)


@app.route('/add', methods=["GET"])
def add():
    with open('./todo.txt', 'a') as todo:
        todo.write(request.args.get('todo_box')+"\n")

    return redirect('/')


@app.route('/del', methods=["GET"])
def delete():
    if not request.args.get('task'):
        abort(400)

    else:
        with open("./todo.txt", 'r+') as fp:
            lines = fp.readlines()

            fp.seek(0)

            fp.truncate()

            for line in lines:
                if line.strip() != request.args.get('task').strip():
                    fp.write(line)

    return redirect('/')
