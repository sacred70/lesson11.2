from flask import Flask, render_template
from utils import load_candidates_from_json
from utils import get_candidate
from utils import get_candidates_by_name
from utils import get_candidates_by_skill

app = Flask(__name__)


@app.route("/")
def all_cand():

    return render_template('list.html', items=load_candidates_from_json())


@app.route("/candidate/<int:x>")
def single_cand(x):
    name = get_candidate(x)["name"]
    position = get_candidate(x)["position"]
    picture = get_candidate(x)["picture"]
    skills = get_candidate(x)["skills"]

    return render_template('single.html',
                           name=name,
                           position=position,
                           picture=picture,
                           skills=skills)


@app.route("/search/<candidate_name>")
def search(candidate_name):
    count = int(len(get_candidates_by_name(candidate_name)))
    return render_template("search.html", count=count, items=get_candidates_by_name(candidate_name))


@app.route("/skill/<skill_name>")
def search_skill(skill_name):
    count = int(len(get_candidates_by_skill(skill_name)))
    return render_template("search.html", count=count, items=get_candidates_by_skill(skill_name), skill=skill_name)


app.run()




