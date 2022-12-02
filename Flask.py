from flask import Flask, request, render_template
from utils import load_candidates_from_json


app = Flask(__name__)

@app.route("/")
def all_cand():

    return render_template('list.html', items=load_candidates_from_json())


@app.route("candidate/<x>")
def single_cand(x):

    return render_template('single.html', items=load_candidates_from_json())

app.run()