Stock Parse
-----------

A Python 3 commandline application that analyses index, stock, and trade data. All data is input via CSV files.

##### Input File Schema
All strings in the CSV files are quoted. Any unquoted data is treated as a float.

###### Index file:

    "symbol","price"
    "ABC",10.50

###### Stock file:

    "symbol","type","last_dividend","fixed_dividend","par_value","price"
    "ABC","common",10,0,50,10.50

###### Trade file:

    "symbol","price","volume","trade_type","trade_date"
    "ABC",10.50,1000,"buy","01-01-2000 12:00:00"

Running the application
-----------------------
##### Dependencies
There are currently no requirements.

Testing
-------
To run all unit tests:

    pip install -r requirements.test.txt
    python -m unittest discover -v -s tests
    