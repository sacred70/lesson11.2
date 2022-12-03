from flask import Flask, request, render_template
from utils import load_candidates_from_json
from utils import get_candidate
from utils import get_candidates_by_name

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

"""
@app.route("/search/<candidate_name>")
def search(candidate_name):
    count = int((len(get_candidates_by_name(candidate_name))) / 2)
    if count == 0:
        return render_template("no_cand.html")
    else:

        if count < 4:
            id = get_candidates_by_name(candidate_name)["id"]
            name = get_candidates_by_name(candidate_name)["name"]
            return render_template("search_1.html", count=count, id=id, name=name)
        else:

            return render_template("search_0.html", count=count, items=get_candidates_by_name(candidate_name))
"""

@app.route("/search/<candidate_name>")
def search(candidate_name):
    count = int(len(get_candidates_by_name(candidate_name)))
    return render_template("search.html", count=count, items=get_candidates_by_name(candidate_name))


@app.route("/skill/<skill_name>")
def search_skill(skill_name):
    pass



app.run()