Stock Parse
-----------

A Python 3 commandline application that analyses index, stock, and trade data. All data is input via CSV files.
 
**Important:** Run `sample_data/update_trade_data.py` to update  `trade_data.csv` with recent timestamps in order for it to return useful data. 
This is due to the trades being filtered to only look for those in the last 15 mins. 

Running the application
-----------------------
The application can be run in one of three ways.Examples use files found in the ./sample_data path.

**Commandline Arguments**

    # index analysis
    -i --index file_name
    # stock analysis
    -s --stock file_name
    # trade analysis
    -t --trade file_name
    
**1 - From source code**

    export PYTHONPATH=.
    python src/stock_parse.py -i sample_data/index_data.csv
    python src/stock_parse.py -s sample_data/stock_data.csv
    python src/stock_parse.py -t sample_data/trade_data.csv
Note: If running in windows `set PYTHONPATH=.`

**2 - As a console script**

    pip install .
    stock_parse -i sample_data/index_data.csv

**3 - In jupyter notebook**

Open the file `stock_analysis.ipynb`

    jupyter notebook

To install iPython notebook

    pip3 install jupyter
   
##### Dependencies
There are currently no requirements for the app. There is one requirement `mock` for testing.

Input File Schema
-----------------
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


Testing
-------
To run all unit tests:

    pip install -r requirements.test.txt
    python -m unittest discover -v -s tests

### Improvement Areas
* Testing of print statements in stock_parse.py
* Duplicate code in stock_parse:run_analysis()
* Add arg to set "interval" start/end date
