import numpy as np

def cleansing_records(row, hd_empty, hd_toolong, hd_invl_phone, hd_invl_salary):
    hd_empty(row)
    hd_toolong(row)
    hd_invl_phone(row)
    hd_invl_salary(row)


def convert_empty(row):
    if row[0] == '':
        row[0] = 'John Doe'

def convert_long(row):
    if len(row[0]) > 25:
        row[0] = row[0][:25]


def convert_digit0(row):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    cv0 = lambda x : '0' if x not in digits else x
    row[1] = ''.join(list(map(cv0, row[1])))


def convert_digit_pre(row):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    phone = list(row[1])
    phone1 = ['0'] + phone
    for i, c in enumerate(phone):
        if c not in digits:
            phone[i] = phone1[i]
            phone1[i+1] = phone[i]

    row[1] = ''.join(phone)


def convert_salary_edge(row):
    if row[2] < 200:
        row[2] = 200
    elif row[2] > 2000:
        row[2] = 2000

data = [
        ['', '0123a334', 100],
        ['a very looooooooooooooooooooo name.........', '09827772aa', 5000],
        ['john lennon', '09081232323', 500]
       ]

for row in data:
    cleansing_records(row, convert_empty, convert_long, convert_digit_pre, convert_salary_edge)

print(data)
