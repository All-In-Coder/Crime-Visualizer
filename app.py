from flask import Flask, url_for, request, render_template, redirect
import os
import time
import pandas as pd
from werkzeug.utils import secure_filename

import model
from flask.wrappers import Response
from csv import writer

app = Flask(__name__)

# Global Variable
data = []
MY_PATH = os.path.abspath(os.getcwd())


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/show', methods=['GET'])
def readCsv():
    return render_template("show.html")


@app.route('/send', methods=['POST'])
def send():
    global data
    file = request.files['myfile']
    data = pd.read_csv(file)
    data2 = data

    data2.to_csv('test.csv', index=False)
    return render_template('options.html')


@app.route('/addDetails', methods=['GET'])
def addDetails():
    return render_template('fillDetails.html')


@app.route('/fillDetails', methods=['POST'])
def fillDetails():
    attribute = ['Dates', 'Category', 'Description', 'Day Of Week', 'District', 'Resolution', 'Address']
    store = []
    for i in attribute:
        store.append(request.form[i])

    with open('test.csv', 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(store)
        f_object.close()
    return redirect('/addDetails')


@app.route('/visualizeOptions')
def visualizeOptions():
    return render_template("options.html")


@app.route('/getReport')
def getReport():
    Report = model.getReport()
    return render_template("showReport.html", haveReport=True, Report=Report)


@app.route('/sendChartOption', methods=["POST"])
def sendChartOption():
    print(request.form)
    keys = list(request.form)
    name = model.run(keys)
    print(name)
    return render_template('options.html', haveImage=True, imgPath=name)


@app.route('/uploader')
def upload():
    return render_template("upload.html")


@app.route('/uploadfiles', methods=['POST'])
def upload_file():
    try:
        f = request.files["myfile"]
        folder_name = request.form["crime"]
        f.save("static/" + folder_name + "/" + secure_filename(f.filename))
        print("saved")
    except Exception as e:
        print("error")
        print(e)
    return redirect("/")

@app.route("/count", methods=["GET", "POST"])
def get_count():
    if request.method == "POST":
        res = request.form.to_dict(flat=False)
        li = list(res.keys())
        count = model.get_count(li[0])
        return render_template("District.html", haveCount=True,crime=li[0], count=count)
    else:
        return render_template("District.html")


@app.route("/crimecount", methods=["GET", "POST"])
def get_crime_count():
    if request.method == "POST":
        res = request.form.to_dict(flat=False)
        li = list(res.keys())
        count = model.get_crime_count(li[0])
        return render_template("crimecount.html", haveCount=True, crime=li[0], count=count)
    else:
        return render_template("crimecount.html")



if __name__ == '__main__':
    app.run(debug=True)
