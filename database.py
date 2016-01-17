class Table():
    '''A class to represent a SQuEaL table'''

	dict = {}
	
    	def set_dict(self, new_dict):
        '''(Table, dict of {str: list of str}) -> NoneType

        Populate this table with the data in new_dict.
        The input dictionary must be of the form:
            column_name: list_of_values
        '''
		str = new_dict.split(": ")
		key = str[0]
		value = str[1]
		self.dict[key] = value

    	def get_dict(self):
        '''(Table) -> dict of {str: list of str}

        Return the dictionary representation of this table. The dictionary keys
        will be the column names, and the list will contain the values
        for that column.
        '''
		return self.dict

	def get_item(self, key):
		return self.dict[key]

	def get_keys(self):
		return self.dict.keys()

	def join_tables(self,table):
		keys = table.dict.keys()
		for key in keys:
			self.dict[key] = table.dict[key]
		return self.dict
	
	def get_row_eql(self,columns,pcol,pval):
		plist = self.dict[pcol]
		index = plist.index(pval)
		cur_row = []
		for column in columns:
			cur_row.append((self.dict[column])[index])
		return cur_row
		
	def get_row_all_eql(self,pcol,pval):
		plist = self.dict[pcol]
		index = plist.index(pval)
		cur_row = []
		for column in self.get_keys():
			cur_row.append((self.dict[column])[index])			
		return cur_row
	
	def get_rows_gt(self,columns,pcol,pval):
		plist = self.dict[pcol]
		list_of_rows = []
		for val in plist:
			if val > pval :
				cur_row = []
				index = plist.index(val)
				for column in columns:
					cur_row.append((self.dict[column])[index])
				list_of_rows.append(cur_row)
		return list_of_rows
		
	def get_rows_all_gt(self,pcol,pval):
		plist = self.dict[pcol]
		list_of_rows = []
		for val in plist:
			if val > pval:
				cur_row = []
				index = plist.index(val)
				for column in self.get_keys():
					cur_row.append((self.dict[column])[index])
				list_of_rows.append(cur_row)
		return list_of_rows
	
	def get_row(self,index):
		list_of_columns = self.get_keys()
		cur_row = []
		for column in list_of_columns:
			cur_row.append(self.dict[column])[index])
		return cur_row
	
			
	def row_to_dict(columns,list_of_rows):
		i = 0
		table = Table()
		for column in columns:
			table[column] = [item[i] for item in list_of_rows]
			i = i + 1
		return table
		
		


class Database():
    '''A class to represent a SQuEaL database'''
	
	dict = {}
	
    	def set_dict(self, new_dict):
        '''(Database, dict of {str: Table}) -> NoneType

        Populate this database with the data in new_dict.
        new_dict must have the format:
            table_name: table
        '''
		
		str = new_dict.split(": ")
		key = str[0]
		value = str[1]
		self.dict[key] = value
		

    	def get_dict(self):
        '''(Database) -> dict of {str: Table}

        Return the dictionary representation of this database.
        The database keys will be the name of the table, and the value
        with be the table itself.
        '''
        	return self.dict
