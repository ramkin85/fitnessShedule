__author__ = 'ramkin85'
from app import app, db
from flask import json
from app.utils import resp_message, list_from_query
from app.models import Trainer


def api(request):
    request_body = json.loads(request.data.decode('utf-8'))
    #request_body = request.get_json()
    app.logger.debug('request_body = %s' % request_body)
    method = request_body.get('method')
    app.logger.debug('testlogging method = %s' % method)
    if (method == None):
        return resp_message('ERROR', 'Method must be declared')
    if method == 'get_list':
        response = TrainerApi.get_list()
    elif method == 'create':
        name = request_body.get('Name')
        foto = request_body.get('Foto')
        info = request_body.get('Info')
        response = TrainerApi.create(name, foto, info)
    elif method == 'update':
        id = request_body.get('ID')
        name = request_body.get('Name')
        foto = request_body.get('Foto')
        info = request_body.get('Info')
        response = TrainerApi.update(id, name, foto, info)
    elif method == 'delete':
        id = request_body.get('ID')
        response = TrainerApi.delete(id)
    else:
        response = resp_message('ERROR', 'unsupported method name "%s"' % method)
    app.logger.debug('response = %s' % response)
    return response


class TrainerApi(Trainer):
    @staticmethod
    def get_list():
        trainer_query_all = Trainer.query.all()
        trainer_list = list_from_query(trainer_query_all, ['id', 'Name', 'Foto', 'Info'])
        app.logger.debug('result = %s' % trainer_list)
        result = json.dumps({'TrainerList': trainer_list})
        return result

    def get_by_id(id):
        trainer = Trainer.query.get(id)
        app.logger.debug('trainer = %s' % trainer)
        return trainer

    def create(name, foto, info):
        app.logger.debug('create name = %s' % name)
        if name is None:
            return resp_message('ERROR', 'Param "name" mast be defined for method "create"')

        trainer = Trainer(name=name, info=info, foto=foto)
        db.session.add(trainer)
        db.session.commit()
        return resp_message('SUCCESS', 'Trainer %s successfully added' % name)

    def delete(id):
        if id is None:
            return resp_message('ERROR', 'Param "id" mast be defined for method "delete"')

        trainer = Trainer.query.get(id)
        db.session.delete(trainer)
        db.session.commit()
        return resp_message('SUCCESS', 'Trainer deleted successfully.')

    def update(id, name, foto, info):
        trainer = Trainer.query.get(id)
        trainer.Name = name
        trainer.Foto = foto
        trainer.Info = info
        db.session.add(trainer)
        db.session.commit()

        return 'OK'
