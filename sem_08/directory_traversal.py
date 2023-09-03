import os
import csv
import json
import pickle


def save_directories(path: str, to_csv=True, to_json=True, to_pickle=True):
    """

    :param path: required parameter of type str
    :param to_csv: keyword parameter
    :param to_json: keyword parameter
    :param to_pickle: keyword parameter

    """

    dictionary = {}
    if to_csv:
        f = open('directory.csv', 'w', newline='', encoding='utf-8')
        csv_write = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        csv_write.writerow(['Directory Name', 'Parent Directory', 'Type', 'Size'])
    for i in range(0, 3):
        for elem in os.walk(path):
            if type(elem[i]) == list:
                for j in range(len(elem[i])):
                    directory = elem[0] + '/' + elem[i][j]
                    type_of_elem = 'directory' if i == 1 else 'file'
                    if i == 2:
                        size = os.path.getsize(directory)
                    else:
                        size = get_dir_size(directory)
                    dictionary[elem[i][j]] = {'parent_directory': elem[0][elem[0].rindex('/') + 1:],
                                              'type': type_of_elem, 'size': size}
                    if to_csv:
                        csv_write.writerow([elem[i][j], elem[0][elem[0].rindex('/') + 1:], type_of_elem, size])
    f.close()
    if to_json:
        with open('directory.json', 'w', encoding='utf-8') as file:
            json.dump(dictionary, file)
    if to_pickle:
        with open('directory.pickle', 'wb') as file2:
            pickle.dump(dictionary, file2)


def get_dir_size(path):
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total
