class Member():
    def __init__(self,arg1,arg2,arg3,arg4):
        self.__firstname=arg1
        self.__surname=arg2
        self.__dob=arg3
        self.__memberType=arg4

    def getFirstname(self):
        return self.__firstname

    def getSurname(self):
        return self.__surname
    
    def getDOB(self):
        return self.__dob

    def getMemberType(self):
        return self.__memberType

    def __str__(self):
        return self.__firstname + " " + self.__surname
