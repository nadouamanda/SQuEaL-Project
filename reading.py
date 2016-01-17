# Functions for reading tables and databases

import glob
from database import *

# a table is a dict of {str:list of str}.
# The keys are column names and the values are the values
# in the column, from top row to bottom row.

# A database is a dict of {str:table},
# where the keys are table names and values are the tables.

# YOU DON'T NEED TO KEEP THE FOLLOWING CODE IN YOUR OWN SUBMISSION
# IT IS JUST HERE TO DEMONSTRATE HOW THE glob CLASS WORKS. IN FACT
# YOU SHOULD DELETE THE PRINT STATEMENT BEFORE SUBMITTING

# Write the read_table and read_database functions below

def read_table(db, tbl):
    path = db + "/*.csv"
    file_list = glob.glob(path)
    tbl = db + tbl + '.csv'
    if tbl in file_list:
		fobj = open(tbl)
		return fobj.read()
    return null
	
def read_database(db):
    path = db + '/*.csv'
    db_list = glob.glob('*.csv')
    for s in db_list:
		s.strip('.csv')
    for s in db_list:
        if '/' in s:
            param,s = s.split('/',1)
	
	return db_list
	
	

	
	
	
