from gendiff import generate_diff
import pytest

cases = [
    (
        'tests/fixtures/test_file1.json',
        'tests/fixtures/test_file2.json',
        'tests/fixtures/stylish_result_for_json.txt',
        'stylish'
    ),
    (
        'tests/fixtures/test_file3.yaml',
        'tests/fixtures/test_file4.yaml',
        'tests/fixtures/stylish_result_for_yaml.txt',
        'stylish'
    ),
    (
        'tests/fixtures/test_file5.json',
        'tests/fixtures/test_file6.json',
        'tests/fixtures/stylish_result_for_json2.txt',
        'stylish'
    ),
    (
        'tests/fixtures/test_file1.json',
        'tests/fixtures/test_file2.json',
        'tests/fixtures/plain_result_for_json.txt',
        'plain'
    ),
    (
        'tests/fixtures/test_file3.yaml',
        'tests/fixtures/test_file4.yaml',
        'tests/fixtures/plain_result_for_yaml.txt',
        'plain'
    ),
    (
        'tests/fixtures/test_file5.json',
        'tests/fixtures/test_file6.json',
        'tests/fixtures/plain_result_for_json2.txt',
        'plain'
    ),
    (
        'tests/fixtures/test_file5.json',
        'tests/fixtures/test_file6.json',
        'tests/fixtures/json_result_for_json.txt',
        'json'
    ),
]


@pytest.mark.parametrize(
    'file_path1, file_path2, result_path, style_format', cases
)
def test_generate_diff(file_path1, file_path2, result_path, style_format):
    with open(result_path) as f:
        result = f.read()
    assert generate_diff(
        file_path1, file_path2, style_format
    ) == result.rstrip()
