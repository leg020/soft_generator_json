

class Tasks:

    def __init__(self, test_id=None, name=None, setting_id=None):
        self.test_id = test_id
        self.name = name
        self.setting_id = setting_id


class Settings:

    def __init__(self, setting_id=None,
                 target=None,
                 scaner_port=None,
                 scaner_boundrate=None,
                 have_cassa=None):
        self.setting_id = setting_id
        self.target = target
        self.scaner_port = scaner_port
        self.scaner_boundrate = scaner_boundrate
        self.have_cassa = have_cassa


class Documents:

    def __init__(self, document_id=None,
                 check_number=None,
                 document_type=None,
                 report_type=None,
                 check_type=None,
                 help_setting=None,
                 type_close=None,
                 sale=False,
                 test_id=None):
        self.document_id = document_id
        self.check_number = check_number
        self.document_type = document_type
        self.report_type = report_type
        self.check_type = check_type
        self.help_setting = help_setting
        self.type_close = type_close
        self.sale = sale
        self.test_id = test_id


class Positions:

    def __init__(self, position_id=None,
                 place_in_list=None,
                 count=None,
                 need_mark=False,
                 mark=None,
                 document_id=None):
        self.position_id = position_id
        self.place_in_list = place_in_list
        self.count = count
        self.need_mark = need_mark
        self.mark = mark
        self.document_id = document_id


class Logs:

    def __init__(self, log_id=None, data=None, test_id=None, date_time=None):
        self.log_id = log_id
        self.data = data
        self.test_id = test_id
        self.date_time = date_time