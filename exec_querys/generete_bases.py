from generate_querys.gen_querys import generate_query
import psycopg2 as pg
from dotenv import load_dotenv
import os
import pandas as pd
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

def generate_files_bases(config: dict):

    load_dotenv('/opt/job-projects/dados-fechamento')
    conn = pg.connect(os.environ.get('DSN'))
    cursor = conn.cursor()
    year_month = datetime.strptime(str(date.today() - relativedelta(months = 1)), '%Y-%m-%d').strftime('%Y-%m')

    list_name_sheet = [
        'New Registereds',
        'Total Unique Users',
        'Unique Users Data',
        'U. User Data Devices'
        ]
    list_select_table_querys = [
        'querys/selects/1_select_new_registered_users.sql',
        'querys/selects/2_select_count_unique_users.sql',
        'querys/selects/3_select_unique_users_data.sql',
        'querys/selects/4_select_unique_users_device_data.sql',
        # 'querys/selects/5_select_click_mmids_data.sql'
    ]

    excel_data = pd.ExcelWriter(f'Dados Fechamento {year_month}.xlsx', engine='xlsxwriter')

    for name_sheet, query_path in zip(list_name_sheet, list_select_table_querys):
        try:
            select_table_query = generate_query(
                query_path,
                config.get('range_start_date'),
                config.get('range_end_date'),
                config.get('version'),
                config.get('mmids')
                )

            df = pd.read_sql(select_table_query, conn)
            list_column_names_refined = [column.replace('_', ' ').title() for column in list(df.columns.values)]
            df.columns = list_column_names_refined
            df.to_excel(excel_data, f"{name_sheet}", index=False)
            
        except pg.OperationalError as error:
            print(error)
            cursor.close()

    excel_data.save()
    cursor.close()