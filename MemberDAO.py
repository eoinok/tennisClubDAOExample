from lib.sitepackages import pypyodbc
from Member import Member
class MemberDAO():
    def __init__(self):
        DBfile = '.\\TennisClub.mdb'
        conn = pypyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ='+DBfile)
        self.cursor = conn.cursor()

    def saveMember(self,thisMember):
        #add code to insert the details contained in thisMember here
        print("this is where the save member code should go")

    def getAllMembers(self):
        print("this is where the get all members code should go")
        #set up an empty list to store the result
        #set up a string called SQL containing a query to pull all Members from the DB
        #execute the query contained in the SQL string against the cursor object
        #loop through the cursor object result
            #each time around the loop use the values contained in row[1],row[2]... etc to create a Member object
            #add the object to the list
        #return the result
        
