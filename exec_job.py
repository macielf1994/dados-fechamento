from exec_querys.create_tables import exec_create_tables
from exec_querys.generete_bases import generate_files_bases
from mmids import list_mmids


closing_config = {
    'version' : '1',
    'range_start_date' : '2021-12-01',
    'range_end_date' : '2021-12-31',
    'mmids' : list_mmids
}

exec_create_tables(closing_config)

generate_files_bases(closing_config)