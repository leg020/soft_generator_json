

class PositionsInCheck:

    def __init__(self, place_in_list=None, cout=None, need_mark=False, mark=None):
        self.place_in_list = place_in_list
        self.cout = cout
        self.need_mark = need_mark
        self.mark = mark


class Checks:

    def __init__(self, check_number=None,
                 document_type=None,
                 report_type=None,
                 check_type=None,
                 help_setting=None,
                 positions=None,
                 type_close=None,
                 sale=False):
        self.check_number = check_number
        self.document_type = document_type
        self.report_type = report_type
        self.check_type = check_type
        self.help_setting = help_setting
        self.positions = positions
        self.type_close = type_close
        self.sale = sale


class Settings:

    def __init__(self, target=None, scaner_port=None, scaner_boundrate=None, have_cassa=None):
        self.target = target
        self.scaner_port = scaner_port
        self.scaner_boundrate = scaner_boundrate
        self.have_cassa = have_cassa


class Data:

    def __init__(self, settings=None, data=None):
        self.settings = settings
        self.data = data