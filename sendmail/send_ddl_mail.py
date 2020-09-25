
import sys
from sendmail.doc import write_doc
from sendmail.mail import sendmail
from sendmail.rocketchat import get_sql, add_separate_message


def main():

    mail_version = sys.argv[1]

    branch_names = sys.argv[2:]

    has_sql_names = []

    for branch_name in branch_names:
        room_name = '{}rc_sql'.format(branch_name)
        sql = get_sql(room_name)
        if sql is not None:
            add_separate_message(room_name, mail_version)
            write_doc(sql, branch_name, mail_version)
            has_sql_names.append(branch_name)

    if len(has_sql_names) != 0:
        sendmail(mail_version, has_sql_names)
        print('Mail sent')
    else:
        print('No sql need to send')


if __name__ == '__main__':
    main()
