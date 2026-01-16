from flask import Flask

app = Flask(__name__)

@app.route("/")
def method():
    return "This is my flask first web app and this time i used debugging"

@app.route("/index")
def index():
    return "This is the index page of my first web app"
    
if __name__ == '__main__':
    app.run(debug=True)