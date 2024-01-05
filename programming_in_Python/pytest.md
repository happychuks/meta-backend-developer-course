# PyTest cheat sheet

### Installation
Run the following on the Terminal:

pip3 install pytest (Mac)

Or

pip install pytest (Windows)

## Nomenclature

Add suffix 'test_' to the file that needs to be tested.

Add suffix 'test_' to the functions to be tested.

Running pytest
This is the command that has to be executed on the Terminal prompt:

python3 -m pytest test_file.py

Alternative method

py.test will look for the keyword test and run the tests over those files and functions automatically.

py.test test_file.py

When you run pytest for a specific function add     ::    to run a specific function in a given file.

Flags used
For example, -v is the flag:

python3 -m pytest abc.py -v

Some other flag options are:
```bash
-v for verbose
-q quiet mode
-s allows the print statement inside the functions to be executed
-x is to flag the tests to stop execution after first failure
-m is used to mark a specific function
-k is a flag for searching and running tests with a specific keyword
--tb is to disable the traceback code of errors
--maxfail n specifies maximum number of test fails allowed
```
