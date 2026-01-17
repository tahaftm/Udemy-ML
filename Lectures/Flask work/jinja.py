from flask import Flask, redirect, url_for, request, render_template

# jinja basically means to send data back to html though either of these:
# {{}}  to display a single variable 
# {% %} to perform for loop or conditions using if else
app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def welcome():
    return render_template("index.html")

@app.route("/pass-or-fail", methods = ["GET","POST"])
def passfail():
    if request.method == "POST":
        maths = float(request.form["maths"])
        physics = float(request.form["physics"])
        chemistry = float(request.form["chemistry"])
        english = float(request.form["english"])
        percent = ((maths+physics+chemistry+english) / 400)*100
    else:
        return render_template("index.html")
    return render_template("result.html",percent = percent, maths=maths, physics=physics, chemistry=chemistry, english = english)
if __name__ == "__main__":
    app.run(debug=True)