from generate_querys.gen_querys import generate_query
import psycopg2 as pg
from dotenv import load_dotenv
import os
import pandas as pd
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from glob import glob

def generate_files_bases(config: dict):

    load_dotenv('.env')
    conn = pg.connect(os.environ.get('DSN'))
    cursor = conn.cursor()
    year_month = datetime.strptime(str(date.today() - relativedelta(months = 1)), '%Y-%m-%d').strftime('%Y-%m')
    list_sql_files = glob('querys/selects/*.sql')

    list_name_sheet_refined = [
        'New Registereds',
        'Total Unique Users',
        'Unique Users Data',
        'U. User Data Devices',
        'Clicks Data'
        ]

    excel_data = pd.ExcelWriter(f'closing_data_jobs/Dados Fechamento {year_month}.xlsx', engine='xlsxwriter')

    for name_sheet, query_path in zip(list_name_sheet_refined, list_sql_files):
        try:
            select_table_query = generate_query(
                query_path,
                config.get('range_start_date'),
                config.get('range_end_date'),
                config.get('version'),
                config.get('mmids')
                )
            print(select_table_query)

            df = pd.read_sql(select_table_query, conn)
            list_column_names_refined = [column.replace('_', ' ').title() for column in list(df.columns.values)]
            df.columns = list_column_names_refined
            df.to_excel(excel_data, f"{name_sheet}", index=False)
            
        except pg.OperationalError as error:
            print(error)
            cursor.close()

    excel_data.save()
    cursor.close()