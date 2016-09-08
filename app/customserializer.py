import datetime


def to_json(python_object):
    if isinstance(python_object, datetime.time):
        hours = str(python_object.hour)
        minutes = str(python_object.minute)
        return {'hours': hours,
                'minutes': minutes}
    raise TypeError(repr(python_object) + 'is not JSON serializable')
