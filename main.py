# Домашняя работа по теме: Работа с файлами
files = ['1.txt', '2.txt', '3.txt']
log_file_name = 'log.txt'


def get_lines_count_files():
    file_list = {}
    for file_name in files:
        with open(file_name, 'rt', encoding='utf-8') as file:
            file_list[file_name] = len(file.readlines())
    sorted_file_list = dict(sorted(file_list.items(), key=lambda item: item[1]))
    return sorted_file_list

def log_files(log_file):
    sorted_files = get_lines_count_files()
    with open(log_file, 'wt', encoding='utf-8') as file:
        for file_name, line_count in sorted_files.items():
            file.write(file_name + '\n')
            file.write(str(line_count) + '\n')
            with open(file_name, 'rt', encoding='utf-8') as file2:
                file_data = file2.read()
                if not file_data.endswith('\n'):
                    file_data +='\n'
                file.write(file_data)

log_files(log_file_name)



