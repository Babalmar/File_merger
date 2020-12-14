import time
import os
date = time.strftime('%Y%m%d')
file: str = 'Output' + date + '.txt'

def merge_files(file):
    all_rows: list = []
    header: str = 'Name|Surname|'
    trailer: str = 'Number of rows: '
    filenames = os.listdir('./Input')

