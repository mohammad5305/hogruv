from flask import Flask, render_template, request, redirect, abort

app = Flask(__name__)


@app.route('/')
def home():
    with open('./todo.txt', 'r') as todo:
        todo_txt = todo.readlines()

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
