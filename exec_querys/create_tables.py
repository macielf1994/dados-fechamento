from generate_querys.gen_querys import generate_query
import psycopg2 as pg
from dotenv import load_dotenv
import os
from glob import glob

def exec_create_tables(config: dict):

    load_dotenv('.env')
    conn = pg.connect(os.environ.get('DSN'))
    cursor = conn.cursor()
    list_create_table_querys = glob('querys/create_tables/*.sql')

    for query_path in list_create_table_querys:
        try:
            create_table_query = generate_query(
                query_path,
                config.get('range_start_date'),
                config.get('range_end_date'),
                config.get('version'),
                config.get('mmids')
                )
            cursor.execute(create_table_query)
            print(create_table_query)

        except pg.OperationalError as error:
            print(error)
            cursor.close()

    conn.commit()
    cursor.close()