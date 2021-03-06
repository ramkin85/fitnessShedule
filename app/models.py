from app import db
from sqlalchemy import Column


# Create your models here.

class Client(db.Model):
    id = Column(db.Integer, primary_key=True)
    Name = Column(db.String(200), unique=True)
    Phone = Column(db.String(15), unique=True)
    Comment = Column(db.String(400), unique=False, nullable=True)
    State = Column(db.String(15), unique=False, default='ACTIVE')

    def __init__(self, Name, Phone, Comment='', State='ACTIVE'):
        self.Name = Name
        self.Phone = Phone
        self.Comment = Comment
        self.State = State

    def __repr__(self):
        return '{Name: %r}' % (self.Name)

    def __getitem__(self, key):
        if key == 'id':
            return self.id
        elif key == 'Name':
            return self.Name
        elif key == 'Phone':
            return self.Phone
        elif key == 'Comment':
            return self.Comment
        elif key == 'State':
            return self.State
        else:
            return None


class Trainer(db.Model):
    id = Column(db.Integer, primary_key=True)
    Name = Column(db.String(200), unique=True)
    Info = Column(db.String(2000))
    Foto = Column(db.String())

    def __init__(self, name, info, foto=None):
        self.Name = name
        self.Info = info
        self.Foto = foto

    def __repr__(self):
        return '{Trainer Name: %r}' % self.Name

    def __getitem__(self, key):
        if key == 'id':
            return self.id
        elif key == 'Name':
            return self.Name
        elif key == 'Info':
            return self.Info
        elif key == 'Foto':
            return self.Foto
        else:
            return None


class Lesson(db.Model):
    id = Column(db.Integer, primary_key=True)
    DayOfWeek = Column(db.String(20))
    Type = Column(db.String(20))
    StartTime = Column(db.Integer)
    EndTime = Column(db.Integer)
    TrainerId = Column(db.Integer, db.ForeignKey('trainer.id'))
    PlacesCount = Column(db.Integer)
    StartDate = Column(db.Integer)
    EndDate = Column(db.Integer)
    Active = Column(db.Boolean())
    State = Column(db.String(20))
    Trainer = db.relationship('Trainer', backref=db.backref('Lessons', lazy='dynamic'))

    def __init__(self, day_of_week, type, start_time, end_time, trainer_id, places_count, start_date, end_date, active, state):
        self.DayOfWeek = day_of_week
        self.Type = type
        self.StartTime = start_time
        self.EndTime = end_time
        self.TrainerId = trainer_id
        self.PlacesCount = places_count
        self.StartDate = start_date
        self.EndDate = end_date
        self.Active = active
        self.State = state

    def __repr__(self):
        return '{Lesson DayOfWeek: %r}' % self.DayOfWeek

    def __getitem__(self, key):
        if key == 'id':
            return self.id
        elif key == 'DayOfWeek':
            return self.DayOfWeek
        elif key == 'Type':
            return self.Type
        elif key == 'StartTime':
            return self.StartTime
        elif key == 'EndTime':
            return self.EndTime
        elif key == 'Trainer':
            return self.Trainer
        elif key == 'PlacesCount':
            return self.PlacesCount
        elif key == 'StartDate':
            return self.StartDate
        elif key == 'EndDate':
            return self.EndDate
        elif key == 'Active':
            return self.Active
        elif key == 'State':
            return self.State
        else:
            return None


class LessonClient(db.Model):
    id = Column(db.Integer(), primary_key=True)
    Client = Column(db.Integer, db.ForeignKey('client.id'))
    Lesson = Column(db.Integer, db.ForeignKey('lesson.id'))

    def __init__(self, client, lesson):
        self.Client = client
        self.Lesson = lesson

    def __repr__(self):
        return '{LessonClient Lesson: %r}' % self.Lesson

    def __getitem__(self, key):
        if key == 'id':
            return self.id
        elif key == 'Client':
            return self.Client
        elif key == 'Lesson':
            return self.Lesson
        else:
            return None