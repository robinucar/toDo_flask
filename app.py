from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# create server

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' # relative path sql name
db = SQLAlchemy(app) # initialize database

@app.route('/') # main route
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)