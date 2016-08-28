__author__ = 'ramkin85'

import logging
import json
from datetime import datetime, time

from app.models import Lesson, Trainer, LessonClient, Client
from app.client import ClientApi

logger = logging.getLogger('django')


def api(request):

    requestBody = json.loads(request.body.decode('utf-8'))
    method = requestBody.get('method')
    logger.debug('testlogging method = %s' % method)
    if (method == None):
        response = FieldError('Method must be declared')
        return HttpResponse(response)

    if method == 'get_list':
        startDate = requestBody.get('startDate')
        endDate = requestBody.get('endDate')
        response = get_list(startDate, endDate)
    elif method == 'create':
        dayOfWeek = requestBody.get('DayOfWeek')
        type = requestBody.get('Type')
        startTime = requestBody.get('StartTime')
        endTime = requestBody.get('EndTime')
        trainer = requestBody.get('Trainer')
        placesCount = requestBody.get('PlacesCount')
        startDate = requestBody.get('StartDate')
        endDate = requestBody.get('EndDate')
        active = requestBody.get('Active')
        response = create(dayOfWeek, type, startTime, endTime, trainer, placesCount, startDate, endDate, active)
    elif method == 'update':
        id = requestBody.get('ID')
        name = requestBody.get('Name')
        phone = requestBody.get('Phone')
        response = update(id, name, phone)
    elif method == 'delete':
        id = requestBody.get('ID')
        response = delete(id)
    elif method == 'bindClient':
        id = requestBody.get('LessonID')
        clientId = requestBody.get('ClientID')
        response = bindClient(id, clientId)
    elif method == 'unbindClient':
        id = requestBody.get('LessonID')
        clientId = requestBody.get('ClientID')
        response = unbindClient(id, clientId)
    elif method == 'vote':
        dayOfWeek = requestBody.get('DayOfWeek')
        type = requestBody.get('Type')
        startTime = requestBody.get('StartTime')
        endTime = requestBody.get('EndTime')
        trainer = requestBody.get('Trainer')
        placesCount = requestBody.get('PlacesCount')
        startDate = requestBody.get('StartDate')
        endDate = requestBody.get('EndDate')
        active = requestBody.get('Active')
        clientName = requestBody.get('ClientName')
        clientPhone = requestBody.get('ClientPhone')
        clientComment = requestBody.get('ClientComment')
        response = vote(dayOfWeek, type, startTime, endTime, trainer, placesCount,
                          startDate, endDate, active, clientName, clientPhone, clientComment)
    else:
        response = FieldError('unsapported method name "%s"' % method)

    logger.debug('response = %s' % response)

    return HttpResponse(response)


def get_list(startDate, endDate):
    result = Lesson.objects.all().select_related('Trainer').filter(StartDate__lte=endDate,
                             EndDate__gte=startDate, Active=True).select_related('Trainer').values('id', 'StartDate', 'EndDate', 'DayOfWeek',
                                                           'Type', 'StartTime', 'EndTime', 'Trainer',
                                                           'PlacesCount', 'Active', 'Trainer__Name')

    logger.debug('result = %s' % result)
    result = json.dumps({'LessonList': list(result)}, cls=DjangoJSONEncoder)
    return result


def get_by_id(id):
    lesson = Lesson.objects.get(pk=id)
    logger.debug('lesson = %s' % lesson)
    return lesson


def get_by_param(**kwargs):
    startTime = time(kwargs.get('startTime')['hours'], kwargs.get('startTime')['minutes'])
    lesson = Lesson.objects.filter(id=kwargs.get('id'), StartDate__lte=kwargs.get('startDate'),
                                StartTime=startTime, DayOfWeek=kwargs.get('dayOfWeek'),
                                State=kwargs.get('state', 'ACTIVE'))
    logger.debug('lesson = %s' % lesson)
    return lesson


def create(dayOfWeek, type, startTime, endTime, trainer, placesCount, startDate, endDate, active, state):
    if dayOfWeek is None or startTime is None or endTime is None or startDate is None:
        return FieldError('Missed required params')

    try:
        trainer = Trainer.objects.get(pk=trainer)
    except:
        trainer = None

    startTime = time(startTime['hours'], startTime['minutes'])
    endTime = time(endTime['hours'], endTime['minutes'])
    if state is None:
        state = 'ACTIVE'
    lesson = Lesson(DayOfWeek=dayOfWeek, Type=type, StartTime=startTime,
             EndTime=endTime, Trainer=trainer, PlacesCount=placesCount, StartDate=startDate, EndDate=endDate,
                    Active=active, State=state)
    lesson.save()

    return 'Lesson created successfully.'


def delete(id):
    #return 'mocked'
    if id == None:
        return FieldError('Param "id" mast be defined for method "delete"')

    lesson = Lesson.objects.get(pk=id)
    lesson.delete()

    return 'Lesson deleted successfully.'


def update(id, dayOfWeek, type, startTime, endTime, trainer, placesCount):
    lesson = Lesson.objects.get(pk=id)
    lesson.DayOfWeek = dayOfWeek
    lesson.Type = type
    lesson.StartTime = startTime
    lesson.EndTime = endTime
    lesson.Trainer = trainer
    lesson.PlacesCount = placesCount

    lesson.update()

    return 'Lesson updated successfully.'


def bindClient(id, clientId):
    lesson = Lesson.objects.get(id=id)
    client = Client.objects.get(id=clientId)
    lessonClient = LessonClient(Lesson=lesson, Client=client)
    lessonClient.save()

    return 'Client binded to lesson successfully.'

def unbindClient(id, clientId):
    lesson = Lesson.objects.get(id=id)
    client = Client.objects.get(id=clientId)
    lessonClient = LessonClient(Lesson=lesson, Client=client)
    lessonClient.delete()

    return 'Client unbinded from lesson successfully.'


def vote(dayOfWeek, type, startTime, endTime, trainer, placesCount,
                          startDate, endDate, active, clientName, clientPhone, clientComment):
    if dayOfWeek is None or startTime is None or endTime is None or startDate is None\
            or clientName is None or clientPhone is None:
        return FieldError('Missed required params')

    lesson = get_by_param(startDate=startDate, startTime=startTime, dayOfWeek=dayOfWeek, state='VOTING')
    if lesson.__len__() == 0:
        lesson = create(dayOfWeek, 'group', startTime, endTime, trainer, placesCount,
                          startDate, endDate, False, 'VOTING')

    client = ClientApi.create(clientName, clientPhone, clientComment, 'POTENCIAL')

    bindClient(lesson.id, client.id)

    return 'Lesson created successfully.'