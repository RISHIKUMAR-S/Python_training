from sql_metadata import Parser

# get tables from query - for more examples see `tests/test_getting_tables.py`
#Parser("SELECT a.* FROM product_a.users AS a JOIN product_b.users AS b ON a.ip_address = b.ip_address").tables
# ['product_a.users', 'product_b.users']

table1 = Parser("SELECT DEPT, ID FROM DEPARTMENT").tables
# ['DEPARTMENT']
print(table1)

# you can also extract aliases of the tables as a dictionary
parser = Parser("SELECT EMP_ID FROM DEPARTMENT AS D")
print(parser)
# get table aliases
print(parser.tables_aliases)
# {'D': 'DEPARTMENT'}

# note that aliases are auto-resolved for columns
print(parser.columns)

