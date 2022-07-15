from gendiff.formaters.stylish import stylish_format
from gendiff.formaters.plain import plain_format
from tests.fixtures.test_file_stylish import data


result_path_stylish = 'tests/fixtures/stylish_result_for_json2.txt'
result_path_plain = 'tests/fixtures/plain_result_for_json2.txt'


def test_stylish_format():
    with open(result_path_stylish) as f:
        file_result = f.read()
    assert stylish_format(data) == file_result.rstrip()


def test_plain_format():
    with open(result_path_plain) as f:
        file_result = f.read()
    assert plain_format(data) == file_result.rstrip()
