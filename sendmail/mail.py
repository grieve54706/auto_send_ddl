import smtplib
import datetime
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os.path import basename

from sendmail.utils import get_config

config = get_config()


def sendmail(mail_version, branch_names):

    gmail_user = config['gmail']['user']
    gmail_pass = config['gmail']['pass']

    today = datetime.date.today().strftime('%Y/%m/%d')

    content = build_content(branch_names)

    msg = MIMEMultipart()
    msg['Subject'] = config['mail']['subject'].format(today, mail_version)
    msg['From'] = gmail_user
    msg['To'] = config['mail']['to']
    msg['Cc'] = ','.join(config['mail']['cc'])
    body = build_body(content)
    msg.attach(body)

    files = get_file_names(branch_names)

    for f in files or []:
        with open(config['file_folder'] + f, "rb") as fil:
            part = MIMEApplication(fil.read(), Name=basename(f))
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_pass)
    to_addrs = [msg['To']] + config['mail']['cc']
    server.sendmail(msg['From'], to_addrs, msg.as_string())
    server.quit()


def build_content(branch_names):
    file_names = list(map(lambda name: config['mail']['content_file_name'].format(name), branch_names))
    file_names = '\n'.join(file_names)
    return config['mail']['content'].format(file_names)


def build_body(content):
    body = MIMEText(content, 'plain', "utf-8")
    body.set_charset("utf-8")
    return body


def get_file_names(branch_names):
    return list(map(lambda name: config['file_name'].format(name), branch_names))
