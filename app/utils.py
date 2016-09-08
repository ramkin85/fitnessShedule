from flask import json


def resp_message(type='ERROR', message=''):
    return json.dumps({'STATUS': type, 'MESSAGE': message})


def list_from_query(result, fields):
    res_list = []
    for i in range(0, result.__len__()):
        item = result[i]
        map = {}
        for key in fields:
            key_ar = key.split('.')
            param_name = key.replace('.', '_')
            value = item
            for k in key_ar:
                value = value[k]
            map[param_name] = value
        res_list.append(map)
    return res_list
