from gendiff import generate_diff
import pytest

cases = [
    (
        'tests/fixtures/test_file1.json',
        'tests/fixtures/test_file2.json',
        'tests/fixtures/result_for_json.txt'
    ),
    (
        'tests/fixtures/test_file3.yaml',
        'tests/fixtures/test_file4.yaml',
        'tests/fixtures/result_for_yaml.txt'
    ),
]


@pytest.mark.parametrize('file_path1, file_path2, result_path', cases)
def test_generate_diff(file_path1, file_path2, result_path):
    with open(result_path) as f:
        result = f.read()
        assert generate_diff(file_path1, file_path2) == result.rstrip()
