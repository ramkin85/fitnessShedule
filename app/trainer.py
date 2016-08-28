__author__ = 'ramkin85'

#from django.template import RequestContext
#from django.shortcuts import render_to_response
#from django.http.response import HttpResponse
#from django.core.exceptions import FieldError
import logging
#from django.core.serializers.json import DjangoJSONEncoder
import json

#from shedule.models import Trainer

logger = logging.getLogger('django')

#class Trainer():

def api(request):

    requestBody = json.loads(request.args.decode('utf-8'))
    # requestBody = json.loads(request.body.decode('utf-8'))
    logger.debug('requestBody = %s' % requestBody)
    method = requestBody.get('method')
    logger.debug('testlogging method = %s' % method)
    if (method == None):
        response = FieldError('Method must be declared')
        return HttpResponse(response)

    if method == 'get_list':
        response = get_list()
    elif method == 'create':
        name = requestBody.get('Name')
        foto = requestBody.get('Foto')
        info = requestBody.get('Info')
        response = create(name, foto, info)
    elif method == 'update':
        id = requestBody.get('ID')
        name = requestBody.get('Name')
        foto = requestBody.get('Foto')
        info = requestBody.get('Info')
        response = update(id, name, foto, info)
    elif method == 'delete':
        id = requestBody.get('ID')
        response = delete(id)
    else:
        response = FieldError('unsapported method name "%s"' % method)

    logger.debug('response = %s' % response)

    return HttpResponse(response)


def get_list():
    result = Trainer.objects.all().values('id', 'Name', 'Foto', 'Info')
    logger.debug('result = %s' % result)
    result = json.dumps({'TrainerList': list(result)}, cls=DjangoJSONEncoder)
    return result


def get_by_id(id):
    trainer = Trainer.objects.get(pk=id)
    logger.debug('trainer = %s' % trainer)
    return trainer


def create(name, foto, info):
    logger.debug('create name = %s' % name)
    if (name == None):
        return FieldError('Param "name" mast be defined for method "create"')

    trainer = Trainer(Name=name, Foto=foto, Info=info)
    trainer.save()

    return None


def delete(id):
    #return 'mocked'
    if id == None:
        return FieldError('Param "id" mast be defined for method "delete"')

    trainer = Trainer.objects.get(pk=id)
    trainer.delete()

    return 'Clent deleted successfully.'


def update(id, name, foto, info):
    trainer = Trainer.objects.get(pk=id)
    trainer.Name = name
    trainer.Foto = foto
    trainer.Info = info
    trainer.update()

    return 'OK'