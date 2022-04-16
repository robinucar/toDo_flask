from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# create server

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' # relative path sql name
db = SQLAlchemy(app) # initialize database


# Todo model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' %self.id 


@app.route('/') # main route
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)