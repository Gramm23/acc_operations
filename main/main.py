from utils import open_operations_list

operations = open_operations_list()

count = 0

for operation in operations:
    if operation.status_operation():
        print(f"""{operation.date_operation()} {operation.description} 
{operation.transfer_from_codding()} -> {operation.account_coding()} 
{operation.amount} {operation.currency}""")
        print()
        count += 1
        if count == 5:
            break
