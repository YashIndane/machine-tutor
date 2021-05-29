from flask import Flask, render_template, request , send_file
import simple_linear_regression as s 

app = Flask("machine_tutor")

def upload_file():
  file = request.files['file']
  file.save(file.filename)

@app.route("/home")
def homepage():
  return render_template("home.html")

@app.route("/regression")
def regression_algos():
  return render_template("regressor.html")

@app.route("/simple-regression", methods = ["POST", "GET"])
def train_simple_regression():
  upload_file()
  test_size = request.args.get("ts")
  random_state =  request.args.get("rs")
  s.sil(request.files["file"].filename, test_size, random_state)
  return "model trained!"

@app.route("/downloads")
def download():
  return render_template("downloads.html")

@app.route("/getmodel")
def download_model():
  return send_file("SalaryData.csv.pk1", as_attachment = True)
  
  

app.run(host="0.0.0.0", port=120)

