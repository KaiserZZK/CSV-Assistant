import tkinter as tk
import tkinter.filedialog as filedialog
import csv

# create the main window
root = tk.Tk()

# ask the user to select a CSV file
file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

# read the CSV file
with open(file_path, 'r') as csvfile:
    # create a CSV reader
    reader = csv.reader(csvfile)

    # read the rows of the CSV file
    for row in reader:
        print(row)

# run the main loop
root.mainloop()
