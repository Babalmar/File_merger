import time
import os
date = time.strftime('%Y%m%d')
file: str = 'Output_' + date + '.txt'


def merge_files(file):
    all_rows: list = []
    header: str = 'Name|Surname|'
    trailer: str = 'Number of rows: '
    filenames = os.listdir('./Input')

    for filename in filenames:
        with open('./Input/' + filename, "r") as f:
            for line in f:
                new_line = line.strip('\n')
                all_rows.append(new_line)

    with open('./Output/' + file, "w", encoding='utf-8') as f:
        hdr = header + '\n'
        f.write(hdr)
        for item in all_rows:
            row = item + '|' + '\n'
            f.write(row)
        trl = trailer + str(len(all_rows)) + '\n'
        f.write(trl)


merge_files(file)