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

@app.route("/search/<candidate_name>")
def search(candidate_name):
    count = len(get_candidates_by_name(candidate_name))
    items = get_candidates_by_name(candidate_name)
    if len(get_candidates_by_name(candidate_name)) <1 :
        return '<h1>"Кандидата с таким именем не найдено"</h1>'
    else:
        return render_template("search.html", count=count, items=items)


app.run()