import datetime
from rocketchat_API.rocketchat import RocketChat

from sendmail.utils import get_config

config = get_config()
rocket_user = config['rocket_chat']['user']
rocket_pass = config['rocket_chat']['pass']
server_url = config['rocket_chat']['server_url']
rocket = RocketChat(rocket_user, rocket_pass, server_url=server_url)
channels = rocket.channels_list().json()['channels']

room_id_map = {}
for channel in channels:
    room_id_map[channel['name']] = channel['_id']


def get_sql(room_name):
    room_id = room_id_map[room_name]
    messages = rocket.channels_history(room_id=room_id, count=20).json()['messages']
    messages = list(filter(lambda msg: 't' not in msg, messages))
    index = next(i for i, m in enumerate(messages) if is_separate(m))
    if index == 0:
        return None
    messages = messages[:index]
    return build_sql(messages)


def add_separate_message(room_name, mail_version):
    room_id = room_id_map[room_name]
    today = datetime.date.today().strftime('%Y/%m/%d')
    msg = '================ {} - {} ================'.format(today, mail_version)
    rocket.chat_post_message(msg, channel=room_id)


def is_separate(msg_obj):
    return '================' in msg_obj['msg']


def build_sql(messages):
    return '\n'.join(list(map(lambda message: message['msg'], messages)))
