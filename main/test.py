import json


def open_operations_list():
    with open("main/operations.json", encoding="utf-8") as data_file:
        operations_file = json.load(data_file)
        return operations_file


def filtered_operations_list():
    filtered_list = [item for item in open_operations_list() if item]
    return filtered_list


def sorted_operations_list():
    sorted_operation_list = sorted(filtered_operations_list(), key=lambda x: x["date"], reverse=True)
    return sorted_operation_list
