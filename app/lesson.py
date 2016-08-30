__author__ = 'ramkin85'
from app import app
from flask import json
from datetime import time
from app.models import Lesson, Trainer, LessonClient, Client
from app.client import ClientApi
from app.utils import resp_message, list_from_query


def api(request):
    request_body = json.loads(request.body.decode('utf-8'))
    method = request_body.get('method')
    app.logger.debug('testlogging method = %s' % method)
    if method is None:
        return resp_message('ERROR', 'Method must be declared')
    elif method == 'get_list':
        start_date = request_body.get('startDate')
        end_date = request_body.get('endDate')
        response = get_list(start_date, end_date)
    elif method == 'create':
        day_of_week = request_body.get('DayOfWeek')
        type = request_body.get('Type')
        start_time = request_body.get('StartTime')
        end_time = request_body.get('EndTime')
        trainer = request_body.get('Trainer')
        places_count = request_body.get('PlacesCount')
        start_date = request_body.get('StartDate')
        end_date = request_body.get('EndDate')
        active = request_body.get('Active')
        response = create(day_of_week, type, start_time, end_time, trainer, places_count, start_date, end_date, active)
    elif method == 'update':
        id = request_body.get('ID')
        name = request_body.get('Name')
        phone = request_body.get('Phone')
        response = update(id, name, phone)
    elif method == 'delete':
        id = request_body.get('ID')
        response = delete(id)
    elif method == 'bindClient':
        id = request_body.get('LessonID')
        client_id = request_body.get('ClientID')
        response = bindClient(id, client_id)
    elif method == 'unbindClient':
        id = request_body.get('LessonID')
        client_id = request_body.get('ClientID')
        response = unbindClient(id, client_id)
    elif method == 'vote':
        day_of_week = request_body.get('DayOfWeek')
        type = request_body.get('Type')
        start_time = request_body.get('StartTime')
        end_time = request_body.get('EndTime')
        trainer = request_body.get('Trainer')
        places_count = request_body.get('PlacesCount')
        start_date = request_body.get('StartDate')
        end_date = request_body.get('EndDate')
        active = request_body.get('Active')
        client_name = request_body.get('ClientName')
        client_phone = request_body.get('ClientPhone')
        client_comment = request_body.get('ClientComment')
        response = vote(day_of_week, type, start_time, end_time, trainer, places_count,
                        start_date, end_date, active, client_name, client_phone, client_comment)
    else:
        response = resp_message('ERROR', 'unsupported method name "%s"' % method)
    app.logger.debug('response = %s' % response)
    return response


def get_list(start_date, end_date):
    result = Lesson.query.filter_by(StartDate__lte=end_date, EndDate__gte=start_date, Active=True).all()\
        .select_related('Trainer').values('id', 'StartDate', 'EndDate', 'DayOfWeek', 'Type', 'StartTime', 'EndTime',
                                          'Trainer', 'PlacesCount', 'Active', 'Trainer__Name')
    # result = Lesson.query.all().select_related('Trainer')\
    #     .filter(StartDate__lte=end_date, EndDate__gte=start_date, Active=True)\
    #     .select_related('Trainer').values('id', 'StartDate', 'EndDate', 'DayOfWeek', 'Type', 'StartTime', 'EndTime',
    #                                       'Trainer', 'PlacesCount', 'Active', 'Trainer__Name')
    app.logger.debug('result = %s' % result)
    result = json.dumps({'LessonList': list_from_query(result)})
    return result


def get_by_id(id):
    lesson = Lesson.objects.get(pk=id)
    app.logger.debug('lesson = %s' % lesson)
    return lesson


def get_by_param(**kwargs):
    startTime = time(kwargs.get('startTime')['hours'], kwargs.get('startTime')['minutes'])
    lesson = Lesson.objects.filter(id=kwargs.get('id'), StartDate__lte=kwargs.get('startDate'),
                                StartTime=startTime, DayOfWeek=kwargs.get('dayOfWeek'),
                                State=kwargs.get('state', 'ACTIVE'))
    app.logger.debug('lesson = %s' % lesson)
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