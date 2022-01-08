from dbops.db_conn import db_connection as conn

def gen_query_new_regs(start_date: str, end_date: str):
    with open('querys/new_registered_users.sql', 'r') as query:
        query_new_regs_users = query \
            .read() \
            .replace('start_enrollment_date', f"'{start_date}'") \
            .replace('end_enrollment_date;', f"'{end_date}'")

        return query_new_regs_users

def exec_query_new_regs(query: str):
    cursor = conn().cursor()
    try:
        cursor.execute(query)
        new_regs_users = cursor.fetchone()[0]
        cursor.close()

        return new_regs_users
    except:
        print('Não foi possível executar a query.')
        cursor.close()

        return
        

generated_query = gen_query_new_regs('2021-12-01', '2021-12-31')

exec_query_new_regs(generated_query)