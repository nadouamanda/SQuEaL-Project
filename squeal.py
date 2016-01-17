from reading import *
from database import *

# Below, write:
# *The cartesian_product function
# *All other functions and helper functions
# *Main code that obtains queries from the keyboard,
#  processes them, and uses the below function to output csv results


def print_csv(table):
    '''(Table) -> NoneType
    Print a representation of table.
    '''
    dict_rep = table.get_dict()
    columns = list(dict_rep.keys())
    print(','.join(columns))
    rows = num_rows(table)
    for i in range(rows):
        cur_column = []
        for column in columns:
            cur_column.append(dict_rep[column][i])
        print(','.join(cur_column))

if(__name__ == "__main__"):
    	query = input("Enter a SQuEaL query, or a blank line to exit:")

        def run_query(db,query):
			col = query.split('select ')[1].split(' from')[0]
			columns = col.split(",")
			result = Table()
			t = Table()
			row = Table()

			if col == '*':
					selectAll = 'true'
			else:
					selectAll = 'false'

			if "where" in query:
				tbl = (query.split('from: ')[1].split(' where’)[0]).split(“,”)
				cst = query.split('where ')[1]
				if ‘=‘ in cst:
					constrains = cst.split(‘=‘)
					leftval = constrains[0]
					rightval = constrains[1]
					fin_row = []
					
					if “\’” in rightval:
						for tbl in tbl:
							table = read_table(db,tbl)
							if leftval in table.get_keys():
								if selectAll:
									c = table.get_keys()
									fin_row.append(table.get_row_all_eql(leftval,rightval))
								else:
									c = columns
									fin_row.append(table.get_row_eql(columns,leftval,rightval))
									
						result = row_to_dict(c,fin_row)
						print_csv(result)
					else:
						for tbl in tbl:
							table = read_table(db,tbl)
							if leftval in table.get_keys():
								leftlist = table.get_item(leftval)
								lefttable = table
							if rightval in table.get_keys():
								rightlist = table.get_item(rightval)
								righttable = table
							
						for l in leftlist:
							for r in rightlist:
								if l == r :
									if selectAll:
										fin_row.append(lefttable.get_row_all_eql(leftval,l) + righttable.get_row_all_eql(rightval,r))	
									else:
										fin_row.append(lefttable.get_row_eql(columns,leftval,l) + righttable.get_row_eql(columns,rightval,r))
							
						if selectAll:
							c = lefttable.get_keys() + righttable.get_keys()
						else:
							c = columns
						
						result = row_to_dict(c,fin_row)
						print_csv(result)

	
				if ‘>’ in cst:
					constrains = cst.split(‘>’)
					leftval = constrains[0]
					rightval = constrains[1]
					fin_row = []
					
					if "\'" in rightval:
						for tbl in tbl:
							table = read_table(db,tbl)
							if leftval in table.get_keys():
								if selectAll:
									c = table.get_keys()
									fin_row += table.get_rows_all_gt(leftval,rightval)
								else:
									c = columns
									fin_row += table.get_rows_gt(columns,leftval,rightval)
						result = row_to_dict(c,fin_row)
						print_csv(result)
					else:
						for tbl in tbl:
							table = read_table(db,tbl)
							if leftval in table.get_keys():
								leftlist = table.get_item(leftval)
								lefttable = table
							if rightval in table.get_keys():
								rightlist = table.get_item(rightval)
								righttable = table
						for l in leftlist:
							for r in rightlist:
								if l > r:
									if selectAll:
										fin_row += (lefttable.get_row_all_eql(leftval,l) + righttable.get_row_all_eql(rightval,r))	
									else:
										fin_row += (lefttable.get_row_eql(columns,leftval,l) + righttable.get_row_eql(columns,rightval,r))
							
						if selectAll:
							c = lefttable.get_keys() + righttable.get_keys()
						else:
							c = columns
						
						result = row_to_dict(c,fin_row)
						print_csv(result)
							
			else:
				tbl = (query.split('from ‘)[1]).split(“,”)
				for tbl in tbl:
					table = read_table(db,tbl)
					if selectAll:
						result.join_tables(table)
					else:
						for c in col:
							if c in table.get_keys():
								t[c] = table.get_item(c)
						result.join_tables(t)

				print_csv(result)

	

	def cartesian_product(tbl1,tbl2):
		rows1 = num_rows(tbl1)
		rows2 = num_rows(tbl2)
		fin_row = []
		for i in range(rows1):
			for j in range(rows2):
				fin_row.append(tbl1.get_row(i) + tbl2.get_row(j))
		c = tbl1.get_keys() + tbl2.get_keys()
		result = row_to_dict(c,fin_row)
		print_csv(result)
				
		
		