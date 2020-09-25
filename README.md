# Auto send DDL

It's a simple script for my job.

1. Login rocket chat to get newest sql. 
2. Write sql to docx. 
3. Send docx via gmail.

## Prepare

* Rocket chat server and account
* A docx file with table
* Gmail account

## Installation

```
$ git clone https://github.com/grieve54706/auto_send_ddl.git
$ cd auto_send_ddl
$ pip3 install -r requirements.txt --user
$ cd resource/
$ vi config.yaml 
```

```

# Add your information, like account, password, taget mail, etc.

rocket_chat:
  user: 'rocket@mail.com'
  pass: 'password'
  server_url: 'http://localhost:3000'

file_folder: '/home/user/'
file_name: 'DB_DDL_2020{}.docx'

gmail:
  user: 'yourname@gmail.com'
  pass: 'yourpassword'

mail:
  subject: 'Subject DB DDL Doc {} - {}'
  to: 'target@mail.com'
  cc:
    - 'other@mail.com'
  content: |
    Dears
    The attach
    {}
  content_file_name: '{} DB DDL Doc'
```

## Running

```
$ python main.py [mail_version] [branch1] [branch2]...
```

## Example

```
$ python main.py 1 02 03
```

