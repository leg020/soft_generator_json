import jsonpickle
from model.data_for_json import *
from model.db_answer import *


class JsonData:

    def __init__(self):
        self.positions = []
        self.documents = []
        self.settings = None

    def add_positions_into_document(self, positions: []):
        pass

    def add_document_into_test(self, document: Documents):
        pass

    def add_settings_into_test(self, settings):
        pass