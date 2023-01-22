from util import *


class CSV_reader:
    def __init__(self):
        self.handler = File_Handler()

    def run(self):
        self.handler.handle_csv("./all_test.csv")


if __name__ == '__main__':
    app = CSV_reader()
    app.run()
