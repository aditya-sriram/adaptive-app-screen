from flask import Flask, render_template, redirect, url_for
from numpy import array_split
import pickle
import pandas as pd
import datetime
from operator import itemgetter

app = Flask(__name__)

data = {"userid1": []}

df = pd.read_json("../data analysis/outputs/process_names.json")

process_names = df["ProcessName"]
process_names_hash = process_names.map(hash)

infile = open("../data analysis/outputs/model",'rb')
model = pickle.load(infile)
infile.close()

day = datetime.datetime.today().weekday()
hour = datetime.datetime.now().hour

feature_data = df.copy()
feature_data["ProcessName"] = df["ProcessName"].map(hash)
feature_data["Day"] = day
feature_data["Hour"] = hour

labels = model.predict(feature_data)

labeled_processes = zip(process_names.values, labels)
labeled_sorted_processes = sorted(labeled_processes, key=itemgetter(1), reverse=True)
sorted_processes = list(map(lambda x: x[0], labeled_sorted_processes))

# app information generation
for process_name in sorted_processes:
    data['userid 1'].append(str(process_name))

@app.route('/')
def index():
    return 'index'

@app.route('/screen/<userid>')
def profile(userid):
    if userid in data:
        return render_template('screen.html', userid=userid, cards=array_split(data[userid], 4))
    else:
        return redirect(url_for('login'))