from flask import Flask, render_template, redirect, url_for, request
from fixture.db import DataBase

flask = Flask(__name__)
result = 'Приветики а вот и результаты'


@flask.route('/', methods=["GET"])
def get_main_page():
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
        a = request.form['data']
    return redirect(url_for('get_main_page'))


@flask.route('/new_test', methods=["GET"])
def get_new_test_page():
    return render_template('new_test.html')


def get_data_for_main_page():
    db = DataBase(host='127.0.0.1', name='tests', user='root', password='')
    data = db.get_tests()
    return data




if __name__ == '__main__':
    flask.run(host="127.0.0.1", port="7000", debug=True, threaded=True, use_reloader=False)