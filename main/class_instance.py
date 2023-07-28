from test import sorted_operations_list
from module import Operations


def get_class_instance():
    operations = []
    for item in sorted_operations_list():
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
