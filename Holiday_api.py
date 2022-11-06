import requests
import pandas as pd
import time

myapi = "7b83d100d7e14c5fbc8705ffe33cbb8d"
url = "https://holidays.abstractapi.com/v1/?"

count = 0
while count < 4:
    country = input("which country: ").upper()
    while country.isalpha() != True or len(country) != 2:
        print("Invalid Input\n")
        country = input("Enter a valid alpha 2 Country Code: ").upper()

    while True:
        try:
            year = int(input("Year: "))
            if year < 1800 or year > 9999:
                print("Invalid! Please Enter between the range of 1800 - 9999\n")
                continue
            break
        except ValueError:
            print("Invalid! Enter a Numeric value")

    while True:
        try:
            month = int(input("Month: "))
            if month < 1 or month > 12:
                print("Invalid! Please Enter between the range of 1 - 12\n")
                continue
            break
        except ValueError:
            print("Invalid! Enter a Numeric value")

    while True:
        try:
            day_start = int(input("From which day: "))
            day_start_error = f"Invalid! {month}/{year} do not have day {day_start} \nEnter a valid day\n"
            if month == 9 or month == 4 or month == 6 or month == 11:
                if day_start < 1 or day_start > 30:
                    print(day_start_error)
                    continue
            elif month == 2:
                if year % 4 == 0:
                    if day_start < 1 or day_start > 29:
                        print(day_start_error)
                        continue
                else:
                    if day_start < 1 or day_start > 28:
                        print(day_start_error)
                        continue
            else:
                if day_start < 1 or day_start > 31:
                    print(day_start_error)
                    continue
            break
        except ValueError:
            print("Invalid! Enter a Numeric value")

    while True:
        try:
            day_end = int(input("To which day?: "))
            day_end_error = f"Invalid! {month}/{year} do not have day {day_end} \nEnter a valid day\n"
            if day_end < day_start:
                print("The End date must be greater or equal to the starting Date")
                continue
            if month == 9 or month == 4 or month == 6 or month == 11:
                if day_end < 1 or day_end > 30:
                    print(day_end_error)
                    continue
            elif month == 2:
                if year % 4 == 0:
                    if day_end < 1 or day_end > 29:
                        print(day_end_error)
                        continue
                else:
                    if day_end < 1 or day_end > 28:
                        print(day_end_error)
                        continue
            else:
                if day_end < 1 or day_end > 31:
                    print(day_end_error)
                    continue
            break
        except ValueError:
            print("Invalid! Enter a Numeric value")

    for i in range(day_start, day_end + 1):
        response = requests.get(f"{url}api_key={myapi}&country={country}&year={year}&month={month}&day={day_start}")
        holiday = response.json()
        pairs = []
        for kp in holiday:
            pairs = kp
        if holiday:
            pair_value = list(pairs.values())
            pair_keys = list(pairs.keys())
        else:
            print(f"There is no holiday on {month}/{day_start}/{year}")
            day_start += 1
            time.sleep(1)
            continue
        holiday_csv = pd.DataFrame({
            'Country Info': pair_keys,
            'Holiday Info': pair_value
        })
        holiday_csv_space = pd.DataFrame({
            "a": [''],
            "b": ['']
        })
        holiday_csv.index = holiday_csv.index + 1
        print(holiday_csv)
        if country:
            holiday_csv.to_csv(f'{country}_holiday_csv_file.csv', mode="a", index=False, header=False)
            holiday_csv_space.to_csv(f'{country}_holiday_csv_file.csv', sep=" ", mode="a", index=False, header=False)
        day_start += 1
        time.sleep(1)

    print("------Successfully executed-----")
    count+=1
