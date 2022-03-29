from lib.sitepackages import pypyodbc
DBfile = '.\\TennisClub.mdb'
conn = pypyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ='+DBfile)
myCursor = conn.cursor()
SQL = "insert into member(firstname, surname, dateofbirth, membertype) values ('Joe','Bloggs','Senior','01/01/2010')"
row = myCursor.execute(SQL)
myCursor.commit()
