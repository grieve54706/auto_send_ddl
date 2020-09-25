import datetime

from docx import Document

from sendmail.utils import get_config

config = get_config()


def write_doc(sql, branch_name, mail_version):
    file_name = config['file_folder'] + config['file_name'].format(branch_name)
    document = Document(file_name)
    cells = document.tables[0].add_row().cells
    cells[0].text = datetime.date.today().strftime('%Y-%m-%d')
    cells[1].text = mail_version
    cells[2].text = sql
    document.save(file_name)
