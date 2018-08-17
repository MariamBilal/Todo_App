from flask import Flask, render_template, request,session,json,jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todoappSql.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

sqldb = SQLAlchemy(app)

class todo_task(sqldb.Model):
     id = sqldb.Column(sqldb.Integer,primary_key = True)
     title = sqldb.Column(sqldb.String(30))
     description = sqldb.Column(sqldb.String(140))
     done = sqldb.Column(sqldb.Boolean)

sqldb.create_all()

@app.route('/add' , methods=['POST'])
def task_add():
    task = request.get_json()
    new_todoTask = todo_task(title = task['title'],
                       description = task['description'],
                       done=False)
    sqldb.session.add(new_todoTask)
    sqldb.session.commit()
    return 'Add sucessufully'


@app.route('/view' , methods=['GET'])
def task_view():
    task = todo_task.query.all()
    list_of_task =[]

    for item in task:
        item_data={}
        item_data['id'] = item.id
        item_data['title'] = item.title
        item_data['description'] = item.description
        item_data['done'] = item.done
        list_of_task.append(item_data)

    return jsonify({'task': list_of_task})

@app.route('/delete/<int:task_id>', methods=['DELETE'])
def task_delete(task_id):
    tasks = todo_task.query.filter_by(id=task_id).first()
    if not tasks:
        return jsonify({'No data available'})
    else:
        sqldb.session.delete(tasks)
        sqldb.session.commit()
    return jsonify({'message':'Deleted Sucessfully'})


app.run(debug = True)


