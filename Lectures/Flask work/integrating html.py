from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def method():
    return "<html><h1>Simple Flask</h1><br><h6>This is a simple flask app</h6></html>"

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run()