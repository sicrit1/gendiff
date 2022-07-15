from gendiff import generate_diff
import pytest

cases_stylish = [
    (
        'tests/fixtures/test_file1.json',
        'tests/fixtures/test_file2.json',
        'tests/fixtures/stylish_result_for_json.txt'
    ),
    (
        'tests/fixtures/test_file3.yaml',
        'tests/fixtures/test_file4.yaml',
        'tests/fixtures/stylish_result_for_yaml.txt'
    ),
    (
        'tests/fixtures/test_file5.json',
        'tests/fixtures/test_file6.json',
        'tests/fixtures/stylish_result_for_json2.txt'
    ),
]


@pytest.mark.parametrize('file_path1, file_path2, result_path', cases_stylish)
def test_generate_diff(file_path1, file_path2, result_path):
    with open(result_path) as f:
        result = f.read()
        assert generate_diff(file_path1, file_path2) == result.rstrip()


cases_plain = [
        (
            'tests/fixtures/test_file1.json',
            'tests/fixtures/test_file2.json',
            'tests/fixtures/plain_result_for_json.txt'
        ),
        (
            'tests/fixtures/test_file3.yaml',
            'tests/fixtures/test_file4.yaml',
            'tests/fixtures/plain_result_for_yaml.txt'
        ),
        (
            'tests/fixtures/test_file5.json',
            'tests/fixtures/test_file6.json',
            'tests/fixtures/plain_result_for_json2.txt'
        ),
]


@pytest.mark.parametrize('file_path1, file_path2, result_path', cases_plain)
def test_generate_diff(file_path1, file_path2, result_path):
    with open(result_path) as f:
        result = f.read()
        assert generate_diff(file_path1, file_path2, 'plain') == result.rstrip()


cases_json = [
        (
            'tests/fixtures/test_file5.json',
            'tests/fixtures/test_file6.json',
            'tests/fixtures/json_result_for_json.txt'
         ),
]


@pytest.mark.parametrize('file_path1, file_path2, result_path', cases_json)
def test_generate_diff(file_path1, file_path2, result_path):
    with open(result_path) as f:
        result = f.read()
    assert generate_diff(file_path1, file_path2, 'json') == result.rstrip()
