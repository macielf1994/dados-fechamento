def get_new_registered_users(start_date: str, end_date: str):
    with open('querys/new_registered_users.sql') as query:
        q_new_registered_users = query \
            .read() \
            .replace('start_enrollment_date', f"'{start_date}'") \
            .replace('end_enrollment_date;', f"'{end_date}'")

        print(q_new_registered_users)

get_new_registered_users('2021-12-01', '2021-12-31')