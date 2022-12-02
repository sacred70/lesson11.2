from flask import Flask, request, render_template
from utils import load_candidates_from_json
from utils import get_candidate
print(get_candidate(4)['name'])
app = Flask(__name__)

@app.route("/")
def all_cand():

    return render_template('list.html', items=load_candidates_from_json())


@app.route("/candidate/<x>")
def single_cand(x):
    name = get_candidate(x)[0]
    position = get_candidate(x)[1]
    picture = get_candidate(x)[2]
    skills = get_candidate(x)[3]

    return render_template('single.html',
                           name=name,
                           position=position,
                           picture=picture,
                           skills=skills)

app.run()