import pymysql.cursors
from model.db_answer import *


class DataBase:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host,
                                          database=name,
                                          user=user,
                                          password=password,
                                          autocommit=True)


    def get_data_from_db(self, text: str):
        cursor = self.connection.cursor()
        try:
            cursor.execute(text)
        finally:
            cursor.close()
        return cursor

    def check_data(self, data):
        if data.rowcount == 0:
            return -1
        else:
            return 0

    def get_tests(self, id=None):
        answer = []
        if id == None:
            data = self.get_data_from_db('select task_id, name, setting_id, description, ip_recipient, port_recipient from tasks')
        else:
            data = self.get_data_from_db('select task_id, name, setting_id, description, ip_recipient, port_recipient from tasks where task_id=%s' % id)
        check_result = self.check_data(data)
        if check_result == 0:
            for row in data:
                (test_id, name, setting_id, description, ip_recipient, port_recipient) = row
                answer.append(Tasks(test_id=test_id, name=name, setting_id=setting_id, description=description, ip_recipient=ip_recipient, port_recipient=port_recipient))
        return answer

    def get_settings(self, id=None):
        answer = []
        if id == None:
            data = self.get_data_from_db('select setting_id, target, scaner_port, scaner_boundrate, have_kassa from settings')
        else:
            data = self.get_data_from_db('select setting_id, target, scaner_port, scaner_boundrate, have_kassa from settings where setting_id=%s' % id)
        check_result = self.check_data(data)
        if check_result == 0:
            for row in data:
                (setting_id, target, scaner_port, scaner_boundrate, have_cassa) = row
                answer.append(Settings(setting_id=setting_id,
                                       target=target,
                                       scaner_port=scaner_port,
                                       scaner_boundrate=scaner_boundrate,
                                       have_cassa=have_cassa))
        return answer


    def get_documents(self, test_id=None, document_id=None):
        answer = []
        if test_id != None:
            data = self.get_data_from_db('select document_id, check_number, document_type, report_type, check_type, help_setting, type_close, sale, test_id from documents where test_id=%s' % test_id)
        elif document_id != None:
            data = self.get_data_from_db('select document_id, check_number, document_type, report_type, check_type, help_setting, type_close, sale, test_id from documents where document_id=%s' % document_id)
        else:
            data = self.get_data_from_db('select document_id, check_number, document_type, report_type, check_type, help_setting, type_close, sale, test_id from documents')
        check_result = self.check_data(data)
        if check_result == 0:
            for row in data:
                (document_id, check_number, document_type, report_type, check_type, help_setting, type_close, sale, test_id) = row
                answer.append(Documents(document_id=document_id,
                                        check_number=check_number,
                                        document_type=document_type,
                                        report_type=report_type,
                                        check_type=check_type,
                                        help_setting=help_setting,
                                        type_close=type_close,
                                        sale=sale,
                                        test_id=test_id))
        return answer

    def get_positions(self, document_id=None, position_id=None):
        answer = []
        if document_id != None:
            data = self.get_data_from_db('select position_id, place_in_list, count, need_mark, mark, document_id from positions where document_id=%s' % document_id)
        elif position_id != None:
            data = self.get_data_from_db('select position_id, place_in_list, count, need_mark, mark, document_id from positions where position_id=%s' % position_id)
        else:
            data = self.get_data_from_db('select position_id, place_in_list, count, need_mark, mark, document_id from positions')
        check_result = self.check_data(data)
        if check_result == 0:
            for row in data:
                (position_id, place_in_list, count, need_mark, mark, document_id) = row
                answer.append(Positions(position_id=position_id,
                                        place_in_list=place_in_list,
                                        count=count,
                                        need_mark=need_mark,
                                        mark=mark,
                                        document_id=document_id))
        return answer

    def get_logs_by_test_id(self, test_id):
        answer = []
        data = self.get_data_from_db('select log_id, data, test_id, date_time from logs where test_id=%s' % test_id)
        check_result = self.check_data(data)
        if check_result == 0:
            for row in data:
                (log_id, data, test_id, date_time) = row
                answer.append(Logs(log_id=log_id, data=data, test_id=test_id, date_time=date_time))
        return answer

    def insert_in_to_settings(self, settings: Settings()):
        self.get_data_from_db("insert into settings(target, scaner_port, scaner_boundrate) VALUES('%s', '%s', %d)" % (settings.target, settings.scaner_port, settings.scaner_boundrate))
        return self.get_settings()[-1].setting_id

    def insert_in_to_tests(self, tasks: Tasks()):
        self.get_data_from_db("insert into tasks(name, setting_id, description, ip_recipient, port_recipient) VALUES('%s', %d, '%s', '%s', %d)" % (tasks.name, tasks.setting_id, tasks.description, tasks.ip_recipient, tasks.port_recipient))
        return self.get_tests()[-1].test_id

    def insert_in_to_documents(self, documents: Documents()):
        self.get_data_from_db("insert into documents(check_number, document_type, report_type, check_type, help_setting, type_close, sale, test_id) VALUES(%d, '%s', %d, %d, %d, %d, %d, %d)" % (documents.check_number,
                                                                                                                                                                                             documents.document_type,
                                                                                                                                                                                             documents.report_type,
                                                                                                                                                                                             documents.check_type,
                                                                                                                                                                                             documents.help_setting,
                                                                                                                                                                                             documents.type_close,
                                                                                                                                                                                             documents.sale,
                                                                                                                                                                                             documents.test_id))
        return self.get_documents()[-1].document_id

    def insert_in_to_poositions(self, position: Positions()):
        self.get_data_from_db("insert into positions(place_in_list, count, need_mark, mark, document_id) VALUES(%d, %d, %d, '%s', %d)" % (position.place_in_list, position.count, position.need_mark, position.mark, position.document_id))
        return self.get_positions(document_id=position.document_id)[-1].position_id

    def insert_in_to_logs(self, data, test_id):
        self.get_data_from_db("insert into logs(data, test_id) VALUES('%s', %d)" % (data, test_id))
        return self.get_logs_by_test_id(test_id=test_id)


    def update_settins_by_id(self, settings: Settings()):
        self.get_data_from_db("UPDATE settings SET target='%s', scaner_port='%s', scaner_boundrate=%d where setting_id=%d" % (settings.target, settings.scaner_port, settings.scaner_boundrate, settings.setting_id))
        return settings.setting_id

    def update_tests_by_id(self, tasks: Tasks()):
        self.get_data_from_db("UPDATE tasks SET name='%s', setting_id=%d, description='%s', ip_recipient='%s', port_recipient=%d where task_id=%d" % (tasks.name, tasks.setting_id, tasks.description, tasks.ip_recipient, tasks.port_recipient, tasks.test_id))
        return tasks.test_id

    def update_documents_by_id(self, document: Documents()):
        self.get_data_from_db("UPDATE documents SET check_number=%d, document_type='%s', report_type=%d, check_type=%d, help_setting=%d, type_close=%d, sale=%d where document_id=%d" % (document.check_number,
                                                                                                                                                                                         document.document_type,
                                                                                                                                                                                         document.report_type,
                                                                                                                                                                                         document.check_type,
                                                                                                                                                                                         document.help_setting,
                                                                                                                                                                                         document.type_close,
                                                                                                                                                                                         document.sale,
                                                                                                                                                                                         document.document_id))
        return document.document_id

    def update_position_by_id(self, position: Positions()):
        self.get_data_from_db("UPDATE positions SET place_in_list=%d, count=%d, need_mark=%d, mark='%s', document_id=%d where position_id=%d" % (position.place_in_list,
                                                                                                                                              position.count,
                                                                                                                                              position.need_mark,
                                                                                                                                              position.mark,
                                                                                                                                              position.document_id,
                                                                                                                                              position.position_id))
        return position.position_id

    def update_log_by_test_id(self, data, test_id):
        self.get_data_from_db("UPDATE logs SET data='%s' where test_id=%d" % (data, test_id))
        return self.get_logs_by_test_id(test_id=test_id)

    def delete_position_by_id(self, position_id):
        self.get_data_from_db("DELETE FROM positions WHERE position_id=%d" % position_id)
        return self.get_positions(position_id=position_id)

    def delete_document_by_id(self, document_id):
        self.get_data_from_db("DELETE FROM positions WHERE document_id=%d" % document_id)
        self.get_data_from_db("DELETE FROM documents WHERE document_id=%d" % document_id)
        return self.get_documents(document_id=document_id)

    def delete_test_by_id(self, test_id):
        documents = self.get_documents(test_id=test_id)
        tests = self.get_tests(id=test_id)
        for i in documents:
            self.get_data_from_db("DELETE FROM positions WHERE document_id=%d" % i.document_id)
        for i in documents:
            self.get_data_from_db("DELETE FROM documents WHERE document_id=%d" % i.document_id)
        self.get_data_from_db("DELETE FROM tasks WHERE task_id=%d" % test_id)
        for i in tests:
            self.get_data_from_db("DELETE FROM settings WHERE setting_id=%d" % i.setting_id)
        return self.get_tests(id=test_id)
