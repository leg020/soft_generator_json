from fixture.db import DataBase

db = DataBase(host='127.0.0.1', name='tests', user='root', password='')

p = db.get_tests()
c = db.get_documents_by_test_id(2)
d = db.get_settings_by_id(1)
f = db.get_positions_by_document_id(1)
a = db.get_logs_by_test_id(2)
pass