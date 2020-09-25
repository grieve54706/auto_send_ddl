from sendmail.doc import write_doc
from sendmail.rocketchat import get_sql


def test_get_sql():
    room_name = 'test'
    sql = get_sql(room_name)
    assert sql == 'TEST SQL'


def test_write_doc():
    branch_name = '10'
    mail_version = '1'
    write_doc('TEST SQL', branch_name, mail_version)
