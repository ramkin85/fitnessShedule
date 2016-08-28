__author__ = 'ramkin85'
from app import app, db
from app.models import Client
from pprint import pprint
from flask import json, jsonify
from app.utils import resp_message, list_from_query


def api(request):
    request_body = json.loads(request.data.decode('utf-8'))
    method = request_body.get('method')
    app.logger.debug('request_body = %s' % request_body)
    app.logger.debug('testlogging method = %s' % method)
    if method is None:
        response = resp_message('ERROR', 'Method must be declared')
    elif method == 'get_list':
        response = ClientApi.get_list()
    elif method == 'create':
        name = request_body.get('Name')
        phone = request_body.get('Phone')
        comment = request_body.get('Comment')
        response = ClientApi.create(name, phone, comment, 'ACTIVE')
    elif method == 'update':
        id = request_body.get('id')
        name = request_body.get('Name')
        phone = request_body.get('Phone')
        comment = request_body.get('Comment')
        response = ClientApi.update(id, name, phone, comment)
    elif method == 'delete':
        id = request_body.get('id')
        response = ClientApi.remove(id)
    else:
        response = resp_message('ERROR', 'unsapported method name "%s"' % method)

    app.logger.debug('response = %s' % response)

    return response


class ClientApi(Client):
    @staticmethod
    def get_list():
        client_query_all = Client.query.all()
        client_list = list_from_query(client_query_all, ['id', 'Name', 'Phone', 'Comment', 'State'])
        app.logger.debug('client_list = %s' % client_list)
        return json.dumps({'ClientList': client_list})

    def get_by_id(id):
        client = Client.query.get(id)
        app.logger.debug('client = %s' % client)
        return client

    def create(name, phone, comment='Нет данных', state='ACTIVE'):
        app.logger.debug('create date = %s' % name)
        if name is None:
            return resp_message('ERROR', 'Param "name" mast be defined for method "create"')

        client = Client(Name=name, Phone=phone, Comment=comment, State=state)
        db.session.add(client)
        db.session.commit()

        return resp_message('SUCCESS', 'Client created successfully.')

    def remove(id):
        if id is None:
            return resp_message('ERROR', 'Param "id" mast be defined for method "delete"')

        client = Client.query.get(id)
        db.session.delete(client)
        db.session.commit()

        return resp_message('SUCCESS', 'Client deleted successfully.')

    def update(id, name, phone, comment=''):
        client = Client.query.get(id)
        client.Name = name
        client.Phone = phone
        client.Comment = comment
        db.session.add(client)
        db.session.commit()

        return resp_message('SUCCESS', 'Client updated successfully.')
