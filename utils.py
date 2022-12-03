# coding: utf8
import json


def load_candidates(file="candidates.json"):
    # загрузит данные из файла
    with open(file, "r", encoding='utf-8') as f:
        text = json.load(f)
        return text


def load_candidates_from_json(path=load_candidates()):
    #  возвращает список всех кандидатов
    list_cand = {}
    for cand in load_candidates():
        list_cand[cand["id"]] = cand["name"]
    return list_cand


def get_candidate(candidate_id):
    #  возвращает одного кандидата по его id
    for cand in load_candidates():
        if cand['id'] == candidate_id:
            return cand


def get_candidates_by_name(candidate_name):
    # возвращает кандидатов по имени
    list_cand = {}
    for cand in load_candidates():
        if candidate_name.lower() in cand['name'].lower():
            list_cand[cand["id"]] = cand["name"]
    return list_cand


def get_candidates_by_skill(skill_name):
    #  возвращает кандидатов по навыку
    list_cand = {}
    skill = skill_name.lower()
    for cand in load_candidates():
        if skill in cand['skills'].lower():
            list_cand[cand["id"]] = cand["name"]
    return list_cand

