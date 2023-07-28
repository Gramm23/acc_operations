import json
from module import Operations


def open_operations_list():
    with open("operations.txt", encoding="utf-8") as data_file:
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


print(open_operations_list())
