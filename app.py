from flask import Flask, render_template

# create server

app = Flask(__name__)

@app.route('/') # main route
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)