# coding: utf8
import json


def load_candidates(file="candidates.json"):
    # загрузит данные из файла
    with open(file, "r", encoding='utf-8') as f:
        text = json.load(f)
        return text


#print(load_candidates())


def load_candidates_from_json(path):
    #  возвращает список всех кандидатов
    list_cand = f'< h1 > Все кандидаты < / h1 >\n'


def get_candidate(candidate_id):
    # возвращает одного кандидата по его id
    pass


def get_candidates_by_name(candidate_name):
    # возвращает кандидатов по имени
    pass

def get_candidates_by_skill(skill_name):
    #  возвращает кандидатов по навыку
    pass

