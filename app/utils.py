from flask import json


def resp_message(type='ERROR', message=''):
    return json.dumps({'STATUS': type, 'MESSAGE': message})


def list_from_query(result, fields):
    res_list = []
    for i in range(0, result.__len__()):
        item = result[i]
        res_list.append({key: item[key] for key in fields})
    return res_list