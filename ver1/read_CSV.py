from data_types import *

import csv

form = Input()

with open("./all_test.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        # Display raw data
        print(row)
        if row[0]=="" or row[1] =="" or row[2] == "":
            continue

        userID = row[0]
        if userID not in form.users:
            form.users[userID] = User()
        currentUser = form.users[userID]

        month = row[1][:2] + row[1][5:]
        if month not in currentUser.months:
            currentUser.months[month] = Month()
        currentMonth = currentUser.months[month]

        date = row[1][3:5]
        if date not in currentMonth.dates:
            currentMonth.dates[date] = Date()
        currentDate = currentMonth.dates[date]

        amount = int(row[2])
        if amount >= 0:
            currentDate.cred += amount
        else:
            currentDate.debt += amount

for user, month in form.users.items():
    # Sort by key value (month)
    sorted_months = sorted(month.months.items(), key=lambda x: x[0])
    for month, date in sorted_months:
        # Sort by key value (date)
        sorted_dates = sorted(date.dates.items(), key=lambda x: x[0])
        currentBalance = 0
        for d, amount in sorted_dates:
            # print(user, month, d, amount.cred, amount.debt)
            # Update minBalance, maxBalance, endBalance
            currentBalance += amount.cred
            if amount.cred != 0:
                date.maxBalance = max(date.maxBalance, currentBalance)
                date.minBalance = min(date.minBalance, currentBalance)
            currentBalance += amount.debt
            if amount.debt != 0:
                date.maxBalance = max(date.maxBalance, currentBalance)
                date.minBalance = min(date.minBalance, currentBalance)
        date.endBalance = currentBalance
        print(user, month, date.minBalance, date.maxBalance, date.endBalance)