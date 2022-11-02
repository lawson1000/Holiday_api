import requests
import pandas
from pprint import pprint
myapi = "7b83d100d7e14c5fbc8705ffe33cbb8d"
url = "https://holidays.abstractapi.com/v1/?"
response = requests.get(f"https://holidays.abstractapi.com/v1/?api_key=7b83d100d7e14c5fbc8705ffe33cbb8d&country=US&year=2022&month=01&day=01")
# country = input("which country: ").upper()
# year = input("what year: ")
# month = input("month: ")
# day_start = int(input("day in the month to start from: "))
# day_end = int(input("to which day?: "))

# response = requests.get(f"{url}api_key={myapi}&country={country}&year={year}&month={month}&day={day_start}")
# day_start += 1
print(response.status_code)
print(response.content)
holiday = response.json()
pprint(holiday)
# for i in range(day_start,day_end+1):
#     response = requests.get(f"{url}api_key={myapi}&country={country}&year={year}&month={month}&day={day_start}")
#     day_start += 1
#     print(response.status_code)
#     print(response.content)

# import pandas as pd
#
#
# students = ['francis','faith','daniel','charles']
# ages = [30,32,29,26]
# RegNO = ['Sto1','Sto2','Sto3','Sto4']
#
#
# studtable =pd.DataFrame({
#     'Students': students,
#     'Ages':ages,
#     'Phone': ['Samsung', 'Huawei','Pixel','Xiaomi'],
#     'RegNO':RegNO
# })

# # studtable.index = studtable.index + 1
# studtable = studtable.set_index("RegNO")
#
# print(studtable)
# print("-----------")
# print(studtable['Students'])
# print("-----------")
# print(studtable['Ages'])
# print("-----------")
# print(studtable['Students'][1])
# print("-----------")
# print(studtable['Ages'][1])
# print("-----------")
# print(studtable['Phone'])
# print("-----------")
# print(studtable['Phone'][3])
#
# studtable.to_csv('Student Details.csv')
# input()
