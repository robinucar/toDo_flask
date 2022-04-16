from crypt import methods
from flask import Flask, redirect, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# create server

app = Flask(__name__)
# relative path sql name
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)  # initialize database


# Todo model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/', methods=['POST', 'GET'])  # main route
def index():
    if request.method == 'POST':
        # getting data from content input
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)  # create a task
            db.session.commit()  # add task to database
            return redirect('/')  # return to index page
        except:
            return 'There was an issue adding your task'

    else:
        # display all current task in the database
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)


# Delete task toute
@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'


# Update Task route
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
       task.content = request.form['content']
       try:
           db.session.commit() # no need add  because we are updating the task
           return redirect('/')
       except:
            return 'There was an issue updating your task'
    else:
        return render_template('update.html', task=task)
if __name__ == "__main__":
    app.run(debug=True)
