import requests
import pandas as pd
import time

my_api = "7b83d100d7e14c5fbc8705ffe33cbb8d"
url = "https://holidays.abstractapi.com/v1/?"


count = 0
while count < 2:

    country = input("which country: ").upper()
    while country.isalpha() is not True or len(country) != 2:
        print("Invalid Input\n")
        country = input("Enter a valid alpha 2 Country Code: ").upper()

    while country.isalpha() is True:

        try:
            # time.sleep(1)
            # print(requests.get(f"{url}api_key={my_api}&country={country}&year=2022&month=12&day=1").json())
            time.sleep(1)
            res = requests.get(f"{url}api_key={my_api}&country={country}&year=2022&month=12&day=1")
            test = res.json()
            if type(test) is dict:
                print(f"No country uses {country}  ")
                country = input("Enter a valid alpha 2 Country Code: ").upper()
                while country.isalpha() is not True or len(country) != 2:
                    print("Invalid Input\n")
                    country = input("Enter a valid alpha 2 Country Code: ").upper()
                continue
            elif type(test) is list:
                break
            else:
                print("unknown error")
                quit()
            break
        except ValueError:
            print("Enter a Valid Country Code")
            country = input("Enter a valid alpha 2 Country Code: ").upper()
        except ConnectionError:
            print("please Check Your Connection")
        except Exception:
            print("Please Check Your Internet and Try again")
            country = input("which Country: ").upper()
        break
    while True:
        try:
            year = int(input("Year: "))
            if year < 1800 or year > 19999:
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
        day_end = int(input("To which day?: "))
        try:
            # day_end = int(input("To which day?: "))
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

    run = True
    while run:
        for i in range(day_start, day_end + 1):
            response = requests.get(f"{url}api_key={my_api}&country={country}"
                                    f"&year={year}&month={month}&day={day_start}")
            holiday = response.json()
            # pairs = []
            # for kp in holiday:
            #     pairs = kp
            try:
                if holiday:
                    # pair_value = list(pairs.values())
                    # pair_keys = list(pairs.keys())
                    holiday_csv = pd.DataFrame(holiday)

                    # holiday_csv = pd.DataFrame({
                    #     'Country Info': pair_keys,
                    #     'Holiday Info': pair_value
                    # })
                    holiday_csv_space = pd.DataFrame({
                        "a": [''],
                        "b": ['']
                    })
                    holiday_csv.index = holiday_csv.index + 1
                    print(holiday_csv)
                    if count < 1:
                        holiday_csv.to_csv(f'{country}_holiday_csv_file.csv', mode="a", index=False, header=False)
                        holiday_csv_space.to_csv(f'{country}_holiday_csv_file.csv', sep=" ", mode="a", index=False,
                                                 header=False)
                        day_start += 1
                        time.sleep(1)
                        print("------Executed-----")

                else:
                    print(f"There is no holiday on {month}/{day_start}/{year}")
                    day_start += 1
                    time.sleep(1)
                    continue
            except ValueError:
                print("You must have inserted an invalid information")
            run = False
        count += 1
print("------Successfully executed-----")
