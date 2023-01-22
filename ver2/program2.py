import tkinter as tk
import tkinter.filedialog as filedialog

from util import *

# create the main window
root = tk.Tk()

# ask the user to select a CSV file
file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
handler = File_Handler()
handler.handle_csv(file_path)

# run the main loop
root.mainloop()
