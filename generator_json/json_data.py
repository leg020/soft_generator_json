import jsonpickle
import json
from model.data_for_json import *
from model.db_answer import *


class JsonData:

    def __init__(self):
        self.positions = []
        self.documents = []
        self.settings = None

    def add_positions(self, positions: []):
        for i in positions:
            self.positions.append(PositionsInCheck(place_in_list=i.place_in_list,
                                                   cout=i.count,
                                                   need_mark=i.need_mark,
                                                   mark=bool(i.mark)))

    def add_document(self, document: Documents):
        doc = Checks(check_number=document.check_number,
                     document_type=document.document_type,
                     report_type=document.report_type,
                     check_type=document.check_type,
                     help_setting=document.help_setting,
                     type_close=document.type_close,
                     sale=bool(document.sale),
                     positions=self.positions)
        self.documents.append(doc)
        self.positions = []

    def add_settings(self, settings: Settings_db):
        self.settings = Settings(target=settings.target,
                                 scaner_port=settings.scaner_port,
                                 scaner_boundrate=settings.scaner_boundrate,
                                 have_cassa=settings.have_cassa)

    def create_json(self):
        data = Data(settings=self.settings, data=self.documents)
        jsonpickle.set_encoder_options('json', indent=2)
        self.documents = []
        return json.loads(jsonpickle.encode(data))
