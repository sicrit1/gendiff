from gendiff import generate_diff
import  pytest


def test_generate_diff():
    with open('tests/fixtures/result.txt') as f:
        result = f.read()
        assert generate_diff('tests/fixtures/test_file1.json', 'tests/fixtures/test_file2.json') == result.rstrip()
