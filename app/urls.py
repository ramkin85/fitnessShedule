__author__ = 'ramkin85'

from backEnd.app import views
from django.conf.urls import url
from shedule import client, trainer, lesson

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/client$', client.api, name='client_api'),
    url(r'^api/trainer$', trainer.api, name='trainer_api'),
    url(r'^api/lesson$', lesson.api, name='lesson_api'),
]