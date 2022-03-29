from lib.sitepackages import pypyodbc

file = '.\\TennisClub.mdb'
conn = pypyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ='+file)
cursor = conn.cursor()

SQL = "select * from member"
rows = cursor.execute(SQL)
for row in rows: # cursors are iterable
	print(row[1],row[2],row[3],row[4])
	