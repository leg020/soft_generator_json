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

    def get_tests(self):
        answer = []
        data = self.get_data_from_db('select task_id, name, setting_id, description, ip_recipient, port_recipient from tasks')
        check_result = self.check_data(data)
        if check_result == 0:
            for row in data:
                (test_id, name, setting_id, description, ip_recipient, port_recipient) = row
                answer.append(Tasks(test_id=test_id, name=name, setting_id=setting_id, description=description, ip_recipient=ip_recipient, port_recipient=port_recipient))
        else:
            answer = -1
        return answer

    def get_test_by_id(self, id):
        answer = []
        data = self.get_data_from_db('select task_id, name, setting_id, description, ip_recipient, port_recipient from tasks where task_id=%s' % id)
        check_result = self.check_data(data)
        if check_result == 0:
            for row in data:
                (test_id, name, setting_id, description, ip_recipient, port_recipient) = row
                answer.append(Tasks(test_id=test_id, name=name, setting_id=setting_id, description=description, ip_recipient=ip_recipient, port_recipient=port_recipient))
        else:
            answer = -1
        return answer

    def get_settings_by_id(self, id):
        answer = []
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
        else:
            answer = -1
        return answer

    def get_documents_by_test_id(self, test_id):
        answer = []
        data = self.get_data_from_db('select document_id, check_number, document_type, report_type, check_type, help_setting, type_close, sale, test_id from documents where test_id=%s' % test_id)
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
        else:
            answer.append(Documents(document_type=check_result))
        return answer

    def get_positions_by_document_id(self, document_id):
        answer = []
        data = self.get_data_from_db('select position_id, place_in_list, count, need_mark, mark, document_id from positions where document_id=%s' % document_id)
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
        else:
            answer.append(Positions(mark=check_result))
        return answer

    def get_logs_by_test_id(self, test_id):
        answer = []
        data = self.get_data_from_db('select log_id, data, test_id, date_time from logs where test_id=%s' % test_id)
        check_result = self.check_data(data)
        if check_result == 0:
            for row in data:
                (log_id, data, test_id, date_time) = row
                answer.append(Logs(log_id=log_id, data=data, test_id=test_id, date_time=date_time))
        else:
            answer.append(Documents(document_type=check_result))
        return answer