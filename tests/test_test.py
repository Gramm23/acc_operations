import json
from main import test


def test_open_operations_list():
    with open('tests/testfile.json', encoding='utf-8') as data_testfile:
        result_testfile = json.load(data_testfile)

        test_result = test.open_operations_list()

        assert result_testfile[0] == test_result[0]
