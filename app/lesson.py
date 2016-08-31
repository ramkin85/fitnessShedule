__author__ = 'ramkin85'
from app import app,db
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
        response = bind_client(id, client_id)
    elif method == 'unbindClient':
        id = request_body.get('LessonID')
        client_id = request_body.get('ClientID')
        response = unbind_client(id, client_id)
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
        .select_related('Trainer')
    # result = Lesson.query.all().select_related('Trainer')\
    #     .filter(StartDate__lte=end_date, EndDate__gte=start_date, Active=True)\
    #     .select_related('Trainer').values('id', 'StartDate', 'EndDate', 'DayOfWeek', 'Type', 'StartTime', 'EndTime',
    #                                       'Trainer', 'PlacesCount', 'Active', 'Trainer__Name')
    app.logger.debug('result = %s' % result)
    result = json.dumps({'LessonList': list_from_query(result)})
    return result


def get_by_id(id):
    lesson = Lesson.qyery.get(id)
    app.logger.debug('lesson = %s' % lesson)
    return lesson


def get_by_param(**kwargs):
    start_time = time(kwargs.get('startTime')['hours'], kwargs.get('startTime')['minutes'])
    lesson = Lesson.qyery.filter(id=kwargs.get('id'), StartDate__lte=kwargs.get('startDate'),
                                StartTime=start_time, DayOfWeek=kwargs.get('dayOfWeek'),
                                State=kwargs.get('state', 'ACTIVE'))
    app.logger.debug('lesson = %s' % lesson)
    return lesson


def create(day_of_week, type, start_time, end_time, trainer_id, places_count, start_date, end_date, active, state):
    if day_of_week is None or start_time is None or end_time is None or start_date is None:
        resp_message('ERROR', 'Missed required params')

    start_time = time(start_time['hours'], start_time['minutes'])
    end_time = time(end_time['hours'], end_time['minutes'])
    if state is None:
        state = 'ACTIVE'
    lesson = Lesson(day_of_week=day_of_week, type=type, start_time=start_time,
                    end_time=end_time, trainer_id=trainer_id, places_count=places_count, start_date=start_date, end_date=end_date,
                    active=active, state=state)
    db.session.add(lesson)
    db.session.commit()
    return 'Lesson created successfully.'


def delete(id):
    if id is None:
        return resp_message('ERROR', 'Param "id" mast be defined for method "delete"')
    lesson = Lesson.qyery.get(id)
    db.session.delete(lesson)
    db.session.commit()
    return 'Lesson deleted successfully.'


def update(id, day_of_week, type, start_time, end_time, trainer, places_count):
    lesson = Lesson.qyery.get(id)
    lesson.DayOfWeek = day_of_week
    lesson.Type = type
    lesson.StartTime = start_time
    lesson.EndTime = end_time
    lesson.Trainer = trainer
    lesson.PlacesCount = places_count
    db.session.update(lesson)
    db.session.commit()
    return 'Lesson updated successfully.'


def bind_client(id, client_id):
    lesson = Lesson.qyery.get(id=id)
    client = Client.qyery.get(id=client_id)
    lesson_client = LessonClient(lesson=lesson, client=client)
    db.session.add(lesson_client)
    db.session.commit()
    return 'Client binded to lesson successfully.'


def unbind_client(id, clientId):
    lesson = Lesson.qyery.get(id=id)
    client = Client.qyery.get(id=clientId)
    lesson_client = LessonClient(lesson=lesson, client=client)
    db.session.delete(lesson_client)
    db.session.commit()
    return 'Client unbinded from lesson successfully.'


def vote(day_of_week, type, start_time, end_time, trainer, places_count, start_date, end_date, active, client_name,
         client_phone, client_comment):
    if day_of_week is None or start_time is None or end_time is None or start_date is None\
            or client_name is None or client_phone is None:
        return resp_message('ERROR', 'Missed required params')
    lesson = get_by_param(startDate=start_date, startTime=start_time, dayOfWeek=day_of_week, state='VOTING')
    if lesson.__len__() == 0:
        lesson = create(day_of_week, 'group', start_time, end_time, trainer, places_count,
                        start_date, end_date, False, 'VOTING')
    client = ClientApi.create(client_name, client_phone, client_comment, 'POTENCIAL')
    bind_client(lesson.id, client.id)
    return 'Lesson created successfully.'
