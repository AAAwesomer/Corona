import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
load_dotenv('../.env')

MYSQL_HOST = os.environ['MYSQL_HOST']
MYSQL_PORT = os.environ['MYSQL_PORT']
MYSQL_USER = os.environ['MYSQL_USER']
MYSQL_PASSWORD = os.environ['MYSQL_PASSWORD']
MYSQL_DB = os.environ['MYSQL_DB']
CHUNK_SIZE = int(os.environ.get('CHUNK_SIZE', '50000'))


def get_engine():
    return create_engine(f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}', echo=False)
