from flask import Flask

# create server

app = Flask(__name__)

@app.route('/') # main route
def index():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)