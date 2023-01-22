"""
The main program that calls the helper functions and provides a minimalistic Graphical User Interface;
Please refer to README.md for usage.
"""

import tkinter as tk
import tkinter.filedialog as filedialog
from util import *

# Create the main window
root = tk.Tk()

# Set the title of the window
root.title("CSV Assistant 1.0")
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()


# Main function to process the CSV file
def run():
    # Ask the user to select a CSV file
    in_file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    out_file_path = filedialog.asksaveasfilename(filetypes=[("CSV files", "*.csv")], initialfile='data.csv')

    # Call helper functions to read, process, and save data
    handler = File_Handler()
    handler.handle_csv(in_file_path, out_file_path)

    # Ask the user if they want to process another file
    result = tk.messagebox.askyesno("Question", "Do you want to process another CSV file?")
    if result:
        # Process another file
        run()


# Create a button to start the CSV processing
button = tk.Button(root, text="Process a CSV", command=run)
button.pack()
canvas.create_window(150, 150, window=button)

# Run the main loop
root.mainloop()