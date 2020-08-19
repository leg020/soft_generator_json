from model.db_answer import Settings, Tasks


class ModelBuilder:

    def convert_in_tasks(self, form,
                         name=None,
                         setting_id=None,
                         description=None,
                         ip_recipient=None,
                         port_recipient=None):
        tests = Tasks()
        if name != None:
            tests.name = name
        else:
            tests.name = form['test_name']
        if setting_id != None:
            tests.setting_id = int(setting_id)
        else:
            tests.setting_id = int(form['setting_id'])
        if description != None:
            tests.description = description
        else:
            tests.description = form['description']
        if ip_recipient != None:
            tests.ip_recipient = ip_recipient
        else:
            tests.ip_recipient = form['ip_recipient']
        if port_recipient != None:
            tests.port_recipient = port_recipient
        else:
            tests.port_recipient = int(form['port_recipient'])
        return tests

    def convert_in_settings(self, form, target=None, scaner_port=None, scaner_boundrate=None):
        settings = Settings()
        if target != None:
            settings.target = target
        else:
            settings.target = form['target']
        if scaner_port != None:
            settings.scaner_port = scaner_port
        else:
            settings.scaner_port = form['scaner_port']
        if scaner_boundrate != None:
            settings.scaner_boundrate = int(scaner_boundrate)
        else:
            settings.scaner_boundrate = int(form['scaner_boundrate'])
        return settings