from flask import Flask, render_template, redirect, url_for, request, session
import os
from fixture.db import DataBase
from model.db_answer import Tasks, Settings, Documents, Positions
from model.model_builder import ModelBuilder


flask = Flask(__name__)
flask.secret_key = os.urandom(24)
result = None



@flask.route('/', methods=["GET"])
def get_main_page():
    session['test_id'] = 'new'
    db = DataBase(host='127.0.0.1', name='tests', user='root', password='')
    tests = db.get_tests()
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
        session['test_id'] = request.form['data']
        return redirect(url_for('get_edit_page', document_id='new'))
    return redirect(url_for('get_main_page'))


def new_test_page(test_id=None, document_id=None):
    db = DataBase(host='127.0.0.1', name='tests', user='root', password='')
    if test_id != None:
        test_info = db.get_tests(id=test_id)[0]
        test_settings = db.get_settings(id=test_info.setting_id)[0]
        documents = db.get_documents(test_id=test_info.test_id)
    else:
        test_info = {}
        test_settings = {}
        documents = []

    if document_id != None:
        doc = db.get_documents(document_id=document_id)
        positions = db.get_positions_by_document_id(document_id=document_id)
        if len(doc) == 0:
            doc = {}
        else:
            doc = doc[0]

        if len(positions) == 0:
            positions = []
    else:
        doc = {}
        positions = []

    return render_template('new_test.html', test_info=test_info, test_settings=test_settings, documents=documents, doc=doc, positions=positions)


@flask.route('/new_test_page', methods=['GET'])
def get_new_test_page():
    return new_test_page()


@flask.route('/new_test_page', methods=['POST'])
def post_new_test_page():
    model_builder = ModelBuilder(form=request.form)
    settings = model_builder.convert_in_settings()
    db = DataBase(host='127.0.0.1', name='tests', user='root', password='')
    setting_id = db.insert_in_to_settings(settings)
    tests = model_builder.convert_in_tasks(setting_id=setting_id)
    test_id = db.insert_in_to_tests(tests)
    session['test_id'] = test_id
    return redirect(url_for('get_edit_page', document_id='new'))


@flask.route('/test_redactor_<document_id>', methods=["GET"])
def get_edit_page(document_id):
    try:
        test_id = session['test_id']
    except:
        return redirect(url_for('get_main_page'))


    if document_id == 'new':
        document_id = None
    return new_test_page(test_id=test_id, document_id=document_id)


@flask.route('/test_redactor_<document_id>', methods=["POST"])
def post_edit_page(document_id):
    db = DataBase(host='127.0.0.1', name='tests', user='root', password='')
    model_builder = ModelBuilder(form=request.form)
    if request.form['document_operation'] == 'edit_settings':
        settings = model_builder.convert_in_settings()
        tests = model_builder.convert_in_tasks()
        setting_id = db.update_settins_by_id(settings)
        session['test_id'] = db.update_tests_by_id(tests)

    if request.form['document_operation'] == 'add':
        document = model_builder.convert_in_documents()
        document_id = db.insert_in_to_documents(documents=document)

    if request.form['document_operation'] == 'edit':
        document = model_builder.convert_in_documents(document_id=document_id)
        document_id = db.update_documents_by_id(document=document)

    if request.form['document_operation'] == 'delete':
        pass

    if request.form['document_operation'] == 'add_position':
        position = model_builder.convert_in_positions(document_id=document_id)
        position_id = db.insert_in_to_poositions(position=position)

    if request.form['document_operation'] == 'edit_position':
        pass

    if request.form['document_operation'] == 'delete_position':
        pass

    return redirect(url_for('get_edit_page', document_id=document_id))





if __name__ == '__main__':
    flask.run(host="127.0.0.1", port="7000", debug=True, threaded=True, use_reloader=False)