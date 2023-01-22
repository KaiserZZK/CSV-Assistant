## Welcome to `CSV Assistant 1.0`!


### What it does
This is a simple program that takes CSV files with the following format:
* CustomerID
* Date
* Amount

and generates an output file with the data:
* CustomerID
* MM/YYYY
* Min Balance: Lowest Balance recorded in a month between Day 1 to Day 30
* Max Balance: Highest Balance recorded in a month between Day 1 to Day 30
* Ending Balance: Remaining balance after the Day 30 transaction


### Environmental Prerequisites
The executable, `CSV-Assistant-1.0`, is built with `PyInstaller`. The file is self-contained
and does not require your computer to have Python installed to be executed.

***However***, PyInstaller is OS-dependent: this executable is coded and built 
under the `macOS version 12.5` environment; and it could only be run on a macOS 
machine. 
* To build executable from source-code for non-macOS platforms like Windows, 
please kindly refer to the **Building Executable for other Environments** section;
* To customize the source-code for optimization and further development, please
have `Python 3.9.12` and above installed on your machine, and consult the 
**Customizing Program** section.


### How to use 
Assuming you are currently on a macOS environment:
* macOS is strict about distributed programs like this one; hence your machine is
likely not allowing you to open `CSV Assistant 1.0` by double-clicking the icon.
If this is the case, kindly control-click on the icon then select "open".
* If the program is still not running, please refer to the **Customizing Program** 
section for instructions on how to run the program in your local terminal.

If the program runs, and you are seeing the following interface:
![alt text](./starting.png)
./illustrations/starting.png=250x)

1. 

Thanks!

### Building Executable for other Environments
PyInstaller can be used to create executables for both Mac and Windows platforms. 
However, you will need to run PyInstaller on a machine that is running the 
platform for which you want to create the executable.

to build a Windows copy, please navigate to the `source` folder and run the 
following command: 

Install PyInstaller using `pip`:
```commandline
pip3 install pyinstaller
```
Run the following command to create an executable:
```commandline
pyinstaller -F -w -n app-name main.py
```
This will create a single file executable with a console window hidden and the specified name app-name.
* The `-F` flag specifies that PyInstaller should create a single file executable.
* The `-w` flag hides the console window when running the executable.
* The `-n app-name` flag specifies the name of the executable file.

For more information, please kindly refer to the `PyInstaller` documentation at https://pyinstaller.readthedocs.io/


### Customizing Program 
Implements a tree-like structure

1. `util.py` 
- should be constant time 
2. `main.py`

3. `tester.py`
```commandline
python3 tester.py ./in_test.csv ./out_test.csv
```
