import json


def generate_diff(file_path1, file_path2):
    with open(file_path1) as f1:
        file1 = json.load(f1)
    with open(file_path2) as f2:
        file2 = json.load(f2)
    data_inter = file1.keys() & file2.keys()
    data_diff1 = file1.keys() - file2.keys()
    data_diff2 = file2.keys() - file1.keys()
    diff_str = ''
    for i in data_inter:
        if file1[i] == file2[i]:
            diff_str += f'  {str(i)}: {str(file1[i])}\n'
        else:
            diff_str += f'- {str(i)}: {str(file1[i])}\n+ {str(i)}: {str(file2[i])}\n'
    for n in data_diff1:
        diff_str += f'- {str(n)}: {str(file1[n])}\n'
    for x in data_diff2:
        diff_str += f'+ {str(x)}: {str(file2[x])}\n'
    deff_json = '{\n' + diff_str.lower() + '}'
    return deff_json


def main():
    generate_diff(file_path1, file_path2)


if __name__ == '__main__':
    main()
