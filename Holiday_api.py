import requests
import pandas as pd
import time

myapi = "7b83d100d7e14c5fbc8705ffe33cbb8d"
url = "https://holidays.abstractapi.com/v1/?"
country = input("which country: ").upper()
year = input("Year: ")
month = input("Month: ")
day_start = int(input("From which day: "))
day_end = int(input("To which day?: "))

for i in range(day_start,day_end+1):
    response = requests.get(f"{url}api_key={myapi}&country={country}&year={year}&month={month}&day={day_start}")
    print(response.status_code)
    holiday = response.json()
    pairs = []
    for kp in holiday:
        pairs=kp
    if holiday != []:
        pair_value = list(pairs.values())
        pair_keys = list(pairs.keys())
    else:
        print(f"There is no holiday on {month}/{day_start}/{year}")
        day_start += 1
        time.sleep(1)
        continue
    holiday_csv=pd.DataFrame({
        'Country Info': pair_keys,
        'Holiday Info': pair_value
    })
    holiday_csv_space = pd.DataFrame({
        "a":[''],
        "b":['']
    })
    holiday_csv.index = holiday_csv.index + 1
    print(holiday_csv)
    if country == "US":
       holiday_csv.to_csv('holiday_csv_file.csv',mode="a",index=False,header=False)
       holiday_csv_space.to_csv('holiday_csv_file.csv',sep=" ", mode="a", index=False, header=False)

    else:
        holiday_csv.to_csv(f'{country}_holiday_csv_file.csv',mode="a",index=False,header=False)
        holiday_csv_space.to_csv(f'{country}_holiday_csv_file.csv', sep=" ", mode="a", index=False, header=False)
    day_start += 1
    time.sleep(1)

print("------Successfully executed-----")
