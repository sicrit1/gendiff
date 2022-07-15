from gendiff.formaters.stylish import stylish
from tests.fixtures.test_file_stylish import data


result_path = 'tests/fixtures/result_for_stylish.txt'


def test_stylish():
    with open(result_path) as f:
        file_result = f.read()
    assert stylish(data) == file_result.rstrip()
