__author__ = 'ramkin85'
from app import app,db,customserializer
from flask import json
from datetime import time
from app.models import Lesson, Trainer, LessonClient, Client
from app.client import ClientApi
from app.utils import resp_message, list_from_query
from app.emails import admin_notification


def api(request):
    request_body = json.loads(request.data.decode('utf-8'))
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
        mode = request_body.get('mode')
        response = vote(day_of_week, type, start_time, end_time, trainer, places_count,
                        start_date, end_date, active, client_name, client_phone, client_comment, mode)
    else:
        response = resp_message('ERROR', 'unsupported method name "%s"' % method)
    app.logger.debug('response = %s' % response)
    return response


def get_list(start_date, end_date):
    result = Lesson.query.filter(Lesson.StartDate<=end_date, Lesson.EndDate>=start_date, Lesson.Active==True).all()
    app.logger.debug('result = %s' % result)
    result = {'LessonList': list_from_query(result,['id', 'StartDate', 'EndDate', 'DayOfWeek', 'Type', 'StartTime',
                                                    'EndTime', 'PlacesCount', 'Active', 'Trainer.Name'])}
    result = json.dumps(result, default=customserializer.to_json)
    return result


def get_by_id(id):
    lesson = Lesson.query.get(id)
    app.logger.debug('lesson = %s' % lesson)
    return lesson


def get_by_param(**kwargs):
    start_time = time(kwargs.get('startTime')['hours'], kwargs.get('startTime')['minutes'])
    lesson = Lesson.query.filter(Lesson.StartDate<=kwargs.get('startDate'),
                                 Lesson.StartTime==start_time, Lesson.DayOfWeek==str(kwargs.get('dayOfWeek')),
                                 Lesson.State==kwargs.get('state', 'ACTIVE')).all()
    app.logger.debug('lesson = %s' % lesson)
    return lesson


def create(day_of_week, type, start_time, end_time, trainer_id, places_count, start_date, end_date, active, state='ACTIVE'):
    try:
        if day_of_week is None or start_time is None or end_time is None or start_date is None:
            resp_message('ERROR', 'Missed required params')

        start_time = time(start_time['hours'], start_time['minutes'])
        end_time = time(end_time['hours'], end_time['minutes'])
        lesson = Lesson(day_of_week=day_of_week, type=type, start_time=start_time,
                        end_time=end_time, trainer_id=trainer_id, places_count=places_count, start_date=start_date, end_date=end_date,
                        active=active, state=state)
        db.session.add(lesson)
        db.session.commit()
        return {'status': 'OK', 'message': 'Lesson created successfully.', 'lesson': lesson}
    except Exception:
        return {'status': 'ERROR', 'message': 'En error ocured while lesson create.', 'error': Exception}


def delete(id):
    if id is None:
        return resp_message('ERROR', 'Param "id" mast be defined for method "delete"')
    lesson = Lesson.query.get(id)
    db.session.delete(lesson)
    db.session.commit()
    return 'Lesson deleted successfully.'


def update(id, day_of_week, type, start_time, end_time, trainer, places_count):
    lesson = Lesson.query.get(id)
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
    lesson_client = LessonClient(lesson=id, client=client_id)
    db.session.add(lesson_client)
    db.session.commit()
    return 'Client binded to lesson successfully.'


def unbind_client(id, client_id):
    lesson_client = LessonClient(lesson=id, client=client_id)
    db.session.delete(lesson_client)
    db.session.commit()
    return 'Client unbinded from lesson successfully.'


def vote(day_of_week, type, start_time, end_time, trainer, places_count, start_date, end_date, active, client_name,
         client_phone, client_comment, mode='FULL'):
    if mode == 'SIMPLE':
        admin_notification()
    else:
        if day_of_week is None or start_time is None or end_time is None or start_date is None\
                or client_name is None or client_phone is None:
            return resp_message('ERROR', 'Missed required params')
        lesson_list = get_by_param(startDate=start_date, startTime=start_time, dayOfWeek=day_of_week, state='VOTING')
        if lesson_list.__len__() == 0:
            lesson = create(day_of_week, type, start_time, end_time, trainer, places_count,
                            start_date, end_date, False, 'VOTING').get('lesson')
        else:
            lesson = lesson_list[0]
        client = ClientApi.create(client_name, client_phone, client_comment, 'POTENCIAL').get('client')
        if lesson is not None and client is not None:
            bind_client(lesson.id, client.id)
            return 'Lesson created successfully.'
