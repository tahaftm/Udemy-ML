from flask import Flask,render_template,request
import pickle
application = Flask(__name__)
app = application
prediction = 0
@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/predict-form",methods = ["POST", "GET"])
def form():
    if request.method == "POST":
        global prediction
        temperature = float(request.form.get("Temperature"))
        RH = float(request.form.get("RH"))
        Ws = float(request.form.get("Ws"))
        Rain = float(request.form.get("Rain"))
        FFMC = float(request.form.get("FFMC"))
        DMC = float(request.form.get("DMC"))
        ISI = float(request.form.get("ISI"))
        Classes = request.form.get("Classes")
        if Classes == "Fire":
            Classes = 1
        else:
            Classes = 0
        Region = request.form.get("Region")
        if Region == "Sidi-Bel Abbes Region":
            Region = 1
        else:
            Region = 0
        with open("model/scaler.pkl", "rb") as f:
            scaler = pickle.load(f)
        with open("model/regressor.pkl", "rb") as f:
            regressor = pickle.load(f)
        pred = regressor.predict(scaler.transform([[temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]]))
        return render_template(
            "form.html",
            prediction=round(pred[0], 2)
        )
    else:
        return render_template("form.html")
    
if __name__ == "__main__":
    app.run(debug=True)