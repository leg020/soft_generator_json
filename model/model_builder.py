from model.db_answer import Settings, Tasks, Documents, Positions


class ModelBuilder:

    def __init__(self, form):
        self.form = form

    def convert_in_tasks(self,
                         test_id=None,
                         name=None,
                         setting_id=None,
                         description=None,
                         ip_recipient=None,
                         port_recipient=None):
        tests = Tasks()
        if test_id != None:
            tests.test_id = int(test_id)
        elif self.form['test_id'] != None and self.form['test_id'] != 'None' and self.form['test_id'] != '':
            tests.test_id = int(self.form['test_id'])
        if name != None:
            tests.name = name
        else:
            tests.name = self.form['test_name']
        if setting_id != None:
            tests.setting_id = int(setting_id)
        else:
            tests.setting_id = int(self.form['setting_id'])
        if description != None:
            tests.description = description
        else:
            tests.description = self.form['description']
        if ip_recipient != None:
            tests.ip_recipient = ip_recipient
        else:
            tests.ip_recipient = self.form['ip_recipient']
        if port_recipient != None:
            tests.port_recipient = port_recipient
        else:
            tests.port_recipient = int(self.form['port_recipient'])
        return tests

    def convert_in_settings(self,
                            setting_id=None,
                            target=None,
                            scaner_port=None,
                            scaner_boundrate=None):
        settings = Settings()
        if setting_id != None:
            settings.setting_id = setting_id
        elif self.form['setting_id'] != None and self.form['setting_id'] != 'None' and self.form['setting_id'] != '':
            settings.setting_id = int(self.form['setting_id'])
        if target != None:
            settings.target = target
        else:
            settings.target = self.form['target']
        if scaner_port != None:
            settings.scaner_port = scaner_port
        else:
            settings.scaner_port = self.form['scaner_port']
        if scaner_boundrate != None:
            settings.scaner_boundrate = int(scaner_boundrate)
        else:
            settings.scaner_boundrate = int(self.form['scaner_boundrate'])
        return settings

    def convert_in_documents(self,
                             document_id=None,
                             check_number=None,
                             document_type=None,
                             report_type=None,
                             check_type=None,
                             help_setting=None,
                             type_close=None,
                             sale=None,
                             test_id=None):
        document = Documents()
        if document_id != None:
            document.document_id = int(document_id)
        else:
            document.document_id = None
        if check_number != None:
            document.check_number = check_number
        else:
            document.check_number = int(self.form['check_number'])

        if document_type != None:
            document.check_type = document_type
        else:
            document.document_type = self.form['document_type']

        if report_type != None:
            document.report_type = report_type
        else:
            document.report_type = int(self.form['report_type'])

        if check_type != None:
            document.check_type = check_type
        else:
            document.check_type = int(self.form['check_type'])

        if help_setting != None:
            document.help_setting = help_setting
        else:
            document.help_setting = int(self.form['help_setting'])

        if type_close != None:
            document.type_close = type_close
        else:
            document.type_close = int(self.form['type_close'])

        if sale != None:
            document.sale = sale
        else:
            try:
                document.sale = int(self.form['sale'])
            except:
                document.sale = 0

        if test_id != None:
            document.test_id = test_id
        else:
            document.test_id = int(self.form['test_id'])

        return document

    def convert_in_positions(self,
                             position_id=None,
                             place_in_list=None,
                             count=None,
                             need_mark=None,
                             mark=None,
                             document_id=None):
        position = Positions()
        if position_id != None:
            position.position_id = position_id
        else:
            try:
                position.position_id = int(self.form['position_id'])
            except:
                position.position_id = None

        if place_in_list != None:
            position.place_in_list = place_in_list
        else:
            position.place_in_list = int(self.form['place_in_list'])

        if count != None:
            position.count = count
        else:
            position.count = int(self.form['count'])

        if need_mark != None:
            position.need_mark = need_mark
        elif self.form['document_operation'] == 'add_position':
            try:
                position.need_mark = int(self.form['new_need_mark'])
            except:
                position.need_mark = 0
        elif self.form['document_operation'] == 'edit_position':
            try:
                position.need_mark = int(self.form['need_mark'])
            except:
                position.need_mark = 0

        if mark != None:
            position.mark = mark
        else:
            position.mark = self.check_mark(self.form['mark'])

        if document_id != None:
            position.document_id = int(document_id)
        else:
            position.document_id = int(self.form['document_id'])
        return position


    def check_mark(self, mark):
        if mark == '':
            mark = None
        return mark



