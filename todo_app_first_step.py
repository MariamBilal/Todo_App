from flask import Flask , render_template,request,jsonify,redirect, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'todo_task'
app.config['MONGO_URI'] = 'mongodb://maryam:maryam22@ds115592.mlab.com:15592/todo_app'

mongo = PyMongo(app)

'''
Inserting task into the db
'''

@app.route("/")
def index():
    return render_template('todo_app_desing.html')

@app.route('/', methods = ['POST'])
def func():
    task = mongo.db.task
    text = {'task' : request.form['task']}
    add = task.insert(text )
    #return "Sucessfully added"
    return redirect(url_for('view'))


'''
displaying task from db onto the form
'''

@app.route('/view' , methods = ['GET'])
def view():
     list_of_task=[]
     task_todo = mongo.db.task
     result = task_todo.find()
     for i in result:
         list_of_task.append(i['task'])
     return render_template('list.html'  , list_of_task = list_of_task )





'''
deleting task from the db
'''


# @app.route('/delete')
# def delete():
#     # return render_template('delete.html')
#     task = mongo.db.task
#     del_text = {'task': request.args.get('task')}
#     find_item = task.find(del_text)
#     if find_item == True:
#         task.remove(del_text)
#         return ('task deleted')
#     else:
#         return "sorry! no item found"
#     return render_template('delete.html')
# @app.route('/delete')
# def deleting_task():

    #return render_template('delete.html')



app.run(debug = True)
