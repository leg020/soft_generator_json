from flask import Flask, render_template, redirect, url_for, request, session
import os
from fixture.db import DataBase
from model.db_answer import Tasks, Settings

flask = Flask(__name__)
flask.secret_key = os.urandom(24)
result = None
test_info = Tasks(test_id=1, name='Это тест', setting_id=1, description='Это путь', ip_recipient='ip', port_recipient=1234)
test_settings = Settings(setting_id=1, target='sdfdsf/dfssdf/sdfdsfd', scaner_port='COM20', scaner_boundrate=57600)



@flask.route('/', methods=["GET"])
def get_main_page():
    session.pop('edit_data', None)
    tests = get_data_for_main_page()
    return render_template('main.html', data=tests, result=result)


@flask.route('/', methods=["POST"])
def post_main_page():
    if request.form['operation'] == 'start':
        a = request.form['data']
    elif request.form['operation'] == 'get_log':
        a = request.form['data']
    elif request.form['operation'] == 'delete':
        a = request.form['data']
    elif request.form['operation'] == 'edit':
        session['edit_data'] = request.form['data']
        return redirect(url_for('get_edit_test_page'))
    return redirect(url_for('get_main_page'))

@flask.route('/edit_test', methods=["GET"])
def get_edit_test_page():
    db = DataBase(host='127.0.0.1', name='tests', user='root', password='')
    test_info = db.get_test_by_id(id=session['edit_data'])[0]
    test_settings = db.get_settings_by_id(id=test_info.setting_id)[0]
    return get_new_test_page(test_info, test_settings)

@flask.route('/new_test', methods=["GET"])
def get_new_test_page():
    session.pop('edit_data', None)
    return get_new_test_page(Tasks(), Settings())

def get_new_test_page(test_info, test_settings):
    return render_template('new_test.html', test_info=test_info, test_settings=test_settings)

def get_data_for_main_page():
    db = DataBase(host='127.0.0.1', name='tests', user='root', password='')
    data = db.get_tests()
    return data








if __name__ == '__main__':
    flask.run(host="127.0.0.1", port="7000", debug=True, threaded=True, use_reloader=False)


# Требуется под основными настройками добавить клавишу Сооздать после зоздания мы получим id теста который можно будет скрытно добавить к документам и по ним отображать меню добавления документов