"""
Providing a tester program for debugging or
in the case the built executable does not work on a certain machine.
Runs on the terminal: no GUI provided;
Please refer to README.md for usage.
"""

import sys
from util import *


class CSV_reader:
    def __init__(self):
        self.handler = File_Handler()

    def run(self, in_file, out_file):
        self.handler.handle_csv(in_file, out_file)


if __name__ == '__main__':
    app = CSV_reader()
    app.run(sys.argv[1], sys.argv[2])