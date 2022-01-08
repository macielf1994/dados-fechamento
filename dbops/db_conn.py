import psycopg2 as pg
from dotenv import load_dotenv
import os

def db_connection():
    load_dotenv('/opt/job-projects/dados-fechamento/.env')

    try:
        conn = pg.connect(os.environ.get('DSN'))
        return conn
    except pg.OperationalError as error:
        print(error)
        return