from _datetime import datetime


class Operations:
    def __init__(self, status, date, amount, currency, description, transfer_to, transfer_from):
        self.status = status
        self.date = date
        self.amount = amount
        self.currency = currency
        self.description = description
        self.transfer_to = transfer_to
        self.transfer_from = transfer_from

    def status_operation(self):
        if self.status == "EXECUTED":
            return True

    def date_operation(self):
        date_object = datetime.strptime(self.date, "%Y-%m-%dT%H:%M:%S.%f")
        formatted_date = date_object.strftime('%d.%m.%Y')
        return formatted_date

    def account_coding(self):
        account = self.transfer_to.split()
        return f'{account[0]} **{account[-1][-4:]}'

    def transfer_from_codding(self):
        if self.transfer_from:
            file_coding = self.transfer_from.split()
            if 'Счет' in file_coding:
                return f'{file_coding[0]} **{file_coding[-1][-4:]}'
            elif len(file_coding[-1]) <= 16:
                return f'{" ".join(file_coding[0:-1])} {file_coding[-1][:4]} ' \
                       f'{file_coding[-1][4:6]}** **** {file_coding[-1][-4:]}'

    def __repr__(self):
        return f'''Статус перевода: {self.status}
Дата перевода: {self.date}
Сумма перевода: {self.amount}
Валюта перевода: {self.currency}
Назначение платежа: {self.description}
Получатель платежа: {self.transfer_to}
Отправитель: {self.transfer_from}'''
