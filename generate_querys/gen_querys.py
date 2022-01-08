from datetime import datetime, date

def generate_query(path_query: str, start_date: str, end_date: str, version: str, list_int_mmids: str):
    month = datetime.strptime(start_date, '%Y-%m-%d').strftime('%B').lower()
    today_date_number = datetime.strptime(str(date.today()), '%Y-%m-%d').strftime('%Y%m%d')
    mmids_str_list = [str(mmid) for mmid in list_int_mmids]

    with open(path_query) as query:
        query_new_regs_users = query \
            .read() \
            .replace('start_date_to_replace', f"'{start_date}'") \
            .replace('end_date_to_replace', f"'{end_date}'") \
            .replace('month_to_replace', f"{month}") \
            .replace('date_to_replace', f"{today_date_number}") \
            .replace('version_to_replace', version) \
            .replace('mmid_list_to_replace', ',\n'.join(mmids_str_list))
            
        return query_new_regs_users