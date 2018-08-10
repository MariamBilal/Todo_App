from flask import Flask , render_template,request,jsonify,redirect, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'todo_task'
app.config['MONGO_URI'] = 'mongodb://maryam:maryam22@ds115592.mlab.com:15592/todo_app'

mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template('todo_app_desing.html')




@app.route('/',methods = ['POST'])
def func():
    task = mongo.db.task
    text = {'task' : request.form['task']}
    add = task.insert(text )
    return "Sucessfully added"


# @app.route('/add')
# def add(text):
#
#     return ('suceesfully added')


app.run(debug = True)
