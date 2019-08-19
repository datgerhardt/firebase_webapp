from flask import Flask, render_template, url_for, request
from pyrebase import pyrebase


app = Flask(__name__)

Config = {
    "apiKey": "apiKey",
  "authDomain": "projectId.firebaseapp.com",
  "databaseURL": "https://databaseName.firebaseio.com",
  "storageBucket": "projectId.appspot.com",
  "serviceAccount": "path/to/serviceAccountCredentials.json"
  }

firebase = pyrebase.initialize_app(Config)
db = firebase.database()


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form['submit'] == 'add':
            todo_name = request.form['name']
            db.child("todo").push(todo_name)
            todo = db.child("todo").get()
            todo_value = todo.val()
            return render_template('list.html', todo_value=todo_value.values())
        elif request.form['submit'] == 'delete':
            todo_name = request.form['name']
            db.child("todo").push(todo_name)
            todo = db.child("todo").remove()
            todo_done = "Congratulation! You are Done with all your tasks "
            return render_template('list.html', todo_done=todo_done)
    return render_template('list.html')

if __name__ =='__main__':
    app.run(debug=True)
