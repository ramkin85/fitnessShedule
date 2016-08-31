__author__ = 'ramkin85'
from app import app
from flask import render_template, request, json
from app.client import api as client_api
from app.trainer import api as trainer_api
from app.lesson import api as lesson_api


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    # return 'hello world'
    return render_template('index.html', title='Расписание')


@app.route('/api/trainer', methods=['POST'])
def trainer():
    app.logger.debug('_cached_json = %s' % request.is_xhr)
    app.logger.debug('_cached_json = %s' % request.get_json())
    app.logger.debug('data = %s' % request.data)
    app.logger.debug('args = %s' % request.args)
    # return trainer_api(request)
    return trainer_api(request)


@app.route('/api/client', methods=['POST'])
def client():
    res = client_api(request)
    app.logger.debug('res = %s' % json.dumps(res))
    return res


@app.route('/api/lesson', methods=['POST'])
def lesson(request):
    return lesson_api(request)
