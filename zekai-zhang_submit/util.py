"""
Defines classes and objects for organizing the data from input files;
Provides helper functions for reading, processsing, and saving input data;
Please refer to README.md for code anatomy.
"""

import csv


# Class for storing the input rows
class Input:
    def __init__(self):
        self.users = {}


# Class for storing all data belonging to a single user
class User:
    def __init__(self):
        self.months = {}


# Class for storing all data within a single month by a single user
class Month:
    def __init__(self):
        self.dates = {}
        self.minBalance = float("inf")  # to be converted to int
        self.maxBalance = float("-inf")  # to be converted to int
        self.endBalance = 0

# Class for storing credit and debit sums within a single day, in a month, by a single user
class Date:
    def __init__(self):
        self.cred = 0
        self.debt = 0


# Class for handling a given CSV file
class File_Handler:
    def __init__(self):
        self.file = Input()

    # Read, process, and save data
    def handle_csv(self, input_file, output_file):
        raw_data = self.read_csv(input_file)
        processed_data = self.process_csv(raw_data)
        self.save_csv(processed_data, output_file)

    # Open and read a given CSV file
    def read_csv(self, file_name):
        form = self.file

        with open(file_name, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                # Display raw data
                # print(row)

                # Skip empty rows
                if row[0] == "" or row[1] == "" or row[2] == "":
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

        return form

    # Process the raw data
    def process_csv(self, file):
        data = []

        for user, month in file.users.items():
            # Sort by key value (month)
            sorted_months = sorted(month.months.items(), key=lambda x: x[0])
            for m, date in sorted_months:
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
                # print(user, m, date.minBalance, date.maxBalance, date.endBalance)
                data.append({'CustomerID': user, 'MM/YYYY': m, \
                             'MinBalance': date.minBalance, 'MaxBalance': date.maxBalance, \
                             'EndingBalance': date.endBalance})

        # print(data)
        return data

    # Save processed data to an output file
    def save_csv(self, data, file_path):
        # Define column headers
        fields = ['CustomerID', 'MM/YYYY', \
                  'MinBalance', 'MaxBalance', 'EndingBalance']

        # Create the output CSV file
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            for d in data:
                writer.writerow(d)

        # print("output file generated and saved!")