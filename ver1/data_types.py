'''

'''

class Input:
    def __init__(self):
        self.users = {}

class User:
    def __init__(self):
        self.months = {}

class Month:
    def __init__(self):
        self.dates = {}
        self.minBalance = float("inf") # to be converted to int
        self.maxBalance = float("-inf") # to be converted to int
        self.endBalance = 0

class Date:
    def __init__(self):
        self.cred = 0
        self.debt = 0