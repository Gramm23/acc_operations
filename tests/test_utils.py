import pytest
from main.module import Operations
import json
from main.utils import open_operations_list


@pytest.fixture
def operations_list():
    with open("testfile.json", encoding="utf-8") as data_file:
        operations_file = json.load(data_file)
        filtered_list = [item for item in operations_file if item]
        sorted_operation_list = sorted(filtered_list, key=lambda x: x["date"], reverse=True)
        operations = []
        for item in sorted_operation_list:
            state = item['state']
            date = item['date']
            amount = item['operationAmount']["amount"]
            currency_name = item['operationAmount']["currency"]["name"]
            description = item["description"]
            to = item['to']

            if 'from' in item:
                from_value = item['from']
            else:
                from_value = None

            operation = Operations(state, date, amount, currency_name, description, to, from_value)
            operations.append(operation)

        return operations


def test_open_operations_list(operations_list):
    assert len(operations_list) > 0
    assert isinstance(operations_list[0], Operations)
    assert operations_list == open_operations_list()


# def test_with_error():
#     with pytest.raises(FileNotFoundError):
#         open_operations_list("operations.txt")
