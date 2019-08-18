import random,numpy as np  
row = np.array(["ha", "tam", "Duy", "Tham"], [123452169,845316578,751264985,896542365], [150,250,350,550])

def cleansing_records(row, hd_empty,hd_toolong,hd_invl_phone,hd_invl_salary):
    hd_empty(row)
    hd_toolong(row)
    hd_invl_phone(row)
    hd_invl_salary(row)
def convert_empty(row):
    if row[0] == '':
        row[0] == "John Doe"
def convert_long(row):
    if len(row[0])> 25:
        row[0] = row[0][:25]
def convert_digit0(row):
    digis = ['0','1','2','3','4','5','6','7','8','9']
    cv0 = lambda x:'0' if x not in digis else x
    row[1] = ''.join(list(map(cv0, row[1])))
def convert_digit_pre(row):
    digis = ['0','1','2','3','4','5','6','7','8','9']
    phone = list(row[1])
    phone1 = ['0'] + phone
    for i, c in enumerate(phone):
        if c not in digis:
            phone[i] = phone1[i]
            phone1[i+1] = phone[i]
def convert_salary_edge(row):
    return 0
def convert_salary_mean(row):
    return 0
cleansing_records(thong_tin,)