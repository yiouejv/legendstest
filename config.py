from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SECRET_KEY = os.urandom(24)

HOST = '127.0.0.1'
PORT = 3306
DATABASE = 'legends'
USERNAME = 'root'
PASSWORD = 'q1w2e3r4.'

DB_URL = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}".format(
    username=USERNAME, password=PASSWORD, host=HOST, port=PORT, db=DATABASE
)

engine = create_engine(DB_URL)
Base = declarative_base(engine)
session = sessionmaker(engine)()

#设置session过期时间
PARMANENT_SESSION_LIFETIME = 15
# SERVER_NAME = 'legendstest.com:5000'
ALLOWED_HOSTS = ['127.18.192.65']

ADMIN_UUID = 'DSADAFAS'
STUDENT_EMAIL = "DSADSAHHE"
TEACHER_EMAIL = "KJYJRFEF"

# 设置后台管理用户每页显示的数量
ADMIN_PAGE_SIZE = 10

# 选择题管理每页显示的题目数量
ChOICE_PAGE_SIZE = 15

# 简答题管理煤业显示的题目的数量
SHORT_ANSWER_SIZE = 10

# 程序设计题管理每页显示的数量
PROGRAM_SIZE = 10

# 试卷管理每页显示的数量
TEST_PAGER_SIZE = 10

# 成绩管理煤业显示的数量
SCORE_PAGER_SIZE = 20